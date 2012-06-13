from tigershark.facade import ElementAccess
from tigershark.facade import X12LoopBridge
from tigershark.facade import enum
from tigershark.facade import D8
from tigershark.facade import DR
from tigershark.facade import TM
from tigershark.facade import boolean
from tigershark.facade.enums import date_or_time_qualifier


class Header(X12LoopBridge):
    loopName = "HEADER"

    class _HierarchicalTransaction(X12LoopBridge):
        """Use this to start the transaction set.

        This also indicates the sequence of hierarchical levels of information
        that will follow, though that information is not used at this time."""
        structure = ElementAccess("BHT", 1, x12type=enum(
            {"0022": "Information Source, Information Receiver, Subscriber, "
                "or Dependent."}, raw_unknowns=True))
        purpose = ElementAccess("BHT", 2, x12type=enum({
            "01": "Cancellation",
            "11": "Response",
            "13": "Request",
            "36": "Authority to Dedduct (Reply)"}, raw_unknowns=True))
        transaction_id = ElementAccess("BHT", 3)
        creation_date = ElementAccess("BHT", 4, x12type=D8)
        creation_time = ElementAccess("BHT", 5, x12type=TM)
        type = ElementAccess("BHT", 6, x12type=enum({
            "RT": "Spend Down",
            "RU": "Medical Services Reservation"}, raw_unknowns=True))

    def __init__(self, aLoop, *args, **kwargs):
        super(Header, self).__init__(aLoop, *args, **kwargs)
        self.hierarchical_transaction_info = self._HierarchicalTransaction(
                aLoop)


class HL(object):
    id = ElementAccess("HL", 1)
    parent_id = ElementAccess("HL", 2)
    level = ElementAccess("HL", 3, x12type=enum(
        {"20": "Information Source",
         "21": "Information Receiver",
         "22": "Subscriber",
            }))
    has_children = ElementAccess("HL", 4, x12type=boolean("1"))


class TraceNumber(X12LoopBridge):
    """ Uniquely identify this transaction set.

    Also aid in reassociating payments and remittances that have been
    separated.
    """
    trace_type = ElementAccess("TRN", 1, x12type=enum({
            "1": "Current Transaction Trace Numbers",
            "2": "Referenced Transaction Trace Numbers (Value from 270)"}))
    trace_number = ElementAccess("TRN", 2)
    entity_id = ElementAccess("TRN", 3)
    entity_additional_id = ElementAccess("TRN", 4)


class DemographicInformation(X12LoopBridge):
    birth_date = ElementAccess("DMG", 2, x12type=D8, qualifier=(1, "D8"))
    gender = ElementAccess("DMB", 3, x12type=enum({
        "F": "Female",
        "M": "Male",
        "U": "Unknown"}))


class Relationship(X12LoopBridge):
    is_insured = ElementAccess("INS", 1, x12type=boolean('Y'))
    relationship = ElementAccess("INS", 2, x12type=enum({
        "01": "Spouse",
        "18": "Self",
        "19": "Child",
        "34": "Other Adult"}))
    maintenance_type = ElementAccess("INS", 3, x12type=enum({
        "001": "Change"}, raw_unknowns=True))
    maintenance_reason = ElementAccess("INS", 4, x12type=enum({
        "25": "Cahnge in Identifying Data Elements"}, raw_unknowns=True))
    student_status = ElementAccess("INS", 9, x12type=enum({
        "F": "Full-time",
        "N": "Not a Student",
        "P": "Part-time"}))
    handicapped = ElementAccess("INS", 10, x12type=boolean("Y"))
    birth_sequence_number = ElementAccess("INS", 17)


class DateOrTimePeriod(X12LoopBridge):
    type = ElementAccess("DTP", 1, x12type=enum(date_or_time_qualifier))
    time = ElementAccess("DTP", 3, x12type=D8, qualifier=(2, "D8"))
    time_range = ElementAccess("DTP", 3, x12type=DR, qualifier=(2, "RD8"))


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
