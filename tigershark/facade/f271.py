from tigershark.facade import X12LoopBridge
from tigershark.facade import X12SegmentBridge
from tigershark.facade import ElementAccess
from tigershark.facade import SegmentAccess
from tigershark.facade import ElementSequenceAccess
from tigershark.facade import SegmentSequenceAccess
from tigershark.facade import SegmentConversion
from tigershark.facade import CompositeAccess
#from tigershark.facade import D8
#from tigershark.facade import DR
#from tigershark.facade import TM
#from tigershark.facade import Money
from tigershark.facade import Facade
from tigershark.facade import enum
from tigershark.facade import boolean
from tigershark.facade import Money
#from tigershark.facade.common import NamedEntity
#from tigershark.facade.common import ReferenceID
#from tigershark.facade.enums import service_type_codes
from tigershark.facade.utils import first
from tigershark.facade.f27x import ContactInformation
from tigershark.facade.f27x import Address
from tigershark.facade.f27x import Location
from tigershark.facade.f27x import DateOrTimePeriod
from tigershark.facade.f27x import DemographicInformation
from tigershark.facade.f27x import Diagnosis
from tigershark.facade.f27x import Header
from tigershark.facade.f27x import HL
from tigershark.facade.f27x import TraceNumber
from tigershark.facade.f27x import Relationship
from tigershark.facade.enums import delivery_or_calendar_pattern_code
from tigershark.facade.enums import delivery_time_pattern_code
from tigershark.facade.enums import eligibility_coverage_level
from tigershark.facade.enums import eligibility_insurance_type
from tigershark.facade.enums import eligibility_reject_reason_code
from tigershark.facade.enums import eligibility_service_type_codes
from tigershark.facade.enums import quantity_qualifier
from tigershark.facade.enums import reference_id_qualifier
from tigershark.facade.enums import id_code_qualifier
from tigershark.facade.enums import time_period_qualifier


class RequestValidation(X12SegmentBridge):
    valid_request = ElementAccess("AAA", 1, x12type=boolean("Y"))
    reject_reason = ElementAccess("AAA", 3,
            x12type=enum(eligibility_reject_reason_code))
    follow_up_action_code = ElementAccess("AAA", 4, x12type=enum({
        "C": "Please Correct and Resubmit",
        "N": "Resubmission Not Allowed",
        "P": "Please Resubmit Original Transaction",
        "R": "Resubmission Allowed",
        "S": "Do Not Resubmit; Inquiry Initiated to a Third Party",
        "W": "Please Wait 30 Days and Resubmit",
        "X": "Please Wait 10 Days and Resubmit",
        "Y": "Do Not Resubmit; We Will Hold Your Request and Respond Again "
                "Shortly"}))


class NamedEntity(X12SegmentBridge):
    entity_identifier = ElementAccess("NM1", 1, x12type=enum({
            "03": "Dependent",
            "1P": "Provider",
            "2B": "Third-Party Administrator",
            "36": "Employer",
            "80": "Hospital",
            "FA": "Facility",
            "GP": "Gateway Provider",
            "IL": "Insured",
            "P5": "Plan Sponsor",
            "PR": "Payer",
            "QC": "Patient"}))
    entity_type = ElementAccess("NM1", 2, x12type=enum({
            "1": "Person",
            "2": "Non-Person Entity"}))

    last_name = ElementAccess("NM1", 3)
    org_name = ElementAccess("NM1", 3)
    first_name = ElementAccess("NM1", 4)
    middle_initial = ElementAccess("NM1", 5)
    suffix = ElementAccess("NM1", 7)

    id_code = ElementAccess("NM1", 9)
    id_code_qual = ElementAccess("NM1", 8, x12type=enum(id_code_qualifier))

    @property
    def is_person(self):
        return self.entity_type[0] == "1"

    @property
    def is_organization(self):
        return self.entity_type[0] == "2"


class ReferenceID(X12SegmentBridge):
    reference_id_qualifier = ElementAccess("REF", 1,
            x12type=enum(reference_id_qualifier))
    reference_id = ElementAccess("REF", 2)
    description = ElementAccess("REF", 3)


class Source(Facade, X12LoopBridge, HL):
    """The information source is the entity with the eligibility answers"""
    loopName = "2000A"

    request_validations = SegmentSequenceAccess("AAA",
            x12type=SegmentConversion(RequestValidation))

    class _Information(X12LoopBridge):
        loopName = "2100A"
        name = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))
        contact_information = SegmentSequenceAccess("PER",
                x12type=SegmentConversion(ContactInformation))
        reference_ids = SegmentSequenceAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        request_validations = SegmentSequenceAccess("AAA",
                x12type=SegmentConversion(RequestValidation))

    def __init__(self, anX12Message, *args, **kwargs):
        super(Source, self).__init__(anX12Message, *args, **kwargs)
        self.source_information = first(self.loops(
            self._Information, anX12Message))
        self.receivers = self.loops(Receiver, anX12Message)


class Receiver(Facade, X12LoopBridge, HL):
    """The entity asking the questions"""
    loopName = "2000B"

    class _Information(X12LoopBridge):
        loopName = "2100B"
        name = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))
        contact_information = SegmentSequenceAccess("PER",
                x12type=SegmentConversion(ContactInformation))
        reference_ids = SegmentSequenceAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        request_validations = SegmentSequenceAccess("AAA",
                x12type=SegmentConversion(RequestValidation))

    def __init__(self, anX12Message, *args, **kwargs):
        super(Receiver, self).__init__(anX12Message, *args, **kwargs)
        self.receiver_information = first(self.loops(
            self._Information, anX12Message))
        self.subscribers = self.loops(Subscriber, anX12Message)


class EligibilityOrBenefitInformation(X12SegmentBridge):
    """Eligibility Information."""
    information_type = ElementAccess("EB", 1, x12type=enum({
        "1": "Active Coverage",
        "2": "Active - Full Risk Capitation",
        "3": "Active - Services Capitated",
        "4": "Active - Services Capitated to Primary Care Physician",
        "5": "Active - Pending Investigation",
        "6": "Inactive",
        "7": "Inactive - Pending Eligibility Update",
        "8": "Inactive - Pending Investigation",
        "A": "Co-Insurance",
        "B": "Co-Payment",
        "C": "Deductible",
        "CB": "Coverage Basis",
        "D": "Benefit Description",
        "E": "Exclusions",
        "F": "Limitations",
        "G": "Out of Pocket (Stop Loss)",
        "H": "Unlimited",
        "I": "Non-Covered",
        "J": "Cost Containment",
        "K": "Reserve",
        "L": "Primary Care Provider",
        "M": "Pre-existing Condition",
        "MC": "Managed Care Coordinator",
        "N": "Services Restricted to Following Provider",
        "O": "Not Deemed a Medical Necessity",
        "P": "Benefit Disclaimer",
        "Q": "Second Surgical Opinion Required",
        "R": "Other or Additional Payor",
        "S": "Prior Year(s) History",
        "T": "Card(s) Reported Lost/Stolen",
        "U": "Contact Following Entity for Eligibility or Benefit Information",
        "V": "Cannot Process",
        "W": "Other Source of Data",
        "X": "Health Care Facility",
        "Y": "Spend Down"}))
    coverage_level = ElementAccess("EB", 2, x12type=enum(
        eligibility_coverage_level))
    service_type = ElementAccess("EB", 3, x12type=enum(
        eligibility_service_type_codes))
    insurance_type = ElementAccess("EB", 4, x12type=enum(
        eligibility_insurance_type))
    description = ElementAccess("EB", 5)
    time_period_type = ElementAccess("EB", 6,
            x12type=enum(time_period_qualifier))
    benefit_amount = ElementAccess("EB", 7, x12type=Money)
    benefit_percent = ElementAccess("EB", 8)
    quantity_type = ElementAccess("EB", 9, x12type=enum(quantity_qualifier))
    quantity = ElementAccess("EB", 10)
    authorization_or_certification = ElementAccess("EB", 11,
            x12type=boolean("Y"))
    in_plan_network = ElementAccess("EB", 12, x12type=boolean("Y"))
    ada_code = CompositeAccess("EB", "AD", 13)
    cpt_code = CompositeAccess("EB", "CJ", 13)
    hcpcs_code = CompositeAccess("EB", "HC", 13)
    icd_9_cm_code = CompositeAccess("EB", "ID", 13)
    ndc_code = CompositeAccess("EB", "ND", 13)
    zz_code = CompositeAccess("EB", "ZZ", 13)


class HealthCareServicesDelivery(X12LoopBridge):
    benefit_quantity_type = ElementAccess("HSD", 1,
            x12type=enum(quantity_qualifier))
    benefit_quantity = ElementAccess("HSD", 2)
    unit_or_basis_for_measurement = ElementAccess("HSD", 3, x12type=enum({
        "DA": "Days",
        "MO": "Months",
        "VS": "Visit",
        "WK": "Week",
        "YR": "Years"}))
    sample_selection_modulus = ElementAccess("HSD", 4)
    time_period_type = ElementAccess("HSD", 5,
            x12type=enum(time_period_qualifier))
    period_count = ElementAccess("HSD", 6)
    delivery_frequency = ElementAccess("HSD", 7,
            x12type=enum(delivery_or_calendar_pattern_code))
    delivery_time = ElementAccess("HSD", 8,
            x12type=enum(delivery_time_pattern_code))


class Message(X12LoopBridge):
    message_text = ElementAccess("MSG", 1)


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

    trace_numbers = SegmentSequenceAccess("TRN",
            x12type=SegmentConversion(TraceNumber))

    class _Information(X12LoopBridge):
        loopName = "2100C"
        name = SegmentAccess("NM1",
                x12type=SegmentConversion(NamedEntity))
        address_street = SegmentAccess("N3",
                x12type=SegmentConversion(Address))
        address_location = SegmentAccess("N4",
                x12type=SegmentConversion(Location))
        reference_ids = SegmentSequenceAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        contact_information = SegmentSequenceAccess("PER",
                x12type=SegmentConversion(ContactInformation))

        request_validations = SegmentSequenceAccess("AAA",
                x12type=SegmentConversion(RequestValidation))
        demographic_information = SegmentAccess("DMG",
                x12type=SegmentConversion(DemographicInformation))
        relationship = SegmentAccess("INS",
                x12type=SegmentConversion(Relationship))
        dates = SegmentSequenceAccess("DTP",
                x12type=SegmentConversion(DateOrTimePeriod))

    class _EligibilityOrBenefitInformation(Facade, X12LoopBridge):
        loopName = "2110C"

        coverage_information = SegmentAccess("EB",
                x12type=SegmentConversion(EligibilityOrBenefitInformation))
        services_deliveries = SegmentSequenceAccess("HSD",
                x12type=SegmentConversion(HealthCareServicesDelivery))
        reference_ids = SegmentSequenceAccess("REF",
                x12type=SegmentConversion(ReferenceID))
        dates = SegmentSequenceAccess("DTP",
                x12type=SegmentConversion(DateOrTimePeriod))
        request_validations = SegmentSequenceAccess("AAA",
                x12type=SegmentConversion(RequestValidation))
        messages = ElementSequenceAccess("MSG", 1)

        class _AdditionalInformation(X12LoopBridge):
            loopName = "2115C"

            diagnosis = SegmentAccess("III",
                x12type=SegmentConversion(Diagnosis))

        def __init__(self, anX12Message, *args, **kwargs):
            super(Subscriber._EligibilityOrBenefitInformation, self).__init__(
                    anX12Message, *args, **kwargs)

            self.additional_information = self.loops(
                    self._AdditionalInformation, anX12Message)

    def __init__(self, anX12Message, *args, **kwargs):
        super(Subscriber, self).__init__(anX12Message, *args, **kwargs)
        self.subscriber_information = first(self.loops(
            self._Information, anX12Message))
        self.eligibility_or_benefit_information = \
                self.loops(self._EligibilityOrBenefitInformation, anX12Message)
        self.dependents = self.loops(Dependent, anX12Message)


class Dependent():
    loopName = "2000D"
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
