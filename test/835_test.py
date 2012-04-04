import unittest
import logging
import sys
import datetime


import M835_4010_X091_A1
from facade import f835


class TestParsed835(unittest.TestCase):
    def setUp(self):
        m = M835_4010_X091_A1.parsed_835
        with open('835-example.edi') as f:
            parsed = m.unmarshall(f.read().strip())
        self.f = f835.F835_4010(parsed)

    ## Header ##
    def test_financial_information(self):
        fi = self.f.header.financial_information
        self.assertEqual(fi.transaction_type,
                ('I', 'Remittance Information Only'))
        self.assertEqual(fi.amount, 12345.67)
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
        rtn = self.f.header.reassociation_trace_number
        self.assertEqual(rtn.trace_type,
                ('1', 'Current Transaction Trace Numbers'))
        self.assertEqual(rtn.check_or_eft_trace_number, '1QG11111111')
        self.assertEqual(rtn.payer_id, '1111111111')
        self.assertEqual(rtn.originating_company_supplemental_code,
                '000011111')

    def test_production_date(self):
        pd = self.f.header.production_date
        self.assertEqual(pd.date, datetime.date(2012, 03, 19))

    ## PAYER ##
    def test_payer(self):
        p = self.f.payer
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

    ## PAYEE ##
    def test_payee(self):
        p = self.f.payee
        c = p.contact_details
        self.assertEqual(c.name, 'MY CLINIC')
        self.assertEqual(c.id_qualifier,
                ('XX', 'Health Care Financing Administration National '\
                        'Provider ID'))
        self.assertEqual(c.id, '1333333333')
        self.assertEqual(c.addr1, '123 HEALTHCARE STREET')
        self.assertEqual(c.city, 'SAN FRANCISCO')
        self.assertEqual(c.zip, '94109')
        self.assertEqual(p.tax_id, '777777777')

    ## Claims Overview ##
    def test_claims_overview(self):
        co = self.f.claims_overview
        self.assertEqual(co.number, '1')
        self.assertEqual(co.provider_id, '1333333333')
        self.assertEqual(co.facility_type_code, '81')
        self.assertEqual(co.fiscal_period_end, datetime.date(2012, 12, 31))
        self.assertEqual(co.claim_count, '2')
        self.assertEqual(co.total_claim_charge, 23456.78)
        self.assertEqual(co.total_covered_charge, 12345.67)

    ## Claims ##
    def test_claims(self):
        claims = self.f.claims
        c = claims[0]
        # Claim details
        pi = c.payment_info
        self.assertEqual(pi.patient_control_number, "001-DDDDDDDDDD")
        self.assertEqual(pi.status_code, ('1', 'Processed as Primary'))
        self.assertEqual(pi.total_charge, 200.02)
        self.assertEqual(pi.payment, 200.02)
        self.assertEqual(pi.patient_responsibility, 0.0)
        self.assertEqual(pi.claim_type, ('13', 'Point of Service (POS)'))
        self.assertEqual(pi.payer_claim_control_number,
                '1234567890 0987654321')
        self.assertEqual(pi.facility_type, '81')
        self.assertEqual(pi.total_covered_charge, 200.02)

        # Patient
        patient = c.patient
        self.assertTrue(patient.is_person())
        self.assertEqual(patient.last_name, "DOE")
        self.assertEqual(patient.first_name, "JOHN")
        self.assertEqual(patient.middle_initial, "")
        self.assertEqual(patient.suffix, "")

        # Insured
        insured = c.insured
        self.assertTrue(insured.is_person())
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
        self.assertTrue(provider.is_organization())
        self.assertEqual(provider.org_name, "MY CLINIC")
        self.assertEqual(provider.id_code_qual, (
                ("XX", "Health Care Financing Administration National "\
                        "Provider Identifier")))
        self.assertEqual(provider.id_code, '1333333333')

        # Other stuff
        self.assertEqual(c.group_or_policy_number, '5G5G5G')
        self.assertEqual(c.contract_class, 'CHOYC+')
        self.assertEqual(c.date_received, datetime.date(2012, 03, 02))
        self.assertEqual(c.date_statement_period_start,
                datetime.date(2012, 02, 22))

        # Line item charges
        l = c.line_items[0]
        self.assertEqual(l.hcpcs_code[0], '88888')
        self.assertEqual(l.charge, 200.02)
        self.assertEqual(l.payment, 200.02)
        self.assertEqual(l.quantity, '1')
        self.assertEqual(l.service_date, datetime.date(2012, 02, 22))
        self.assertEqual(l.provider_control_number, '251111111111')
        self.assertEqual(l.allowed_amount, 200.02)

        # Second claim!
        c = claims[1]
        # Claim details
        pi = c.payment_info
        self.assertEqual(pi.patient_control_number, "001-SSSSSSSSSS")
        self.assertEqual(pi.status_code, ('1', 'Processed as Primary'))
        self.assertEqual(pi.total_charge, 23276.56)
        self.assertEqual(pi.payment, 12000.65)
        self.assertEqual(pi.patient_responsibility, 145.0)
        self.assertEqual(pi.claim_type,
                ("14", "Exclusive Provider Organization (EPO)"))
        self.assertEqual(pi.payer_claim_control_number,
                '2234567890 0987654322')
        self.assertEqual(pi.facility_type, '81')
        self.assertEqual(pi.total_covered_charge, 12145.65)

        # Patient
        patient = c.patient
        self.assertTrue(patient.is_person())
        self.assertEqual(patient.last_name, "SMITH")
        self.assertEqual(patient.first_name, "JOHN")

        # Insured
        insured = c.insured
        self.assertTrue(insured.is_person())
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

        # Line item charges
        l = c.line_items[0]
        self.assertEqual(l.hcpcs_code[0], '88888')
        self.assertEqual(l.charge, 23276.56)
        self.assertEqual(l.payment, 12145.65)
        self.assertEqual(l.quantity, '1')
        self.assertEqual(l.service_date, datetime.date(2012, 02, 21))
        self.assertEqual(l.provider_control_number, '252222222222')
        self.assertEqual(l.adjustment_contractual_obligation, 11130.91)
        self.assertEqual(l.allowed_amount, 12145.65)


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
