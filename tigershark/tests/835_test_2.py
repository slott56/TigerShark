import unittest
import logging
import sys
import datetime
from decimal import Decimal


from tigershark.facade import f835
from tigershark.parsers import M835_4010_X091_A1


class TestParsed835(unittest.TestCase):
    def setUp(self):
        m = M835_4010_X091_A1.parsed_835
        with open('835-example-2.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        self.f = f835.F835_4010(parsed)

    ## Header ##
    def test_financial_information(self):
        fi = self.f.facades[0].header.financial_information
        self.assertEqual(fi.transaction_type,
                ('I', 'Remittance Information Only'))
        self.assertEqual(fi.amount, Decimal('12345.67'))
        self.assertEqual(fi.credit_or_debit, ('C', 'Credit'))
        self.assertEqual(fi.payment_method,
                ('ACH', 'Automated Clearing House (ACH)'))
        self.assertEqual(fi.payment_format,
                ('CCP', 'Cash Concentration/Disbursement Plus Addenda'))
        self.assertEqual(fi.sender_aba_transit_routing_number, '999999999')
        self.assertEqual(fi.sender_canadian_bank_branch_and_institution_number,
                None)
        self.assertEqual(fi.sender_account_type, ('DA', 'Demand Deposit'))
        self.assertEqual(fi.sender_bank_account_number, '1234567890')
        self.assertEqual(fi.sender_id, '1111111111')
        self.assertEqual(fi.sender_supplemental_id, '000011111')
        self.assertEqual(fi.receiver_aba_transit_routing_number, '222222222')
        self.assertEqual(
                fi.receiver_canadian_bank_branch_and_institution_number, None)
        self.assertEqual(fi.receiver_account_type, ('DA', 'Demand Deposit'))
        self.assertEqual(fi.receiver_bank_account_number, '3333333333')
        self.assertEqual(fi.issue_date, datetime.date(2012, 03, 22))

    def test_reassociation_trace_number(self):
        rtn = self.f.facades[0].header.reassociation_trace_number
        self.assertEqual(rtn.trace_type,
                ('1', 'Current Transaction Trace Numbers'))
        self.assertEqual(rtn.check_or_eft_trace_number, '1QG11111111')
        self.assertEqual(rtn.payer_id, '1111111111')
        self.assertEqual(rtn.originating_company_supplemental_code,
                '000011111')

        rtn = self.f.facades[1].header.reassociation_trace_number
        self.assertEqual(rtn.trace_type,
                ('1', 'Current Transaction Trace Numbers'))
        self.assertEqual(rtn.check_or_eft_trace_number, '1QG11111112')
        self.assertEqual(rtn.payer_id, '1111111112')
        self.assertEqual(rtn.originating_company_supplemental_code,
                '000011112')

    def test_production_date(self):
        pd = self.f.facades[0].header.production_date
        self.assertEqual(pd.date, datetime.date(2012, 03, 19))
        pd = self.f.facades[1].header.production_date
        self.assertEqual(pd.date, datetime.date(2012, 03, 19))

    ## PAYER ##
    def test_payer(self):
        p = self.f.facades[0].payer
        c = p.contact_details
        self.assertEqual(c.name, 'UNITED HEALTHCARE INSURANCE COMPANY')
        self.assertEqual(c.id_qualifier,
            ('XV', 'Health Care Financing Administration National Plan ID'))
        self.assertEqual(c.id, '87726')
        self.assertEqual(c.addr1, '9900 BREN ROAD')
        self.assertEqual(c.city, 'MINNETONKA')
        self.assertEqual(c.state, 'MN')
        self.assertEqual(c.zip, '553430000')
        self.assertEqual(c.contact_name, 'ATLANTA SERVICE CENTER')
        self.assertEqual(c.contact_phone, '8778423210')
        self.assertEqual(c.contact_phone_ext, None)
        self.assertEqual(p.payer_id, '87726')

        p = self.f.facades[1].payer
        c = p.contact_details
        self.assertEqual(c.name, 'ACME, INC. A WHOLLY OWNED SUBSIDIARY OF '\
                'UNITED HEALTHCARE INSURANCE COMPANY')
        self.assertEqual(c.id_qualifier,
            ('XV', 'Health Care Financing Administration National Plan ID'))
        self.assertEqual(c.id, '87726')
        self.assertEqual(c.addr1, '123 MAIN STREET')
        self.assertEqual(c.city, 'ANYTOWN')
        self.assertEqual(c.state, 'CA')
        self.assertEqual(c.zip, '940660000')
        self.assertEqual(p.payer_id, '87726')

    ## PAYEE ##
    def test_payee(self):
        def _test():
            self.assertEqual(c.name, 'MY CLINIC')
            self.assertEqual(c.id_qualifier,
                    ('XX', 'Health Care Financing Administration National '\
                            'Provider ID'))
            self.assertEqual(c.id, '1333333333')
            self.assertEqual(c.addr1, '123 HEALTHCARE STREET')
            self.assertEqual(c.city, 'SAN FRANCISCO')
            self.assertEqual(c.zip, '94109')
            self.assertEqual(p.tax_id, '777777777')

        p = self.f.facades[0].payee
        c = p.contact_details
        _test()
        p = self.f.facades[1].payee
        c = p.contact_details
        _test()

    ## Claims Overview ##
    def test_claims_overview(self):
        co = self.f.facades[0].claims_overview
        self.assertEqual(co.number, '1')
        self.assertEqual(co.provider_id, '1333333333')
        self.assertEqual(co.facility_type_code, '81')
        self.assertEqual(co.fiscal_period_end, datetime.date(2012, 12, 31))
        self.assertEqual(co.claim_count, '1')
        self.assertEqual(co.total_claim_charge, Decimal('200.02'))
        self.assertEqual(co.total_covered_charge, Decimal('200.02'))

        co = self.f.facades[1].claims_overview
        self.assertEqual(co.number, '1')
        self.assertEqual(co.provider_id, '1333333333')
        self.assertEqual(co.facility_type_code, '81')
        self.assertEqual(co.fiscal_period_end, datetime.date(2012, 12, 31))
        self.assertEqual(co.claim_count, '1')
        self.assertEqual(co.total_claim_charge, Decimal('23276.56'))
        self.assertEqual(co.total_covered_charge, Decimal('12000.65'))

    ## Claims ##
    def test_claims(self):
        claims = self.f.facades[0].claims
        c = claims[0]
        # Claim details
        pi = c.payment_info
        self.assertEqual(pi.patient_control_number, "001-DDDDDDDDDD")
        self.assertEqual(pi.status_code, ('1', 'Processed as Primary'))
        self.assertEqual(pi.total_charge, Decimal('200.02'))
        self.assertEqual(pi.payment, Decimal('200.02'))
        self.assertEqual(pi.patient_responsibility, Decimal('0.0'))
        self.assertEqual(pi.claim_type, ('13', 'Point of Service (POS)'))
        self.assertEqual(pi.payer_claim_control_number,
                '1234567890 0987654321')
        self.assertEqual(pi.facility_type, '81')
        self.assertEqual(pi.total_covered_charge, Decimal('200.02'))

        # Patient
        patient = c.patient
        self.assertTrue(patient.is_person())
        self.assertFalse(patient.is_organization())
        self.assertEqual(patient.last_name, "DOE")
        self.assertEqual(patient.first_name, "JOHN")
        self.assertEqual(patient.middle_initial, "")
        self.assertEqual(patient.suffix, "")

        # Insured
        insured = c.insured
        self.assertTrue(insured.is_person())
        self.assertFalse(insured.is_organization())
        self.assertEqual(insured.last_name, "DOE")
        self.assertEqual(insured.first_name, "JANE")
        self.assertEqual(insured.middle_initial, "")
        self.assertEqual(insured.suffix, "")
        self.assertEqual(insured.id_code_qual,
                ("MI", "Member Identification Number"))
        self.assertEqual(insured.id_code, "123111111")

        # Corrected Info
        corrected = c.corrected_insured
        self.assertEqual(corrected.last_name, "DOE")
        self.assertEqual(corrected.first_name, "JANE")
        self.assertEqual(corrected.middle_initial, "D")

        # Service Provider
        provider = c.service_provider
        self.assertFalse(provider.is_person())
        self.assertTrue(provider.is_organization())
        self.assertEqual(provider.org_name, "MY CLINIC")
        self.assertEqual(provider.id_code_qual, (
                ("XX", "Health Care Financing Administration National "\
                        "Provider Identifier")))
        self.assertEqual(provider.id_code, '1333333333')

        # Other stuff
        self.assertEqual(c.group_or_policy_number, '5G5G5G')
        self.assertEqual(c.contract_class, 'CHOYC+')
        # If a received date isn't supplied, don't die just return None!
        self.assertEqual(c.date_received, None)
        self.assertEqual(c.date_statement_period_start,
                datetime.date(2012, 02, 22))
        self.assertEqual(c.claim_adjustments.patient_responsibility.amount_1,
                Decimal('0.0'))
        self.assertEqual(c.claim_adjustments.contractual_obligation.amount_1,
                Decimal('0.0'))

        # Line item charges
        l = c.line_items[0]
        self.assertEqual(l.hcpcs_code[0], '88888')
        self.assertEqual(l.charge, Decimal('200.02'))
        self.assertEqual(l.payment, Decimal('200.02'))
        self.assertEqual(l.quantity, '1')
        self.assertEqual(l.service_date, datetime.date(2012, 02, 22))
        self.assertEqual(l.provider_control_number, '251111111111')
        self.assertEqual(l.allowed_amount, Decimal('200.02'))
        self.assertEqual(l.claim_adjustments.patient_responsibility.amount_1,
                Decimal('0.0'))
        self.assertEqual(l.claim_adjustments.contractual_obligation.amount_1,
                Decimal('0.0'))

        # Second claim!
        claims = self.f.facades[1].claims
        c = claims[0]
        # Claim details
        pi = c.payment_info
        self.assertEqual(pi.patient_control_number, "001-SSSSSSSSST")
        self.assertEqual(pi.status_code, ('1', 'Processed as Primary'))
        self.assertEqual(pi.total_charge, Decimal('23276.56'))
        self.assertEqual(pi.payment, Decimal('12000.65'))
        self.assertEqual(pi.patient_responsibility, Decimal('145.0'))
        self.assertEqual(pi.claim_type,
                ("14", "Exclusive Provider Organization (EPO)"))
        self.assertEqual(pi.payer_claim_control_number,
                '2234567891 1987654322')
        self.assertEqual(pi.facility_type, '81')
        self.assertEqual(pi.total_covered_charge, Decimal('12145.65'))

        # Patient
        patient = c.patient
        self.assertTrue(patient.is_person())
        self.assertFalse(patient.is_organization())
        self.assertEqual(patient.last_name, "SMITH")
        self.assertEqual(patient.first_name, "JOHN")

        # Insured
        insured = c.insured
        self.assertTrue(insured.is_person())
        self.assertFalse(insured.is_organization())
        self.assertEqual(insured.last_name, "SMITH")
        self.assertEqual(insured.first_name, "JANE")
        self.assertEqual(insured.middle_initial, "")
        self.assertEqual(insured.suffix, "")
        self.assertEqual(insured.id_code_qual,
                ("MI", "Member Identification Number"))
        self.assertEqual(insured.id_code, "123222222")

        # Corrected Info
        corrected = c.corrected_insured
        self.assertEqual(corrected.last_name, "SMITH")
        self.assertEqual(corrected.first_name, "JANE")
        self.assertEqual(corrected.middle_initial, "A")

        # Other stuff
        self.assertEqual(c.group_or_policy_number, '717171')
        self.assertEqual(c.contract_class, 'CHOYC')
        self.assertEqual(c.date_received, datetime.date(2012, 03, 03))
        self.assertEqual(c.date_statement_period_start,
                datetime.date(2012, 02, 23))
        self.assertEqual(c.claim_adjustments.patient_responsibility.amount_1,
                Decimal('145.0'))
        # Don't look into the child loops for segments
        self.assertEqual(c.claim_adjustments.contractual_obligation.amount_1,
                Decimal('0.0'))

        # Line item charges
        l = c.line_items[0]
        self.assertEqual(l.hcpcs_code[0], '88888')
        self.assertEqual(l.charge, Decimal('23276.56'))
        self.assertEqual(l.payment, Decimal('12145.65'))
        self.assertEqual(l.quantity, '1')
        self.assertEqual(l.service_date, datetime.date(2012, 02, 21))
        self.assertEqual(l.provider_control_number, '252222222222')
        self.assertEqual(l.claim_adjustments.contractual_obligation.amount_1,
                Decimal('11130.91'))
        self.assertEqual(
                l.claim_adjustments.contractual_obligation.total_amount(),
                Decimal('11130.91'))
        self.assertEqual(l.claim_adjustments.patient_responsibility.amount_1,
                Decimal('0.0'))
        self.assertEqual(l.allowed_amount, Decimal('12145.65'))


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
