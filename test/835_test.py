import unittest
import logging
import sys
import datetime

from parsers import M835_4010_X091_A1
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

if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
