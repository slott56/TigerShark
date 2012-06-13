#from decimal import Decimal

from tigershark.facade import X12LoopBridge
from tigershark.facade import ElementAccess
#from tigershark.facade import ElementSequenceAccess
from tigershark.facade import CompositeAccess
from tigershark.facade import D8
from tigershark.facade import DR
from tigershark.facade import TM
#from tigershark.facade import Money
from tigershark.facade import Facade
from tigershark.facade import enum
from tigershark.facade import boolean
from tigershark.facade.common import NamedEntity
from tigershark.facade.common import ReferenceID
from tigershark.facade.enums import service_type_codes
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
        creation_time = ElementAccess("BHT", 5, x12type=TM)
        type = ElementAccess("BHT", 6)

    def __init__(self, aLoop, *args, **kwargs):
        super(Header, self).__init__(aLoop, *args, **kwargs)
        self.hierarchical_transaction_info = self._HierarchicalTransaction(
                aLoop)


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


class Receiver(Facade, X12LoopBridge, _HL):
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


class TraceNumber(X12LoopBridge):
    """ Uniquely identify this transaction set.

    Also aid in reassociating payments and remittances that have been
    separated.
    """
    trace_type = ElementAccess("TRN", 1, x12type=enum({
            "1": "Current Transaction Trace Numbers"}))
    trace_number = ElementAccess("TRN", 2)
    entity_id = ElementAccess("TRN", 3)
    entity_additional_id = ElementAccess("TRN", 4)


class DemographicInformation(X12LoopBridge):
    birth_date = ElementAccess("DMG", 2, x12type=D8, qualifier=(1, "D8"))
    gender = ElementAccess("DMB", 3, x12type=enum({
        "F": "Female",
        "M": "Male"}))


class Relationship(X12LoopBridge):
    is_insured = ElementAccess("INS", 1, x12type=boolean('Y'))
    relationship = ElementAccess("INS", 2, x12type=enum({
        "01": "Spouse",
        "18": "Self",
        "19": "Child",
        "34": "Other Adult"}))
    birth_sequence_number = ElementAccess("INS", 17)


class DateOrTimePeriod(X12LoopBridge):
    type = ElementAccess("DTP", 1, x12type=enum({
        "102": "Issue",
        "307": "Eligibility",
        "435": "Admission",
        "472": "Service"}))
    time = ElementAccess("DTP", 3, x12type=D8, qualifier=(2, "D8"))
    time_range = ElementAccess("DTP", 3, x12type=DR, qualifier=(2, "RD8"))


class EligibilityOrBenefitInformation(X12LoopBridge):
    service_type = ElementAccess("EQ", 1, x12type=enum(service_type_codes))
    ada_code = CompositeAccess("EQ", "AD", 2)
    cpt_code = CompositeAccess("EQ", "CJ", 2)
    hcpcs_code = CompositeAccess("EQ", "HC", 2)
    icd_9_cm_code = CompositeAccess("EQ", "ID", 2)
    hiec_code = CompositeAccess("EQ", "IV", 2)
    ndc_code = CompositeAccess("EQ", "ND", 2)
    zz_code = CompositeAccess("EQ", "ZZ", 2)
    coverage_level = ElementAccess("EQ", 3, x12type=enum({
        "CHD": "Children Only",
        "DEP": "Dependents Only",
        "ECH": "Employee and Children",
        "EMP": "Employee Only",
        "ESP": "Employee and Spouse",
        "FAM": "Family",
        "IND": "Individual",
        "SPC": "Spouse and Children",
        "SPO": "Spouse Only"}))
    insurance_type = ElementAccess("EQ", 4, x12type=enum({
        "AP": "Auto Insurance Policy",
        "C1": "Commercial",
        "CO": "Consolidated Omnibus Budget Reconciliation Act (COBRA)",
        "GP": "Group Policy",
        "HM": "Health Maintenance Organization (HMO)",
        "HN": "Health Maintenance Organization (HMO) - Medicare Risk",
        "IP": "Individual Policy",
        "MA": "Medicare Part A",
        "MB": "Medicare Part B",
        "MC": "Medicaid",
        "PR": "Preferred Provider Organization (PPO)",
        "PS": "Point of Service (POS)",
        "SP": "Supplemental Policy",
        "WC": "Workers Compenstation"}))


class MonetaryAmounts(X12LoopBridge):
    spend_down = ElementAccess("AMT", 2, qualifier=(1, "R"))


class Diagnosis(X12LoopBridge):
    principal_diagnosis_icd9_code = ElementAccess("III", 2,
            qualifier=(1, "BK"))
    diagnosis_icd9_code = ElementAccess("III", 2, qualifier=(1, "BF"))
    other_code = ElementAccess("III", 2, qualifier=(1, "ZZ"), x12type=enum({
        "11": "Office",
        "12": "Home",
        "21": "Inpatient Hospital",
        "22": "Outpatient Hospital",
        "23": "Emergency Room - Hospital",
        "24": "Ambulatory Surgical Center",
        "25": "Birthing Center",
        "26": "Military Treatment Facility",
        "31": "Skilled Nursing Facility",
        "32": "Nursing Facility",
        "33": "Custodial Care Facility",
        "34": "Hospice",
        "41": "Ambulance - Land",
        "42": "Ambulance - Air or Water",
        "50": "Federally Qualified Health Center",
        "51": "Inpatient Psychiatric Facility",
        "52": "Psychiatric Facility Partial Hospitalization",
        "53": "Community Mental Health Center",
        "54": "Intermediate Care Facility/Mentally Retarded",
        "55": "Residential Substance Abuse Treatment Facility",
        "56": "Psychiatric Residential Treatment Center",
        "60": "Mass Immunization Center",
        "61": "Comprehensive Inpatient Rehabilitation Facility",
        "62": "Comprehensive Outpatient Rehabilitation Facility",
        "65": "End-Stage Renal Disease Treatment Facility",
        "71": "State or Local Public Health Clinic",
        "72": "Rural Health Clinic",
        "81": "Independent Laboratory 99 Other Unlisted Facility"},
        raw_unknowns=True))


class Subscriber(Facade, X12LoopBridge, _HL):
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

        def __init__(self, anX12Message, *args, **kwargs):
            super(Subscriber._AdditionalInformation, self).__init__(
                    anX12Message, *args, **kwargs)
            self.eligibilit_or_benefit_information = \
                    EligibilityOrBenefitInformation(anX12Message)
            self.spend_amounts = self.loops(MonetaryAmounts,
                    anX12Message)
            self.diagnoses = self.loops(Diagnosis, anX12Message)
            self.prior_authorization = ReferenceID(anX12Message)
            self.dates = self.loops(DateOrTimePeriod, anX12Message)

    def __init__(self, anX12Message, *args, **kwargs):
        super(Subscriber, self).__init__(anX12Message, *args, **kwargs)
        self.trace_number = TraceNumber(
                anX12Message, *args, **kwargs)
        self.entity_details = first(self.loops(self._NamedEntity,
            anX12Message))
        self.reference_ids = self.loops(self._ReferenceID, anX12Message)
        self.provider_information = self._ProviderInformation(anX12Message)
        self.demographic_information = self._DemographicInformation(
                anX12Message)
        self.relationship = self._Relationship(anX12Message)
        self.date = self._DateOrTimePeriod(anX12Message)
        self.additional_information = self.loops(self._AdditionalInformation,
                anX12Message)
        self.dependents = self.loops(Dependent, anX12Message)


class Dependent(Facade, X12LoopBridge, _HL):
    """A person identifiable only when associated with a subscriber.

    This person cannot be uniquely identified without the presence of a
    Subscriber. The Dependent isn't a direct member of Source.

    The Dependent is a sub-loop of the Subscriber."""
    loopName = "2000D"

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

        def __init__(self, anX12Message, *args, **kwargs):
            super(Subscriber._AdditionalInformation, self).__init__(
                    anX12Message, *args, **kwargs)
            self.eligibilit_or_benefit_information = \
                    EligibilityOrBenefitInformation(anX12Message)
            self.spend_amounts = self.loops(MonetaryAmounts,
                    anX12Message)
            self.diagnoses = self.loops(Diagnosis, anX12Message)
            self.prior_authorization = ReferenceID(anX12Message)
            self.dates = self.loops(DateOrTimePeriod, anX12Message)

    def __init__(self, anX12Message, *args, **kwargs):
        super(Dependent, self).__init__(anX12Message, *args, **kwargs)
        self.trace_number = TraceNumber(
                anX12Message, *args, **kwargs)
        self.entity_details = first(self.loops(self._NamedEntity,
            anX12Message))
        self.reference_ids = self.loops(self._ReferenceID, anX12Message)
        self.provider_information = self._ProviderInformation(anX12Message)
        self.demographic_information = self._DemographicInformation(
                anX12Message)
        self.relationship = self._Relationship(anX12Message)
        self.date = self._DateOrTimePeriod(anX12Message)
        self.additional_information = self.loops(self._AdditionalInformation,
                anX12Message)


class EligibilityOrBenefitInformation(X12LoopBridge):
    """The information requested about the patient."""
    pass


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
