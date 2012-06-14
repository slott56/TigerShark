from decimal import Decimal

from tigershark.facade import ElementAccess
from tigershark.facade import Facade
from tigershark.facade import Money
from tigershark.facade import X12LoopBridge
from tigershark.facade import enum
from tigershark.facade.enums.common import id_code_qualifier
from tigershark.facade.enums.common import reference_id_qualifier
from tigershark.facade.enums.remittance import claim_adjustment_reasons


class ClaimAdjustment(X12LoopBridge):
    group = ElementAccess("CAS", 1, x12type=enum(
        {"CO": "Contractual Obligation",
         "CR": "Correction and/or reversal",
         "OA": "Other Adjustment",
         "PI": "Payor initiated adjustment",
         "PR": "Patient Responsibility"}))

    reason_1 = ElementAccess("CAS", 2,
            x12type=enum(claim_adjustment_reasons, raw_unknowns=True))
    amount_1 = ElementAccess("CAS", 3, x12type=Money)
    quantity_1 = ElementAccess("CAS", 4)

    reason_2 = ElementAccess("CAS", 5,
            x12type=enum(claim_adjustment_reasons, raw_unknowns=True))
    amount_2 = ElementAccess("CAS", 6, x12type=Money)
    quantity_2 = ElementAccess("CAS", 7)

    reason_3 = ElementAccess("CAS", 8,
            x12type=enum(claim_adjustment_reasons, raw_unknowns=True))
    amount_3 = ElementAccess("CAS", 9, x12type=Money)
    quantity_3 = ElementAccess("CAS", 10)

    reason_4 = ElementAccess("CAS", 11,
            x12type=enum(claim_adjustment_reasons, raw_unknowns=True))
    amount_4 = ElementAccess("CAS", 12, x12type=Money)
    quantity_4 = ElementAccess("CAS", 13)

    reason_5 = ElementAccess("CAS", 14,
            x12type=enum(claim_adjustment_reasons, raw_unknowns=True))
    amount_5 = ElementAccess("CAS", 15, x12type=Money)
    quantity_5 = ElementAccess("CAS", 16)

    reason_6 = ElementAccess("CAS", 17,
            x12type=enum(claim_adjustment_reasons, raw_unknowns=True))
    amount_6 = ElementAccess("CAS", 18, x12type=Money)
    quantity_6 = ElementAccess("CAS", 19)

    def total_amount(self, reason=None):
        s = Decimal('0.0')
        for i in range(1, 7):
            val = self.__getattribute__("amount_%s" % i)
            reason_tuple = self.__getattribute__("reason_%s" % i)
            if reason is None or (reason_tuple is not None and
                    reason_tuple[0] is not None and
                    reason_tuple[0] == reason):
                s += val
        return s

    def total_quantity(self, reason=None):
        s = 0.0
        for i in range(1, 7):
            a = self.__getattribute__("quantity_%s" % i)
            if a is not None:
                try:
                    s += float(a)
                except:
                    pass
        return s

    def all_reasons_iter(self):
        for i in range(1, 7):
            reason_tuple = self.__getattribute__("reason_%s" % i)
            if reason_tuple is not None:
                yield reason_tuple

    def __init__(self, aLoop, qualifier, *args, **kwargs):
        self.qualifier = qualifier
        super(ClaimAdjustment, self).__init__(aLoop, *args, **kwargs)


class ContactDetails(X12LoopBridge):
    name = ElementAccess("N1", 2)
    id_qualifier = ElementAccess("N1", 3, x12type=enum({
            "XV": "Health Care Financing Administration National Plan ID",
            "FI": "Federal Taxpayer Identification Number",
            "XX": "Health Care Financing Administration National Provider ID"
            }))
    id = ElementAccess("N1", 4)
    addr1 = ElementAccess("N3", 1)
    addr2 = ElementAccess("N3", 2)
    city = ElementAccess("N4", 1)
    state = ElementAccess("N4", 2)
    zip = ElementAccess("N4", 3)
    country_code = ElementAccess("N4", 4)
    location_type = ElementAccess("N4", 5, x12type=enum({
        "CY": "County/Parish",
        "FI": "Federal Information Processing Standards (FIPS) 55 (Named "
                "Populated Places)"}, raw_unknowns=True))
    location_id = ElementAccess("N4", 6)
    contact_code = ElementAccess("PER", 1, x12type=enum({
        "IC": "Information Contact"}, raw_unknowns=True))
    contact_name = ElementAccess("PER", 2)
    contact_edi = ElementAccess("PER", oneOf=("ED", (3, 4), (5, 6), (7, 8)))
    contact_email = ElementAccess("PER", oneOf=("EM", (3, 4), (5, 6), (7, 8)))
    contact_fax = ElementAccess("PER", oneOf=("FX", (3, 4), (5, 6), (7, 8)))
    contact_home_phone = ElementAccess("PER",
            oneOf=("HP", (3, 4), (5, 6), (7, 8)))
    contact_work_phone = ElementAccess("PER",
            oneOf=("WP", (3, 4), (5, 6), (7, 8)))
    contact_phone = ElementAccess("PER", oneOf=("TE", (3, 4), (5, 6), (7, 8)))
    contact_phone_ext = ElementAccess("PER",
            oneOf=("EX", (3, 4), (5, 6), (7, 8)))


class NamedEntity(X12LoopBridge):
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

    def is_person(self):
        return self.entity_type[0] == "1"

    def is_organization(self):
        return self.entity_type[0] == "2"

    def __init__(self, aLoop, qualifier=None, *args, **kwargs):
        if qualifier:
            self.qualifier = qualifier
        super(NamedEntity, self).__init__(aLoop)
        #NOTE: Sometimes this can be multiple Elements...
        self.contact_details = ContactDetails(aLoop, *args, **kwargs)


class ReferenceID(Facade, X12LoopBridge):
    reference_id_qualifier = ElementAccess("REF", 1,
            x12type=enum(reference_id_qualifier))
    reference_id = ElementAccess("REF", 2)
    description = ElementAccess("REF", 3)
