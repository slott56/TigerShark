from facade import X12LoopBridge
#from facade import X12SegmentBridge
from facade import ElementAccess
#from facade import SegmentSequenceAccess
#from facade import SegmentConversion
#from facade import SequenceOf
#from facade import ElementSequenceAccess
from facade import CompositeAccess
#from facade import CompositeSequenceAccess
from facade import D8
from facade import Facade


class F835_4010(Facade):
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

    class _ClaimsOverview(X12LoopBridge):
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

    class _Claim(Facade, X12LoopBridge):
        class _ServiceInfo(X12LoopBridge):
            """ Oh jeez, I'm so sorry about this mess.

            Each claim has several nested 2110 loops that have additional
            information pertaining to a claim. This is usually when the
            insurance company doesn't want to pay the whole amount billed.
            The only way I could think of to implement this is to do this
            mess of multiple inheritance.

            Rest assured I did not come to this decision lightly."""
            loopName = "2110"
            hcpcs_code = CompositeAccess("SVC", "HC", 1)
            charge = ElementAccess("SVC", 2)
            payment = ElementAccess("SVC", 3)
            quantity = ElementAccess("SVC", 5)
            start_date = ElementAccess("DTM", 2, qualifier=(1, "150"),
                    x12type=D8)
            end_date = ElementAccess("DTM", 2, qualifier=(1, "151"),
                    x12type=D8)
            # Claim adjustments
            # WARNING: This should add up all of the amounts in this segment,
            # but it DOESN'T!
            adjustment_contractual_obligation = ElementAccess("CAS", 3,
                    qualifier=(1, "CO"))
            adjustment_correction_and_reveral = ElementAccess("CAS", 3,
                    qualifier=(1, "CR"))
            adjustment_other = ElementAccess("CAS", 3, qualifier=(1, "OA"))
            adjustment_payor_initiated_reductions = ElementAccess("CAS", 3,
                    qualifier=(1, "PI"))
            adjustment_patient_responsibility = ElementAccess("CAS", 3,
                    qualifier=(1, "PR"))

            # Identification
            apg_number = ElementAccess("REF", 2, qualifier=(1, "1S"))
            provider_control_number = ElementAccess("REF", 2,
                    qualifier=(1, "6R"))
            authorization_number = ElementAccess("REF", 2,
                    qualifier=(1, "BB"))
            attachment_code = ElementAccess("REF", 2, qualifier=(1, "E9"))
            prior_authorization_number = ElementAccess("REF", 2,
                    qualifier=(1, "G1"))
            predetermination_of_benefits_id = ElementAccess("REF", 2,
                    qualifier=(1, "G3"))
            location_number = ElementAccess("REF", 2, qualifier=(1, "LU"))
            rate_code_number = ElementAccess("REF", 2, qualifier=(1, "RB"))
            # TODO: Rendering provider info?

            # Line-item claim amounts
            allowed_amount = ElementAccess("AMT", 2, qualifier=(1, "B6"))
            per_day_limit = ElementAccess("AMT", 2, qualifier=(1, "DY"))
            deduction_amount = ElementAccess("AMT", 2, qualifier=(1, "KH"))
            tax_amount = ElementAccess("AMT", 2, qualifier=(1, "T"))
            total_claim_before_taxes = ElementAccess("AMT", 2,
                    qualifier=(1, "T2"))

            not_covered_quantity = ElementAccess("QTY", 2, qualifier=(1, "NE"))

        loopName = "2100"
        patient_control_number = ElementAccess("CLP", 1)
        status_code = ElementAccess("CLP", 2)  # TODO enum?
        total_charge = ElementAccess("CLP", 3)
        payment = ElementAccess("CLP", 4)
        patient_responsibility = ElementAccess("CLP", 5)
        claim_type = ElementAccess("CLP", 6)  # TODO enum?
        payer_claim_control_number = ElementAccess("CLP", 7)
        facility_type = ElementAccess("CLP", 8)
        frequency_code = ElementAccess("CLP", 9)
        diagnosis_related_group_weight = ElementAccess("CLP", 11)
        discharge_fraction = ElementAccess("CLP", 12)
        # OH MAN, is there really no better way to do this?
        # Patient Info
        patient_entity_type = ElementAccess("NM1", 2, qualifier=(1, "QC"))
        patient_last_name = ElementAccess("NM1", 3, qualifier=(1, "QC"))
        patient_first_name = ElementAccess("NM1", 4, qualifier=(1, "QC"))
        patient_middle_initial = ElementAccess("NM1", 5, qualifier=(1, "QC"))
        patient_suffix = ElementAccess("NM1", 7, qualifier=(1, "QC"))
        patient_id_code_qual = ElementAccess("NM1", 8,
                qualifier=(1, "QC"))  # TODO enum?
        patient_id_code = ElementAccess("NM1", 9, qualifier=(1, "QC"))
        # Insured Info
        insured_entity_type = ElementAccess("NM1", 2, qualifier=(1, "IL"))
        insured_last_name = ElementAccess("NM1", 3, qualifier=(1, "IL"))
        insured_first_name = ElementAccess("NM1", 4, qualifier=(1, "IL"))
        insured_middle_initial = ElementAccess("NM1", 5, qualifier=(1, "IL"))
        insured_suffix = ElementAccess("NM1", 7, qualifier=(1, "IL"))

        insured_id_code_qual = ElementAccess("NM1", 8,
                qualifier=(1, "IL"))  # TODO enum?
        insured_id_code = ElementAccess("NM1", 9, qualifier=(1, "IL"))
        # Corrected Info
        corrected_insured_entity_type = ElementAccess("NM1", 2,
                qualifier=(1, "74"))
        corrected_insured_last_name = ElementAccess("NM1", 3,
                qualifier=(1, "74"))
        corrected_insured_first_name = ElementAccess("NM1", 4,
                qualifier=(1, "74"))
        corrected_insured_middle_initial = ElementAccess("NM1", 5,
                qualifier=(1, "74"))
        corrected_insured_suffix = ElementAccess("NM1", 7,
                qualifier=(1, "74"))
        corrected_insured_id_code_qual = ElementAccess("NM1", 8,
                qualifier=(1, "74"))  # TODO enum?
        corrected_insured_id_code = ElementAccess("NM1", 9,
                qualifier=(1, "74"))
        # Service Provider
        service_provider_entity_type = ElementAccess("NM1", 2,
                qualifier=(1, "74"))
        service_provider_last_name = ElementAccess("NM1", 3,
                qualifier=(1, "74"))
        service_provider_first_name = ElementAccess("NM1", 4,
                qualifier=(1, "74"))
        service_provider_middle_initial = ElementAccess("NM1", 5,
                qualifier=(1, "74"))
        service_provider_suffix = ElementAccess("NM1", 7,
                qualifier=(1, "74"))
        service_provider_id_code_qual = ElementAccess("NM1", 8,
                qualifier=(1, "74"))  # TODO enum?
        service_provider_id_code = ElementAccess("NM1", 9,
                qualifier=(1, "74"))
        # Crossover Carrier
        crossover_carrier_entity_type = ElementAccess("NM1", 2,
                qualifier=(1, "TT"))
        crossover_carrier_org_name = ElementAccess("NM1", 3,
                qualifier=(1, "74"))
        crossover_carrier_id_code_qual = ElementAccess("NM1", 8,
                qualifier=(1, "TT"))  # TODO enum?
        crossover_carrier_id_code = ElementAccess("NM1", 9,
                qualifier=(1, "TT"))
        # Corrected Priority Payer
        corrected_priority_payer_entity_type = ElementAccess("NM1", 2,
                qualifier=(1, "TT"))
        corrected_priority_payer_org_name = ElementAccess("NM1", 3,
                qualifier=(1, "74"))
        corrected_priority_payer_id_code_qual = ElementAccess("NM1", 8,
                qualifier=(1, "TT"))  # TODO enum?
        corrected_priority_payer_id_code = ElementAccess("NM1", 9,
                qualifier=(1, "TT"))
        # TODO: Medicare inpatient/outpatient adjudication?

        # References
        group_or_policy_number = ElementAccess("REF", 2, qualifier=(1, "1L"))
        member_id = ElementAccess("REF", 2, qualifier=(1, "1W"))
        repriced_claim_reference_number = ElementAccess("REF", 2,
                qualifier=(1, "9A"))
        adjusted_repriced_claim_reference_number = ElementAccess("REF", 2,
                qualifier=(1, "9B"))
        employee_id = ElementAccess("REF", 2, qualifier=(1, "A6"))
        authorization_number = ElementAccess("REF", 2, qualifier=(1, "BB"))
        contract_class = ElementAccess("REF", 2, qualifier=(1, "CE"))
        medical_record_id = ElementAccess("REF", 2, qualifier=(1, "EA"))
        original_reference_number = ElementAccess("REF", 2,
                qualifier=(1, "F8"))
        prior_authorization_number = ElementAccess("REF", 2,
                qualifier=(1, "G1"))
        predetermination_of_benefits_number = ElementAccess("REF", 2,
                qualifier=(1, "G3"))
        insurance_policy_number = ElementAccess("REF", 2, qualifier=(1, "IG"))
        ssn = ElementAccess("REF", 2, qualifier=(1, "SY"))

        provider_commercial_number = ElementAccess("REF", 2,
                qualifier=(1, "G2"))

        # Dates
        date_expiration = ElementAccess("DTM", 2, qualifier=(1, "036"),
                x12type=D8)
        date_received = ElementAccess("DTM", 2, qualifier=(1, "050"),
                x12type=D8)
        date_statement_period_start = ElementAccess("DTM", 2,
                qualifier=(1, "232"), x12type=D8)
        date_statement_period_end = ElementAccess("DTM", 2,
                qualifier=(1, "233"), x12type=D8)

        # Claim payment info
        total_covered_charge = ElementAccess("AMT", 2, qualifier=(1, "AU"))
        discount_amount = ElementAccess("AMT", 2, qualifier=(1, "D8"))
        per_day_limit = ElementAccess("AMT", 2, qualifier=(1, "DY"))
        patient_amount_paid = ElementAccess("AMT", 2, qualifier=(1, "F5"))
        interest = ElementAccess("AMT", 2, qualifier=(1, "I"))
        negative_ledger = ElementAccess("AMT", 2, qualifier=(1, "NL"))
        tax_amount = ElementAccess("AMT", 2, qualifier=(1, "T"))
        total_claim_before_taxes = ElementAccess("AMT", 2,
                qualifier=(1, "T2"))

        def __init__(self, anX12Message, *args, **kwargs):
            super(F835_4010._Claim, self).__init__(anX12Message, *args,
                    **kwargs)
            self.infos = self.loops(self._ServiceInfo, anX12Message)

    def __init__(self, anX12Message):
        """Examine the message and extract the relevant Loops."""
        self.payer = self.loops(self._Payer, anX12Message)
        self.payee = self.loops(self._Payee, anX12Message)
        self.claims_overview = self.loops(self._ClaimsOverview, anX12Message)
        self.claims = self.loops(self._Claim, anX12Message)
