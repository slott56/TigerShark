from decimal import Decimal

from tigershark.facade import ElementAccess
from tigershark.facade import X12LoopBridge
from tigershark.facade import enum
from tigershark.facade import Money
from tigershark.facade.enums import claim_adjustment_reasons


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
