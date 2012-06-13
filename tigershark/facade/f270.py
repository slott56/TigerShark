from tigershark.facade import X12LoopBridge
from tigershark.facade import CompositeAccess
from tigershark.facade import ElementAccess
from tigershark.facade import Facade
from tigershark.facade import enum
from tigershark.facade.common import NamedEntity
from tigershark.facade.common import ReferenceID
from tigershark.facade.utils import first
from tigershark.facade.f27x import DateOrTimePeriod
from tigershark.facade.f27x import DemographicInformation
from tigershark.facade.f27x import Diagnosis
from tigershark.facade.f27x import Header
from tigershark.facade.f27x import HL
from tigershark.facade.f27x import MonetaryAmounts
from tigershark.facade.f27x import TraceNumber
from tigershark.facade.f27x import Relationship
from tigershark.facade.enums import eligibility_coverage_level
from tigershark.facade.enums import eligibility_insurance_type
from tigershark.facade.enums import eligibility_service_type_codes


class Source(Facade, X12LoopBridge, HL):
    """The information source is the entity with the eligibility answers"""
    loopName = "2000A"

    class _NamedEntity(NamedEntity):
        loopName = "2100A"

    def __init__(self, anX12Message, *args, **kwargs):
        super(Source, self).__init__(anX12Message, *args, **kwargs)
        self.entity_details = first(self.loops(self._NamedEntity,
            anX12Message))
        self.receivers = self.loops(Receiver, anX12Message)


class ProviderInformation(X12LoopBridge):
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
        "9K": "Servicer",
        "D3": "National Association of Boards of Pharmacy Number",
        "EI": "Employer's Identification Number",
        "HPI": "Healthcare Financing Administration National Provider ID",
        "SY": "Social Security Number",
        "TJ": "Federal Taxpayer's Identification Number",
        "ZZ": "Mutually Defined"}, raw_unknowns=True))
    reference_id = ElementAccess("PRV", 3)


class Receiver(Facade, X12LoopBridge, HL):
    """The entity asking the questions"""
    loopName = "2000B"

    class _NamedEntity(NamedEntity):
        loopName = "2100B"

    class _ReferenceID(ReferenceID):
        loopName = "2100B"

    class _ProviderInformation(ProviderInformation):
        loopName = "2100B"

    def __init__(self, anX12Message, *args, **kwargs):
        super(Receiver, self).__init__(anX12Message, *args, **kwargs)
        self.reference_ids = self.loops(self._ReferenceID, anX12Message)
        self.entity_details = first(self.loops(self._NamedEntity,
            anX12Message))
        self.provider_information = self._ProviderInformation(anX12Message)
        self.subscribers = self.loops(Subscriber, anX12Message)


class EligibilityOrBenefitInquiry(X12LoopBridge):
    service_type = ElementAccess("EQ", 1, x12type=enum(
        eligibility_service_type_codes))
    ada_code = CompositeAccess("EQ", "AD", 2)
    cpt_code = CompositeAccess("EQ", "CJ", 2)
    hcpcs_code = CompositeAccess("EQ", "HC", 2)
    icd_9_cm_code = CompositeAccess("EQ", "ID", 2)
    hiec_code = CompositeAccess("EQ", "IV", 2)
    ndc_code = CompositeAccess("EQ", "ND", 2)
    zz_code = CompositeAccess("EQ", "ZZ", 2)
    coverage_level = ElementAccess("EQ", 3, x12type=enum(
        eligibility_coverage_level))
    insurance_type = ElementAccess("EQ", 4, x12type=enum(
        eligibility_insurance_type))


class Subscriber(Facade, X12LoopBridge, HL):
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

    class _TraceNumber(TraceNumber):
        loopName = "2100C"

    class _NamedEntity(NamedEntity):
        loopName = "2100C"

    class _ReferenceID(ReferenceID):
        loopName = "2100C"

    class _ProviderInformation(ReferenceID):
        loopName = "2100C"

    class _DemographicInformation(DemographicInformation):
        loopName = "2100C"

    class _Relationship(Relationship):
        loopName = "2100C"

    class _DateOrTimePeriod(DateOrTimePeriod):
        loopName = "2100C"

    class _AdditionalInformation(Facade, X12LoopBridge):
        loopName = "2110C"

        class _EligibilityOrBenefitInquiry(EligibilityOrBenefitInquiry):
            loopName = "2110C"

        class _Diagnosis(Diagnosis):
            loopName = "2110C"

        def __init__(self, anX12Message, *args, **kwargs):
            super(Subscriber._AdditionalInformation, self).__init__(
                    anX12Message, *args, **kwargs)
            self.eligibility_or_benefit_inquiry = \
                    self._EligibilityOrBenefitInquiry(anX12Message)
            self.spend_amount = MonetaryAmounts(anX12Message)
            self.diagnoses = self.loops(self._Diagnosis, anX12Message)
            self.prior_authorization_or_referral = ReferenceID(anX12Message)
            self.date = DateOrTimePeriod(anX12Message)

    def __init__(self, anX12Message, *args, **kwargs):
        super(Subscriber, self).__init__(anX12Message, *args, **kwargs)
        self.trace_numbers = self.loops(self._TraceNumber, anX12Message)
        self.entity_details = first(self.loops(self._NamedEntity,
            anX12Message))
        self.reference_ids = self.loops(self._ReferenceID, anX12Message)
        self.provider_information = self._ProviderInformation(anX12Message)
        self.demographic_information = self._DemographicInformation(
                anX12Message)
        self.relationship = self._Relationship(anX12Message)
        self.dates = self.loops(self._DateOrTimePeriod, anX12Message)
        self.additional_information = self.loops(self._AdditionalInformation,
                anX12Message)
        self.dependents = self.loops(Dependent, anX12Message)


class Dependent(Facade, X12LoopBridge, HL):
    """A person identifiable only when associated with a subscriber.

    This person cannot be uniquely identified without the presence of a
    Subscriber. The Dependent isn't a direct member of Source.

    The Dependent is a sub-loop of the Subscriber."""
    loopName = "2000D"

    class _TraceNumber(TraceNumber):
        loopName = "2100D"

    class _NamedEntity(NamedEntity):
        loopName = "2100D"

    class _ReferenceID(ReferenceID):
        loopName = "2100D"

    class _ProviderInformation(ReferenceID):
        loopName = "2100D"

    class _DemographicInformation(DemographicInformation):
        loopName = "2100D"

    class _Relationship(Relationship):
        loopName = "2100D"

    class _DateOrTimePeriod(DateOrTimePeriod):
        loopName = "2100D"

    class _AdditionalInformation(Facade, X12LoopBridge):
        loopName = "2110D"

        class _EligibilityOrBenefitInquiry(EligibilityOrBenefitInquiry):
            loopName = "2110C"

        class _Diagnosis(Diagnosis):
            loopName = "2110C"

        def __init__(self, anX12Message, *args, **kwargs):
            super(Subscriber._AdditionalInformation, self).__init__(
                    anX12Message, *args, **kwargs)
            self.eligibility_or_benefit_inquiry = \
                    self._EligibilityOrBenefitInquiry(anX12Message)
            self.diagnoses = self.loops(self._Diagnosis, anX12Message)
            self.prior_authorization_or_referral = ReferenceID(anX12Message)
            self.date = DateOrTimePeriod(anX12Message)

    def __init__(self, anX12Message, *args, **kwargs):
        super(Dependent, self).__init__(anX12Message, *args, **kwargs)
        self.trace_numbers = self.loops(self._TraceNumber, anX12Message)
        self.entity_details = first(self.loops(self._NamedEntity,
                anX12Message))
        self.reference_ids = self.loops(self._ReferenceID, anX12Message)
        self.provider_information = self._ProviderInformation(anX12Message)
        self.demographic_information = self._DemographicInformation(
                anX12Message)
        self.relationship = self._Relationship(anX12Message)
        self.dates = self.loops(self._DateOrTimePeriod, anX12Message)
        self.additional_information = self.loops(self._AdditionalInformation,
                anX12Message)


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
            #self.receiver = first(self.loops(Receiver, anX12Message))
            #self.claims_overview = first(self.loops(ClaimsOverview,
            #    anX12Message))
            #self.claims = self.loops(Claim, anX12Message)
