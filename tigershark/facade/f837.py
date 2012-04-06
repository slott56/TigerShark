"""Defines an insurance Claim from a business perspective,
mapping to underlying X12 structures.

There are two parts to this module.

-   A **Facade** over :mod:`X12.message` structures.
    See `Facade Use Cases`_ and `Facade Implementation`_.

-   A mapping of a Claim, using the **Facade** elements.
    See `Claim Mapping`_.


Claim Mapping
===============

**Patient** - Loop 2000C

..  autoclass:: Patient
..  autoclass:: Instutitional_Patient
..  autoclass:: Institutional_Inpatient
..  autoclass:: Institutional_Outpatient
..  autoclass:: Professional_Patient

**Provider** - Loop 2000A (a/k/a BillingProvider)

..  autoclass:: Provider

**Submitter** - Loop 1000A

..  autoclass:: Submitter

**Subscriber** - Loop 2000B

..  autoclass:: Subscriber

**Paperwork** -

..  autoclass:: Paperwork

**ClaimDetails** - Superclass for portions of Loop 2300, including embedded paperwork
  and various "HI" composite objects.

..  autoclass:: ClaimDetails

**Institutional_ClaimDetails**

..  autoclass:: Institutional_ClaimDetails

**Professional_ClaimDetails**

..  autoclass:: Professional_ClaimDetails

**ServiceLine**

..  autoclass:: ServiceLine
..  autoclass:: Institutional_ServiceLine
..  autoclass:: Professional_ServiceLine
..  autoclass:: ServiceLineAdj

Top-Level **Claim**.

..  autoclass:: Claim
"""
from tigershark.facade import X12LoopBridge
from tigershark.facade import X12SegmentBridge
from tigershark.facade import ElementAccess
from tigershark.facade import SegmentSequenceAccess
from tigershark.facade import SegmentConversion
from tigershark.facade import SequenceOf
from tigershark.facade import ElementSequenceAccess
from tigershark.facade import CompositeAccess
from tigershark.facade import CompositeSequenceAccess
from tigershark.facade import D8


class Patient( X12LoopBridge ):
    """Patient Data from loop 2000C"""
    loopName= "2000C"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    id= ElementAccess( "NM1", 9 )
    addr1= ElementAccess( "N3", 1 )
    addr2= ElementAccess( "N3", 2 )
    city= ElementAccess( "N4", 1 )
    state= ElementAccess( "N4", 2 )
    zip= ElementAccess( "N4", 3 )
    country= ElementAccess( "N4", 4 )
    dob= ElementAccess( "DMG", 2, x12type=D8 )
    sex= ElementAccess( "DMG", 3 )
    ssn= ElementAccess( "REF", 2, qualifier=(1,"SY") )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Instutitional_Patient( Patient ):
    """Patient on an 837I claim."""
    rel= ElementAccess( "PAT", 1 )
    measCode= ElementAccess( "PAT", 7 )
    weight= ElementAccess( "PAT", 8 )
    resp= ElementAccess( "PAT", 9 )

class Institutional_Inpatient( Instutitional_Patient ):
    pass

class Institutional_Outpatient( Instutitional_Patient ):
    pass

class Professional_Patient( Patient ):
    """Patient on an 837P claim."""
    rel= ElementAccess( "PAT", 1 )
    dateFormat= ElementAccess( "PAT", 5 )
    dod= ElementAccess( "PAT", 6 )
    measCode= ElementAccess( "PAT", 7 )
    weight= ElementAccess( "PAT", 8 )
    preg= ElementAccess( "PAT", 9 )

class Provider( X12LoopBridge ):
    """Provider Data on the 2000A loop."""
    loopName= "2000A"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    nm106= ElementAccess( "NM1", 6 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    taxId= ElementAccess( "NM1", 9 )
    npi= ElementAccess( "NM1", 9 )
    nm109= ElementAccess( "NM1", 9 )
    addr1= ElementAccess( "N3", 1 )
    addr2= ElementAccess( "N3", 2 )
    city= ElementAccess( "N4", 1 )
    state= ElementAccess( "N4", 2 )
    zip= ElementAccess( "N4", 3 )
    country= ElementAccess( "N4", 4 )
    contact_name= ElementAccess( "PER", 1 )
    contact_funct= ElementAccess( "PER", 2 )
    # Email, Phone and Fax are all on the same segment in pairs (3,4), (5,6), (7,8)
    # First value is a qualifier: "EM", "TE" or "FX"
    # Second value is the number
    email= ElementAccess( "PER", oneOf=( "EM", (3,4), (5,6), (7,8) ) )
    fax= ElementAccess( "PER", oneOf=( "FX", (3,4), (5,6), (7,8) ) )
    phone= ElementAccess( "PER", oneOf=( "TE", (3,4), (5,6), (7,8) ) )
    provCode= ElementAccess( "PRV", 1 )
    qual= ElementAccess( "PRV", 2 )
    taxonomyCd= ElementAccess( "PRV", 3 )
    BCID= ElementAccess( "REF", 2, qualifier=(1,"1A") )
    BSID= ElementAccess( "REF", 2, qualifier=(1,"1B") )
    medID= ElementAccess( "REF", 2, qualifier=(1,"1C") )
    uPIN= ElementAccess( "REF", 2, qualifier=(1,"1G") )
    commID= ElementAccess( "REF", 2, qualifier=(1,"G2") )
    taxID_sy= ElementAccess( "REF", 2, qualifier=(1,"SY") )
    taxID_ei= ElementAccess( "REF", 2, qualifier=(1,"EI") )
    ITSSpec= ElementAccess( "REF", 2, qualifier=(1,"N5") )
    legacyID= ElementAccess( "REF", 2, qualifier=(1,"X5") )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Submitter( X12LoopBridge ):
    """Submitter Data derived from the 1000A loop."""
    loopName= "1000A"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    nm106= ElementAccess( "NM1", 6 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    id= ElementAccess( "NM1", 9 )
    email= ElementAccess( "PER", oneOf=( "EM", (3,4), (5,6), (7,8) ) )
    fax= ElementAccess( "PER", oneOf=( "FX", (3,4), (5,6), (7,8) ) )
    phone= ElementAccess( "PER", oneOf=( "TE", (3,4), (5,6), (7,8) ) )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Subscriber( X12LoopBridge ):
    """Subscriber Data from the 2000B loop."""
    loopName= "2000B"
    qualifier= ElementAccess( "NM1", 1 )
    entityType= ElementAccess( "NM1", 2 )
    last= ElementAccess( "NM1", 3 )
    first= ElementAccess( "NM1", 4 )
    mid= ElementAccess( "NM1", 5 )
    nm106= ElementAccess( "NM1", 6 )
    suffix= ElementAccess( "NM1", 7 )
    idQual= ElementAccess( "NM1", 8 )
    id= ElementAccess( "NM1", 9 )
    addr1= ElementAccess( "N3", 1 )
    addr2= ElementAccess( "N3", 2 )
    city= ElementAccess( "N4", 1 )
    state= ElementAccess( "N4", 2 )
    zip= ElementAccess( "N4", 3 )
    country= ElementAccess( "N4", 4 )
    payerResp= ElementAccess( "SBR", 1 )
    relCode= ElementAccess( "SBR", 2 )
    reference= ElementAccess( "SBR", 3 )
    name= ElementAccess( "SBR", 4 )
    insType= ElementAccess( "SBR", 5 )
    claimCode= ElementAccess( "SBR", 9 )
    rel= ElementAccess( "PAT", 1 )
    dateFormat= ElementAccess( "PAT", 5 )
    dod= ElementAccess( "PAT", 6 )
    measCode= ElementAccess( "PAT", 7 )
    weight= ElementAccess( "PAT", 8 )
    preg= ElementAccess( "PAT", 9 )
    dob= ElementAccess( "DMG", 2, x12type=D8 )
    gender= ElementAccess( "DMG", 3 )
    ssn= ElementAccess( "REF", 2, qualifier=(1,"SY") )
    def __str__( self ):
        return "%s, %s %s %s" % ( self.last, self.first, self.mid, self.suffix )

class Paperwork( X12SegmentBridge ):
    """Claim Supplemental Information, contained within ClaimDetails."""
    rptType= ElementAccess( "PWK", 1 )
    transCD= ElementAccess( "PWK", 2 )
    AttCtlQual= ElementAccess( "PWK", 6 )
    AttCtl= ElementAccess( "PWK", 7 )

class ClaimDetails( X12LoopBridge ):
    """Claim Details from the 2300 Loop."""
    loopName= "2300"
    patAcct= ElementAccess( "CLM", 1 )
    amount= ElementAccess( "CLM", 2 )
    serviceLoc= ElementAccess( "CLM", 5 )
    respCode1= ElementAccess( "CLM", 6 )
    medAssign= ElementAccess( "CLM", 7 )
    assignBenInd= ElementAccess( "CLM", 8 )
    release= ElementAccess( "CLM", 9 )
    signature= ElementAccess( "CLM", 10 )
    relCauses= ElementAccess( "CLM", 11 )
    progCode= ElementAccess( "CLM", 12 )
    provAgree= ElementAccess( "CLM", 16 )
    respCode2= ElementAccess( "CLM", 18 )
    delayCode= ElementAccess( "CLM", 20 )
    admsType= ElementAccess( "CL1", 1 )
    admsSrc= ElementAccess( "CL1", 2 )
    dischStat= ElementAccess( "CL1", 3 )
    coveredDays= ElementAccess( "QTY", 2, qualifier=(1,"CA") )
    coveredDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"CA") )
    nonCoveredDays= ElementAccess( "QTY", 2, qualifier=(1,"NA") )
    nonCoveredDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"NA") )
    coInsuranceDays= ElementAccess( "QTY", 2, qualifier=(1,"CD") )
    coInsuranceDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"CD") )
    reserveDays= ElementAccess( "QTY", 2, qualifier=(1,"LA") )
    reserveDays_UOM= ElementAccess( "QTY", 3, qualifier=(1,"LA") )
    origClaimNo= ElementAccess( "REF", 2, qualifier=(1,"F8") )
    medLRec= ElementAccess( "REF", 2, qualifier=(1,"EA") )
    microID= ElementAccess( "REF", 2, qualifier=(1,"D9") )
    paperwork= SegmentSequenceAccess( "PWK", x12type=SegmentConversion(Paperwork) )

class Institutional_ClaimDetails( ClaimDetails ):
    """Institutional Claim Details from the 2300 Loop."""
    fmt= ElementAccess( "DTP", 2 )
    stmtDts= ElementAccess( "DTP", 3, qualifier=(1,"434") )
    admsDt= ElementAccess( "DTP", 3, qualifier=(1,"435") )
    dischHr= ElementAccess( "DTP", 3, qualifier=(1,"096") )
    billNote= ElementAccess( "NTE", 2, qualifier=(1,"ADD") )
    # Non-"ADD" "NTE" segments are claim notes -- legacy uses an array of up to 10.
    # Only for institutional claims.
    claimNotes= ElementSequenceAccess( "NTE", 2, qualPos=1, notInList=("ADD",) )

    # DR Composite (Diagnosis Related Group (DRG) Information)
    drg= CompositeAccess( "HI", "DR", 1 )
    # BP/BR Composite (Principal Procedure Information)
    prinProcCode= CompositeAccess( "HI", ("BR","BP"), 1 )
    # BF Composite (Diagnosis) can have a number of attributes
    diagCode= CompositeSequenceAccess( "HI", "BF" )
    # BG Composite (Condition Information) can have a number of attributes
    condCode= CompositeSequenceAccess( "HI", "BG" )
    # BK Composite (Principal Diagnosis) is split into two attributes
    prinDiagCode= CompositeAccess( "HI", "BK", 1 )
    admitDiagCd= CompositeAccess( "HI", "BK", 2 )
    # BO/BQ Composite (Other Procedure Information) has a number of attributes
    procCode= CompositeSequenceAccess( "HI", ("BQ","BO") )
    # BH Composite (Occurrence Information) has a number of attributes
    occrCode= CompositeSequenceAccess( "HI", "BH" )
    # BE Composite (Value Information) has a number of attributes
    valueCode= CompositeSequenceAccess( "HI", "BE" )
    # BI Composite (Occurrence Span Information) is not used
    # TC Composite (Treatment Code Information) is not used

class Professional_ClaimDetails( ClaimDetails ):
    """Professional Claim Details from the 2300 Loop."""
    fmt= ElementAccess( "DTP", 2 )
    intDt= ElementAccess( "DTP", 3, qualifier=(1,"454") )
    accidentDt= ElementAccess( "DTP", 3, qualifier=(1,"439") )
    onsetDt= ElementAccess( "DTP", 3, qualifier=(1,"431") )
    lmpDt= ElementAccess( "DTP", 3, qualifier=(1,"484") )
    prescDt= ElementAccess( "DTP", 3, qualifier=(1,"471") )

    measCode= ElementAccess("CR1", 1)
    weight= ElementAccess("CR1", 2)
    ambTransCode= ElementAccess("CR1", 3)
    ambTransReason= ElementAccess("CR1", 4)
    ambTransQual= ElementAccess("CR1", 5)
    ambTransQty= ElementAccess("CR1", 6)
    ambDescript= ElementAccess("CR1", 9)
    ambDescript2= ElementAccess("CR1", 10)

    claimNotes= ElementSequenceAccess( "NTE", 2 )

    diagCode= ElementAccess( "HI", SequenceOf(1,8) )
    homeHealthCd= ElementAccess( "CR7", 1 )
    visitsRend= ElementAccess( "CR7", 2 )
    visitsProj= ElementAccess( "CR7", 3 )

    codeCat= ElementAccess("CRC", 1 )
    cond= ElementAccess("CRC", SequenceOf(2,6) )
    ref1Num= ElementAccess( "REF", 2, qualifier=(1,"9F") )
    preAuth= ElementAccess( "REF", 2, qualifier=(1,"G1") )

class ServiceLine( X12LoopBridge ):
    """Service Line from the 2400 Loop."""
    loopName= "2400"
    SrvLNo= ElementAccess( "LX", 1 )
    format= ElementAccess( "DTP", 2 )
    srvDT= ElementAccess( "DTP", 3, qualifier=(1,"472") )
    dmeCode= ElementAccess( "SV5", 1 )
    qualifier= ElementAccess( "SV5", 2 )
    amt1= ElementAccess( "SV5", 3 )
    amt2= ElementAccess( "SV5", 4 )
    amt3= ElementAccess( "SV5", 5 )
    amt4= ElementAccess( "SV5", 6 )

class Institutional_ServiceLine( ServiceLine ):
    """Institutional Service Line from the 2400 Loop."""
    revenueCode= ElementAccess( "SV2", 1 )
    procID= ElementAccess( "SV2", 2 )
    amt= ElementAccess( "SV2", 3 )
    unitsQual= ElementAccess( "SV2", 4 )
    units= ElementAccess( "SV2", 5 )
    unitRate= ElementAccess( "SV2", 6 )
    amtNotCovered= ElementAccess( "SV2", 7 )

class Professional_ServiceLine( ServiceLine ):
    """Professional Service Line from the 2400 Loop."""
    srvID= ElementAccess( "SV1", 1 )
    amt= ElementAccess( "SV1", 2 )
    unitsQual= ElementAccess( "SV1", 3 )
    units= ElementAccess( "SV1", 4 )
    facCode= ElementAccess( "SV1", 5 )
    diagCode= ElementAccess( "SV1", 7 )
    respCode1= ElementAccess( "SV1", 9 )
    respCode2= ElementAccess( "SV1", 11 )
    respCode3= ElementAccess( "SV1", 12 )
    coPay= ElementAccess( "SV1", 15 )

class ServiceLineAdj( X12LoopBridge ):
    """Service Line Adjustment from the 2430 Loop."""
    loopName= "2430"
    idCode= ElementAccess( "SVD", 1 )
    amt= ElementAccess( "SVD", 2 )
    procID= ElementAccess( "SVD", 3 )
    svcID= ElementAccess( "SVD", 4 )
    qty= ElementAccess( "SVD", 5 )
    assNo= ElementAccess( "SVD", 6 )
    format= ElementAccess( "DTP", 2 )
    srvDT= ElementAccess( "DTP", 3, qualifier=(1,"579") )

class Claim( object ):
    """A claim, built from an X12 :samp:`837` message.
    
    :ivar submitter: A sequence of :class:`Submitter` instances from the 1000A loop.
    :ivar provider: A sequence of :class:`Provider` instances from the 2000A loop.
    :ivar subscriber: A sequence of :class:`Subscriber` instances from the 2000B loop.
    :ivar patient: A sequence of :class:`Institutional_Inpatient` instances from the 2000C loop.
    """
    def loops( self, theClass, anX12Message ):
        return [ theClass(loop) for loop in anX12Message.descendant( "loop", theClass.loopName ) ]

    def __init__( self, anX12Message ):
        """Examine the message and extract the relevant Loops."""
        # XXX - determine 837P vs. 837I and Inpatient vs. Outpatient
        self.submitter= self.loops( Submitter, anX12Message )
        print( "Loop 1000A, Submitter", map( str, self.submitter ) )
        self.provider= self.loops( Provider, anX12Message )
        print( "Loop 2000A, Billing Provider", map( str, self.provider ) )
        self.subscriber= self.loops( Subscriber, anX12Message )
        print( "Loop 2000B, Subscriber", map( str, self.subscriber ) )
        self.patient= self.loops( Institutional_Inpatient, anX12Message )
        print( "Loop 2000C, Patient", map( str, self.patient ) )
        # Loop 2300 - Claim Details
        self.claimDetails= self.loops( Institutional_ClaimDetails, anX12Message )
        print( "Loop 2300, Claim Details", map( str, self.claimDetails ) )
        # Loop 2400 - Service Lines
