from tigershark.facade import CompositeAccess
from tigershark.facade import ElementAccess
from tigershark.facade import Facade
from tigershark.facade import SegmentAccess
from tigershark.facade import SegmentConversion
from tigershark.facade import SegmentSequenceAccess
from tigershark.facade import X12LoopBridge
from tigershark.facade import X12SegmentBridge
from tigershark.facade import enum
from tigershark.facade.enums.eligibility import coverage_level
from tigershark.facade.enums.eligibility import insurance_type
from tigershark.facade.enums.eligibility import service_type_codes
from tigershark.facade.f27x import Address
from tigershark.facade.f27x import ContactInformation
from tigershark.facade.f27x import DateOrTimePeriod
from tigershark.facade.f27x import DemographicInformation
from tigershark.facade.f27x import Diagnosis
from tigershark.facade.f27x import Hierarchy
from tigershark.facade.f27x import Header
from tigershark.facade.f27x import Location
from tigershark.facade.f27x import NamedEntity
from tigershark.facade.f27x import ProviderInformation
from tigershark.facade.f27x import ReferenceID
from tigershark.facade.f27x import Relationship
from tigershark.facade.f27x import TraceNumber
from tigershark.facade.utils import first


class Source(Facade, X12LoopBridge):
    """The information source is the entity with the eligibility answers"""
    loopName = "2000A"

    hierarchy = SegmentAccess("HL", x12type=SegmentConversion(Hierarchy))

    class _Information(X12LoopBridge):
        loopName = "2100A"

        name = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))

    def __init__(self, anX12Message, *args, **kwargs):
        super(Source, self).__init__(anX12Message, *args, **kwargs)
        self.source_information = first(self.loops(
            self._Information, anX12Message))
        self.receivers = self.loops(Receiver, anX12Message)


class Receiver(Facade, X12LoopBridge):
    """The entity asking the questions"""
    loopName = "2000B"

    hierarchy = SegmentAccess("HL", x12type=SegmentConversion(Hierarchy))

    class _Information(X12LoopBridge):
        loopName = "2100B"

        name = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))
        reference_ids = SegmentSequenceAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        address_street = SegmentAccess("N3",
                x12type=SegmentConversion(Address))
        address_location = SegmentAccess("N4",
                x12type=SegmentConversion(Location))
        contact_information = SegmentSequenceAccess("PER",
                x12type=SegmentConversion(ContactInformation))
        provider_information = SegmentAccess("PRV",
                x12type=SegmentConversion(ProviderInformation))

    def __init__(self, anX12Message, *args, **kwargs):
        super(Receiver, self).__init__(anX12Message, *args, **kwargs)
        self.receiver_information = first(self.loops(
            self._Information, anX12Message))
        self.subscribers = self.loops(Subscriber, anX12Message)


class EligibilityOrBenefitInquiry(X12SegmentBridge):
    service_type = ElementAccess("EQ", 1, x12type=enum(
        service_type_codes))
    ada_code = CompositeAccess("EQ", "AD", 2)
    cpt_code = CompositeAccess("EQ", "CJ", 2)
    hcpcs_code = CompositeAccess("EQ", "HC", 2)
    icd_9_cm_code = CompositeAccess("EQ", "ID", 2)
    hiec_code = CompositeAccess("EQ", "IV", 2)
    ndc_code = CompositeAccess("EQ", "ND", 2)
    zz_code = CompositeAccess("EQ", "ZZ", 2)
    coverage_level = ElementAccess("EQ", 3, x12type=enum(
        coverage_level))
    insurance_type = ElementAccess("EQ", 4, x12type=enum(
        insurance_type))


class MonetaryAmount(X12SegmentBridge):
    spend_down = ElementAccess("AMT", 2, qualifier=(1, "R"))


class Subscriber(Facade, X12LoopBridge):
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

    hierarchy = SegmentAccess("HL", x12type=SegmentConversion(Hierarchy))
    trace_numbers = SegmentSequenceAccess("TRN",
            x12type=SegmentConversion(TraceNumber))

    class _Information(X12LoopBridge):
        loopName = "2100C"

        name = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))
        reference_ids = SegmentSequenceAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        address_street = SegmentAccess("N3",
                x12type=SegmentConversion(Address))
        address_location = SegmentAccess("N4",
                x12type=SegmentConversion(Location))
        provider_information = SegmentAccess("PRV",
                x12type=SegmentConversion(ProviderInformation))
        demographic_information = SegmentAccess("DMG",
                x12type=SegmentConversion(DemographicInformation))
        relationship = SegmentAccess("INS",
                x12type=SegmentConversion(Relationship))
        dates = SegmentSequenceAccess("DTP",
                x12type=SegmentConversion(DateOrTimePeriod))

    class _EligibilityOrBenefitInformation(Facade, X12LoopBridge):
        loopName = "2110C"

        coverage_information = SegmentAccess("EQ",
                x12type=SegmentConversion(EligibilityOrBenefitInquiry))
        monetary_amount = SegmentAccess("AMT",
                x12type=SegmentConversion(MonetaryAmount))
        diagnoses = SegmentSequenceAccess("III",
                x12type=SegmentConversion(Diagnosis))
        prior_authorization_or_referral = SegmentAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        date = SegmentAccess("DTP",
                x12type=SegmentConversion(DateOrTimePeriod))

    def __init__(self, anX12Message, *args, **kwargs):
        super(Subscriber, self).__init__(anX12Message, *args, **kwargs)
        self.subscriber_information = first(self.loops(
            self._Information, anX12Message))
        self.eligibility_or_benefit_information = self.loops(
                self._EligibilityOrBenefitInformation, anX12Message)
        self.dependents = self.loops(Dependent, anX12Message)


class Dependent(Facade, X12LoopBridge):
    """A person identifiable only when associated with a subscriber.

    This person cannot be uniquely identified without the presence of a
    Subscriber. The Dependent isn't a direct member of Source.

    The Dependent is a sub-loop of the Subscriber."""
    loopName = "2000D"

    hierarchy = SegmentAccess("HL", x12type=SegmentConversion(Hierarchy))
    trace_numbers = SegmentSequenceAccess("TRN",
            x12type=SegmentConversion(TraceNumber))

    class _Information(X12LoopBridge):
        loopName = "2100D"

        name = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))
        reference_ids = SegmentSequenceAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        address_street = SegmentAccess("N3",
                x12type=SegmentConversion(Address))
        address_location = SegmentAccess("N4",
                x12type=SegmentConversion(Location))
        provider_information = SegmentAccess("PRV",
                x12type=SegmentConversion(ProviderInformation))
        demographic_information = SegmentAccess("DMG",
                x12type=SegmentConversion(DemographicInformation))
        relationship = SegmentAccess("INS",
                x12type=SegmentConversion(Relationship))
        dates = SegmentSequenceAccess("DTP",
                x12type=SegmentConversion(DateOrTimePeriod))

    class _EligibilityOrBenefitInformation(Facade, X12LoopBridge):
        loopName = "2110D"

        coverage_information = SegmentAccess("EQ",
                x12type=SegmentConversion(EligibilityOrBenefitInquiry))
        diagnoses = SegmentSequenceAccess("III",
                x12type=SegmentConversion(Diagnosis))
        prior_authorization_or_referral = SegmentAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        date = SegmentAccess("DTP",
                x12type=SegmentConversion(DateOrTimePeriod))

    def __init__(self, anX12Message, *args, **kwargs):
        super(Dependent, self).__init__(anX12Message, *args, **kwargs)
        self.dependent_information = first(self.loops(
            self._Information, anX12Message))
        self.eligibility_or_benefit_information = self.loops(
                self._EligibilityOrBenefitInformation, anX12Message)


class F270_4010(Facade):
    def __init__(self, anX12Message):
        st_loops = anX12Message.descendant('LOOP', name='ST_LOOP')
        if len(st_loops) > 0:
            self.facades = []
            for loop in st_loops:
                self.facades.append(F270_4010(loop))
        else:
            self.header = first(self.loops(Header, anX12Message))
            self.source = first(self.loops(Source, anX12Message))
