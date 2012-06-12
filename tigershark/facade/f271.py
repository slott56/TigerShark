#from decimal import Decimal

from tigershark.facade import X12LoopBridge
from tigershark.facade import ElementAccess
#from tigershark.facade import ElementSequenceAccess
#from tigershark.facade import CompositeAccess
from tigershark.facade import D8
from tigershark.facade import TM
#from tigershark.facade import Money
from tigershark.facade import Facade
from tigershark.facade import enum
from tigershark.facade import boolean
from tigershark.facade.common import NamedEntity
from tigershark.facade.common import ReferenceID
from tigershark.facade.utils import first


class Header(X12LoopBridge):
    loopName = "HEADER"
    transaction_set_type = ElementAccess("ST", 1, x12type=enum(
        {"270": "270 Eligibility Inquiry",
         "271": "271 Eligibility Response"}))
    transaction_set_control_number = ElementAccess("ST", 2)

    class _HierarchicalTransaction(X12LoopBridge):
        """Use this to start the transaction set.

        This also indicates the sequence of hierarchical levels of information
        that will follow, though that information is not used at this time."""
        structure = ElementAccess("BHT", 1, x12type=enum(
            {"0022": "Information Source, Information Receiver, Subscriber, "
                "or Dependent."}, raw_unknowns=True))
        purpose = ElementAccess("BHT", 2, x12type=enum(
            {"11": "Response"}, raw_unknowns=True))
        transaction_id = ElementAccess("BHT", 3)
        creation_date = ElementAccess("BHT", 4, x12type=D8)
        createion_time = ElementAccess("BHT", 5, x12type=TM)
        type = ElementAccess("BHT", 6)


class _HL(object):
    id = ElementAccess("HL", 1)
    parent_id = ElementAccess("HL", 2)
    level = ElementAccess("HL", 3, x12type=enum(
        {"20": "Information Source",
         "21": "Information Receiver",
            }))
    has_children = ElementAccess("HL", 4, x12type=boolean("1"))


class Source(Facade, X12LoopBridge, _HL):
    """The information source is the entity with the eligibility answers"""
    loopName = "2000A"

    entity_identifier = ElementAccess("NM1", 1, x12type=enum({
            "QC": "Patient",
            "IL": "Insured",
            "2B": "Third-Party Administrator",
            "36": "Employer",
            "GP": "Gateway Provider",
            "P5": "Plan Sponsor",
            "PR": "Payer"}))

    class _NamedEntity(NamedEntity):
        loopName = "2100A"

    def __init__(self, anX12Message, *args, **kwargs):
        super(Source, self).__init__(anX12Message, *args, **kwargs)
        self.entity_details = first(self.loops(self._NamedEntity,
            anX12Message))
        self.receivers = self.loops(Receiver, anX12Message)


class Receiver(Facade, X12LoopBridge, _HL):
    """The entity asking the questions"""
    loopName = "2000B"

    class _NamedEntity(NamedEntity):
        loopName = "2100B"

    class _ReferenceID(ReferenceID):
        loopName = "2100B"

    class _ProviderInformation(X12LoopBridge):
        loopName = "2100B"

        provider_code = ElementAccess("PRV", 1, x12type=enum({
            "AD": "Admitting",
            "AT": "Attending",
            "BI": "Billing",
            "CO": "Consulting",
            "CV": "Covering",
            "H": "Hospital",
            "HH": "Home Health Care",
            "LA": "Laboratory",
            "OT": "Other Physician",
            "P1": "Pharmacist",
            "P2": "Pharmacy",
            "PC": "Primary Care Physician",
            "PE": "Performing",
            "R": "Rural Health Clinic",
            "RF": "Referring",
            "SB": "Submitting",
            "SK": "Skilled Nursing Facility",
            "SU": "Supervising"}))
        reference_id_qualifier = ElementAccess("PRV", 2, x12type=enum({
            "HPI": "National Prodiver ID / Healthcare Provider ID",
            "ZZ": "Mutually Defined"}, raw_unknowns=True))
        reference_id = ElementAccess("PRV", 3)

    def __init__(self, anX12Message, *args, **kwargs):
        self.reference_ids = self.loops(self._ReferenceID, anX12Message)
        self.entity_details = first(self.loops(self._NamedEntity,
            anX12Message))
        self.provider_information(self._ProviderInformation(anX12Message))


class Subscriber(X12LoopBridge):
    """The person uniquely identified by the Source.

    This person was identified as a member of the Source. Subscriber may or
    may not be the patient.

    NOTE: Patient

    The Patient may be the Subscriber or the Dependent. There are several ways
    of identifying which type the Patient is, but the two most common are:

        1. The Source assigns a unique ID number to each member of the
        Subscriber's family. In this case all dependents of a Subscriber are
        uniquely addressable by the Source, and are thus considered proper
        Subscribers, not Dependents.

        2. The Source only gives a unique ID number to the Subscriber, and all
        family members are identifiable only by giving the Subscriber's and the
        Dependent's information. In this case both the Subscriber and Dependent
        will be defined.
    """
    loopName = "2000C"


class Dependent(X12LoopBridge):
    """A person identifiable only when associated with a subscriber.

    This person cannot be uniquely identified without the presence of a
    Subscriber. The Dependent isn't a direct member of Source.

    The Dependent is a sub-loop of the Subscriber."""
    loopName = "2000D"


class EligibilityOrBenefitInformation(X12LoopBridge):
    """The information requested about the patient."""
    pass


class F271_4010(Facade):
    def __init__(self, anX12Message):
        st_loops = anX12Message.descendant('LOOP', name='ST_LOOP')
        if len(st_loops) > 0:
            self.facades = []
            for loop in st_loops:
                self.facades.append(F271_4010(loop))
        else:
            self.header = first(self.loops(Header, anX12Message))
            self.source = first(self.loops(Source, anX12Message))
            #self.receiver = first(self.loops(Receiver, anX12Message))
            #self.claims_overview = first(self.loops(ClaimsOverview,
            #    anX12Message))
            #self.claims = self.loops(Claim, anX12Message)
