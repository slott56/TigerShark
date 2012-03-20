#!/usr/bin/env python
"""Claims_837 views."""
from django.http import HttpResponse
from web.claims_837.models import Factory
from web.claims_837.parse import parse_837p, parse_837i, parse_837d
from web.claims.models import (
    X12Message, Location, ClaimType, SecondaryCoverage, Benefit, TypeOfService,
    ClaimProperties, ClaimGroup, GroupStatus )
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import X12.parse
from django.core import serializers

def home( request ):
    return HttpResponse("Claims_837: {0} rows.".format(X12Message.objects.count()) )

@csrf_exempt
def load( request ):
    """POST request with claim, claim_id, properties.
    Use the "claims_837" model.
    """
    if request.method == 'POST':
        claim= request.POST['claim']
        claim_id= request.POST['claim_id']
        prop_json= request.POST.get('properties',{})
        properties= json.loads( prop_json )
        cons_json= request.POST.get('constraints',{})
        constraints= json.loads( cons_json )
        try:
            loader= Loader() # Could be a different configuration
            msg= loader.load( claim, claim_id, properties, constraints )
            response= {'claim': msg.marshall(), 'claim_id':msg.name,
                       'group_name':msg.group.name, 'message':None}
            return HttpResponse( content=json.dumps(response), status=201, content_type='application/json' )
        except Exception as e:
            return HttpResponse( content=json.dumps(repr(e)), status=404, content_type='application/json' )
    raise Http404

def fetch( request, claim_id ):
    """GET request with claim_id.
    Fetch a given claim from the database.  Marshall it as an X12 message.
    
    :param claimID: the claim identifier provided when the claim was loaded.
    :return: status tuple ( status, message )
    """
    try:
        claim= X12Message.objects.get( name=claim_id )
        if claim:
            object= { 'claim_id': claim_id, 'claim': claim.marshall(), 'message': None }
            status= 200
        else:
            object= { 'claim_id': claim_id, 'claim': None, 'message': "No claim matches %r" % ( claim_id ) }
            status= 404
    except X12Message.DoesNotExist, e:
        object= { 'claim_id': claim_id, 'claim': None, 'message': "No claim matches %r" % ( claim_id ) }
        status= 404
    except Exception, e:
        logger.exception( e )
        object= { 'claim_id': claim_id, 'claim': None, 'message': "Internal Error %r" % ( claim_id ) }
        status= 500
        
    return HttpResponse( content=json.dumps(object), status=status, content_type='application/json' )


class Loader( object ):
    """Load claims_837-specific claim segments.
    Loading a claim, creates the associated properties,
    automod constraints, and a default group that claims are loaded to.
    """
    def __init__( self ):
        """Initialize an instance of  Loader."""
        self.log= logging.getLogger( "web.claims_837.views.Loader" )
    def _conformProperties( self, properties ):
        """Conform the given set of properties attributes to a :class:`ClaimProperties`
        object.  This will either get an existing properties object or create a new
        properties object.
        The argument value must be a dictionary with the following attributes:

            - ``TYPE`` - this must resolve to a name in the :class:`ClaimType` table.

            - ``SECONDARY`` - this must resolve to a name in the :class:`SecondaryCoverage` table.

            - ``LOCATION`` - This must resolve to a name in the :class:`Location` table.

            - ``BENEFIT`` - this must resolve to a name in the :class:`Benefit` table.

            - ``TYPE-OF-SERVICE`` - this is paired with Benefit to locate a row in the
              :class:`TypeOfService` table.

        :param properties: a dictionary with attributes for the properties.
        :return: A ClaimProperties object.
        """
        self.log.debug( "ClaimProperties: %r", properties )
        if properties is not None:
            loc, status= Location.objects.get_or_create( name = properties["LOCATION"] )
            ct, status= ClaimType.objects.get_or_create( name = properties["TYPE"] )
            sc, status= SecondaryCoverage.objects.get_or_create( name = properties["SECONDARY"] )
            ben, status= Benefit.objects.get_or_create( benefit=properties["BENEFIT"])
            tos, status= TypeOfService.objects.get_or_create( benefit=ben, typeOfService=properties["TYPE-OF-SERVICE"] )
            props, status = ClaimProperties.objects.get_or_create(
                claimType= ct,
                secondaryCoverage= sc,
                location= loc,
                typeOfService= tos, )
            return props
    def _defaultGroup( self, properties, user="Owner" ):
        """Loading always allocates a default group, based on the ClaimProperties,
        user and a fixed :class:`GroupStatus` of ``Base``.
        """
        claimProperties= self._conformProperties( properties )
        group, status = ClaimGroup.objects.get_or_create(
            name=claimProperties.shortName(),
            description=claimProperties.fullName(),
            status= GroupStatus.objects.get(name='Base'),
            owner=user,
            )
        return group

    def load( self, claim, claimID, properties, constraints ):
        """Load a Claim, conforming it with ClaimProperties.
        The various parsers (:class:`parse_837p`, :class:`parse_837i`, :class:`parse_837d`) defined
        in L{web.claims_837.parse} are tried to see which can successfully
        parse the message.  If the message can be parsed, the resulting object
        is persisted in the database, associated with the given properties.
        
        Note that the properties are conformed into several
        different dimensions.  If there are unique values in the attributes,
        new rows will be created in the dimension tables. 

        :param claim: source text for an ``837`` claim.
        :param claimID: a unique identifier for this claim.
        :param properties: dictionary of properties attributes,
            used by :class:`_conformProperties`
        :return: the Claim loaded or an exception
        """
        self.log.debug( "X12Message: %r", claim )
        msg= None
        for parser in ( parse_837p, parse_837i, parse_837d ):
            try:
                parser.unmarshall( claim )
                msg= parser.unmarshall( claim, Factory )
                msg.name= claimID
                msg.properties= self._conformProperties( properties )
                msg.group= self._defaultGroup( properties, "Owner" )
                msg.save()
                self.log.debug( "Parser %s loaded %s", parser.desc, claimID )
                break
            except X12.parse.ParseError, e:
                # If we break trying to recognize the GS, then we're using the wrong parser
                messageDesc, parser, segments = e.args
                if segments is not None and segments[0][0] == 'GS':
                    self.log.debug( "Message didn't match %s", messageDesc )
                else:
                    # This is a more serious problem with message or parser.
                    self.log.error( "Error in parser %s", parser )
                    e.log( log )
                msg= None
            except Exception, e:
                # This is a non-parser error: it's some kind of bug.
                self.log.error( "*** %r", e )
                raise
        if msg is None:
            self.log.warning( "Could not parse %r", claim )
            raise X12.parse.ParseError( "Could not parse" )
        return msg