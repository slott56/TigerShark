#!/usr/bin/env python
"""The ``X12.map.dj`` package emits Django class definitions for Segment definitions.

See :ref:`traversal` for notes on the **Visitor** design pattern.

..  autoclass:: DjangoModelVisitor
    :members:
   
..  autoclass:: DjangoAdminVisitor
    :members:
"""
from tigershark.X12.parse import StructureVisitor
from tigershark.X12.parse import StopDescent

class DjangoModelVisitor( StructureVisitor ):
    """Emit Django class definitions for Segments.
    
    Extension to :class:`X12.parse.StructureVisitor`
    """
    def __init__( self, *args, **kw ):
        super( DjangoModelVisitor, self ).__init__( *args, **kw )
        self.result= ['from web.claims.models import X12Segment','from django.db import models','']
        self.segTypes= set()
    def preSegment( self, aSegment, indent=0 ):
        """Examine this Segment: is it a new type?"""
        if aSegment.name in self.segTypes:
            raise StopDescent( "Already seen this Segment Type" )
        self.segTypes.add( aSegment.name )
        self.result.append( 'class Segment_%s(models.Model):' % ( aSegment.name, ) )
        self.result.append( '    """%r"""' % ( aSegment.props,) )
        self.result.append( '    segment = models.ForeignKey( X12Segment )' )
    def postSegment( self, aSegment, indent=0 ):
        self.result.append( "    def unmarshall( self, segmentToken, cs=':' ):" )
        children= aSegment.structure
        for pos in range(len(children)):
            if len(children[pos].structure):
                # Composites have further decomposition
                self.result.append( "        # composite= segmentToken[%d].split(cs)" % ( pos+1, ) )
                subChildren= children[pos].structure
                for c in range(len(subChildren)):
                    self.result.append( "        self.%s = segmentToken.subElt(%d,cs,%d)" % (
                        self._fixName(subChildren[c].name), pos+1, c ))
            else:
                # Elements are atomic
                nm= children[pos].name
                self.result.append( "        self.%s = segmentToken.elt(%d)" % ( nm, pos+1 ) )
        self.result.append( "" )
    def preComposite( self, aComposite, indent=0 ):
        """Report this Composite."""
        self.result.append( '    # <Composite %r, %r, ' % (
            aComposite.name, aComposite.props ) )
    def _fixName( self, name ):
        return name.replace("-","_")
    def postElement( self, anElement, indent=0 ):
        """Report this Element."""
        elt= anElement
        opts= { 'max_length' : (16 if elt.max_len is None else int(elt.max_len)) }
        if elt.req_sit != "R":
            opts['blank']= True
            opts['null']= True
        # XXX - Use elt.type_name
        code= '    %s = models.CharField( %s ) # %r %r'
        optStr= ", ".join( [ '%s=%s' % (n,v) for n,v in opts.items() ] )
        self.result.append( code % ( self._fixName(elt.name), optStr, elt.props.data_type, elt.props.desc, ) )
    def getSource( self, appname='claims_837' ):
        return "\n".join( self.result )

class DjangoAdminVisitor( StructureVisitor ):
    """Emit Django admin definitions for Segments.
    
    Extension to :class:`X12.parse.StructureVisitor`
    """
    def __init__( self, *args, **kw ):
        super( DjangoAdminVisitor, self ).__init__( *args, **kw )
        self.result= ['from django.contrib import admin','']
        self.segTypes= set()
    def preSegment( self, aSegment, indent ):
        if aSegment.name in self.segTypes:
            raise StopDescent( "Already seen this Segment Type" )
        self.segTypes.add( aSegment.name )
    def getSource( self, appname='claims_837' ):
        def emitter( segTypes ):
            for aSegment in self.segTypes:
                yield 'from web.{0}.models import {1}'.format(appname,aSegment)
                yield 'admin.site.register( {1} )'.format(appname,aSegment)
        return "\n".join( emitter(self.segTypes) )
