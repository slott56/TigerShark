#!/usr/bin/env python
"""Claims view functions.
"""
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from web.claims.models import (
    X12Message, Factory, Location, ClaimType, SecondaryCoverage,
    Benefit, TypeOfService, ClaimProperties, TestConstraints, ClaimGroup,
    GroupStatus,
    )
import json
import logging, sys
import X12.parse
from web.claims.parse import parser

logging.basicConfig( stream= sys.stderr )
logger = logging.getLogger( __name__ )

def home( request ):
    return HttpResponse("Claims Home Page.")

@csrf_exempt
def load( request ):
    """POST request with claim, claim_id, properties, constraints.
    
    The POST request has four parameters:

    :claim: is the X12-encoded message.
    :claim_id: is the user-assigned unique ID for this claim.
    :properties: is a JSON-encoded Properties object for this claim.
    :constraints: is a JSON-encoded TestConstraint object for this claim.
    """
    if request.method == 'POST':
        claim= request.POST['claim']
        claim_id= request.POST['claim_id']
        prop_json= request.POST.get('properties',{})
        properties= json.loads( prop_json )
        cons_json= request.POST.get('constraints',{})
        constraints= json.loads( cons_json )
        try:
            loader= Loader(parser) # Could be a different configuration
            msg= loader.load( claim, claim_id, properties, constraints )
            response= {'claim': msg.marshall(), 'claim_id':msg.name,
                       'group_name':msg.group.name, 'message':None}
            return HttpResponse( content=json.dumps(response), status=201, content_type='application/json' )
        except Exception as e:
            logger.exception( "claims.views.load")
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
    """Load generic claims.
    Loading a claim, creates the associated properties,
    test constraints, and a default group that claims are loaded to.
    """
    def __init__( self, parser ):
        """Initialize an instance of Loader."""
        self.log= logging.getLogger( "web.claims.views.Loader" )
        self.parser= parser
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
    def _conformConstraints( self, x12message, constraints ):
        """Conform the given set of properties attributes to an :class:`TestConstraints`
        object.  This will either get an existing constraints object or create a new
        constraints object.

        The argument value must be a dictionary with the following attributes:

            - ``GENDER`` - This must resolve to a name in the :class:`Location` table.

            - ``AGE-FROM`` - this must resolve to a name in the :class:`ClaimType` table.

            - ``AGE-TO`` - this must resolve to a name in the :class:`SecondaryCoverage` table.

        :param constraints: a dictionary with attributes for the constraints.
        :return: An TestConstraints object.
        """
        self.log.debug( "TestConstraints: %r", constraints )
        if constraints is not None:
            tcons, status = TestConstraints.objects.get_or_create(
                gender= constraints["GENDER"],
                age_low= constraints["AGE-FROM"],
                age_high= constraints["AGE-TO"],
                message= x12message)
            return tcons
    def load( self, claim, claimID, properties, constraints ):
        """Load a Claim, conforming it with ClaimProperties and TestConstraints.
        A generic parser defined
        in :mod:`X12.parse` is tried to 
        parse the message.  If the message can be parsed, the resulting object
        is persisted in the database, associated with the given properties
        and constraints.
        
        Note that the properties and constraints are conformed into several
        different dimensions.  If there are unique values in the attributes,
        new rows will be created in the dimension tables.  If this is not
        intended, there are two choices:

            - Validate the constraints against the dimensions outside
              this service.

            - Report the new values in the dimension to the users and
              have them reassign the dimension values.  This seems
              like needless work, but it turns out to be simpler because
              it gets fewer rejections and helps users discover and respond
              to changes in the baseline claim-processing system.

        XXX - get actual user as an argument -- it's originally in the request.

        :param claim: source text for a generic X12 claim.
        :param claimID: a unique identifier for this claim.
        :param properties: dictionary of properties attributes,
            used by :meth:`_conformProperties`
        :param constraints: dictionary of automod constrain attributes,
            used by :meth:`_conformConstraints`
        :return: the Claim loaded or an exception
        """
        self.log.debug( "X12Message: %r", claim )
        try:
            msg= self.parser.unmarshall( claim, Factory )
            msg.name= claimID
            msg.properties= self._conformProperties( properties )
            msg.group= self._defaultGroup( properties, "Owner" )
            msg.save()
            self._conformConstraints( msg, constraints )
            self.log.debug( "Parser %s loaded %s", self.parser.desc, claimID )
            return msg
        except X12.parse.ParseError, e:
            # If we break trying to recognize the GS, then we're using the wrong parser
            messageDesc, parser, segments = e.args
            if segments is not None and segments[0][0] == 'GS':
                self.log.debug( "Message didn't match %s", messageDesc )
            else:
                # This is a more serious problem with message or parser.
                self.log.error( "Error in parser %s", parser )
                e.log( log )
            self.log.warning( "Could not parse %r", claim )
            raise 
        except Exception, e:
            # This is a non-parser error: it's some kind of bug.
            self.log.error( "*** %r", e )
            raise
