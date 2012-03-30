from facade import X12LoopBridge
#from facade import X12SegmentBridge
from facade import ElementAccess
#from facade import SegmentSequenceAccess
#from facade import SegmentConversion
#from facade import SequenceOf
#from facade import ElementSequenceAccess
#from facade import CompositeAccess
#from facade import CompositeSequenceAccess
from facade import D8


class F835_4010(object):
    class _Payer(X12LoopBridge):
        """Payer information from the 1000A loop."""
        loopName = "1000A"
        name = ElementAccess("N1", 2)
        qualifier = ElementAccess("NM1", 3)
        id = ElementAccess("NM1", 4)
        addr1 = ElementAccess("N3", 1)
        addr2 = ElementAccess("N3", 2)
        city = ElementAccess("N4", 1)
        state = ElementAccess("N4", 2)
        zip = ElementAccess("N4", 3)
        payer_id = ElementAccess("REF", 2, qualifier=(1, "2U"))
        submitter_id = ElementAccess("REF", 2, qualifier=(1, "EO"))
        # health industry number
        hin = ElementAccess("REF", 2, qualifier=(1, "HI"))
        naic_code = ElementAccess("REF", 2, qualifier=(1, "NF"))
        email = ElementAccess("PER", oneOf=("EM", (3, 4), (5, 6), (7, 8)))
        fax = ElementAccess("PER", oneOf=("FX", (3, 4), (5, 6), (7, 8)))
        phone = ElementAccess("PER", oneOf=("TE", (3, 4), (5, 6), (7, 8)))

        def __str__(self):
            return "%s, %s %s %s" % (self.last, self.first, self.mid,
                    self.suffix)

    class _Payee(X12LoopBridge):
        """Payee information from 1000B loop."""
        loopName = "1000B"
        name = ElementAccess("N1", 2)
        qualifier = ElementAccess("NM1", 3)
        id = ElementAccess("NM1", 4)
        addr1 = ElementAccess("N3", 1)
        addr2 = ElementAccess("N3", 2)
        city = ElementAccess("N4", 1)
        state = ElementAccess("N4", 2)
        zip = ElementAccess("N4", 3)
        state_license = ElementAccess("REF", 2, qualifier=(1, "0B"))
        provider_UPIN = ElementAccess("REF", 2, qualifier=(1, "1G"))
        pharmacy_number = ElementAccess("REF", 2, qualifier=(1, "D3"))
        payee_id = ElementAccess("REF", 2, qualifier=(1, "PQ"))
        tax_id = ElementAccess("REF", 2, qualifier=(1, "TJ"))

    class _Claims(X12LoopBridge):
        loopName = "2000"
        number = ElementAccess("LX", 1)
        provider_id = ElementAccess("TS3", 1)
        facility_type_code = ElementAccess("TS3", 2)
        fiscal_period_end = ElementAccess("TS3", 3, x12type=D8)
        claim_count = ElementAccess("TS3", 4)
        total_claim_charge = ElementAccess("TS3", 5)
        # All of the below are optional and a 0/None value does not
        # neccessarily mean that value is *actually* 0
        total_covered_charge = ElementAccess("TS3", 6)
        total_noncovered_charge = ElementAccess("TS3", 7)
        total_denied_charge = ElementAccess("TS3", 8)
        total_provider_payment = ElementAccess("TS3", 9)
        total_interest = ElementAccess("TS3", 10)
        total_contractual_adjustment = ElementAccess("TS3", 11)
        total_gramm_rudman_reduction = ElementAccess("TS3", 12)
        total_msp_payer = ElementAccess("TS3", 13)
        total_blood_deducible = ElementAccess("TS3", 14)
        total_non_lab_charge = ElementAccess("TS3", 15)
        total_coinsurance = ElementAccess("TS3", 16)
        total_hcpcs_reported_charge = ElementAccess("TS3", 17)
        total_hspcs_payable = ElementAccess("TS3", 18)
        total_deductible = ElementAccess("TS3", 19)
        total_professional_component = ElementAccess("TS3", 20)
        total_msp_patient_liability_met = ElementAccess("TS3", 21)
        total_patient_reimbursement = ElementAccess("TS3", 22)
        total_pip_claim = ElementAccess("TS3", 23)
        # TODO: TS2 segment

    class _ClaimPayment(X12LoopBridge):
        loopName = "2100"

    def loops(self, theClass, anX12Message):
        return [theClass(loop) for loop in
                anX12Message.descendant("loop", theClass.loopName)]

    def __init__(self, anX12Message):
        """Examine the message and extract the relevant Loops."""
        self.payer = self.loops(self._Payer, anX12Message)[0]  # Only 1 allowed
        self.payee = self.loops(self._Payee, anX12Message)[0]  # Only 1 allowed
        self.claims = self.loops(self._Claims, anX12Message)
