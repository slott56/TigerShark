import datetime
from decimal import Decimal
import logging
import sys
import unittest

from tigershark.facade import f271
from tigershark.parsers import M271_4010_X092_A1


class TestParsed271(unittest.TestCase):
    def setUp(self):
        m = M271_4010_X092_A1.parsed_271
        with open('tests/271-example-2.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        self.f = f271.F271_4010(parsed)

    def test_number_of_facades(self):
        self.assertEqual(len(self.f.facades), 1)

    def test_header(self):
        h = self.f.facades[0].header.hierarchical_transaction_info
        self.assertEqual(h.structure, ("0022", "Information Source, "
                "Information Receiver, Subscriber, or Dependent."))
        self.assertEqual(h.purpose, ("11", "Response"))
        self.assertEqual(h.transaction_id, "140")
        self.assertEqual(h.creation_date, datetime.date(2012, 8, 30))
        self.assertEqual(h.creation_time, datetime.time(9, 31, 22))

    def test_number_of_receivers(self):
        self.assertEqual(len(self.f.facades[0].source.receivers), 1)

    def test_number_of_subscribers(self):
        self.assertEqual(
                len(self.f.facades[0].source.receivers[0].subscribers), 1)

    def test_hierarchy(self):
        source = self.f.facades[0].source
        h = source.hierarchy
        self.assertEqual(h.id, "1")
        self.assertEqual(h.parent_id, '')
        self.assertEqual(h.level, ("20", "Information Source"))
        self.assertTrue(h.has_children)

        receiver = source.receivers[0]
        h = receiver.hierarchy
        self.assertEqual(h.id, "2")
        self.assertEqual(h.parent_id, '1')
        self.assertEqual(h.level, ("21", "Information Receiver"))
        self.assertTrue(h.has_children)

        subscriber = receiver.subscribers[0]
        h = subscriber.hierarchy
        self.assertEqual(h.id, "3")
        self.assertEqual(h.parent_id, '2')
        self.assertEqual(h.level, ("22", "Subscriber"))
        self.assertFalse(h.has_children)

    def test_source(self):
        source = self.f.facades[0].source
        name = source.source_information.name
        self.assertEqual(name.entity_identifier,
                ("PR", "Payer"))
        self.assertEqual(name.entity_type,
                ("2", "Non-Person Entity"))
        self.assertEqual(name.org_name, "COMMERCIAL SAMPLE")
        self.assertEqual(name.id_code, "44444")
        self.assertEqual(name.id_code_qual,
                ("PI", "Payor Identification"))
        self.assertFalse(name.is_person)
        self.assertTrue(name.is_organization)

    def test_receiver(self):
        receiver = self.f.facades[0].source.receivers[0]
        name = receiver.receiver_information.name
        self.assertEqual(name.entity_identifier,
                ("1P", "Provider"))
        self.assertEqual(name.entity_type,
                ("2", "Non-Person Entity"))
        self.assertEqual(name.org_name, "")
        self.assertEqual(name.id_code, "1234567890")
        self.assertEqual(name.id_code_qual,
                ("XX", "Health Care Financing Administration National "\
                        "Provider Identifier"))
        self.assertFalse(name.is_person)
        self.assertTrue(name.is_organization)

    def test_subscriber(self):
        self.assertEqual(
                len(self.f.facades[0].source.receivers[0].subscribers), 1)

    def test_subscriber_trace_numbers(self):
        def _test(i, trace_type, trace_number, entity_id, entity_addl_id):
            self.assertEqual(subscriber.trace_numbers[i].trace_type,
                    trace_type)
            self.assertEqual(subscriber.trace_numbers[i].trace_number,
                    trace_number)
            self.assertEqual(subscriber.trace_numbers[i].entity_id,
                    entity_id)
            self.assertEqual(
                    subscriber.trace_numbers[i].entity_additional_id,
                    entity_addl_id)
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        self.assertEqual(len(subscriber.trace_numbers), 3)
        _test(0, ("2",
                "Referenced Transaction Trace Numbers (Value from 270)"),
                "51813246", "9ZIRMEDCOM", "")
        _test(1, ("1", "Current Transaction Trace Numbers"),
                "53637360", "9ZIRMEDCOM", "ELR ID")
        _test(2, ("1", "Current Transaction Trace Numbers"),
                "51893570", "9ZIRMEDCOM", "ELI ID")

    def test_subscriber_name(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        name = subscriber.subscriber_information.name
        self.assertEqual(name.entity_identifier,
                ("IL", "Insured"))
        self.assertEqual(name.entity_type,
                ("1", "Person"))
        self.assertEqual(name.id_code, "111111111")
        self.assertEqual(name.id_code_qual,
                ("MI", "Member Identification Number"))
        self.assertTrue(name.is_person)
        self.assertFalse(name.is_organization)

    def test_subscriber_address(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        info = subscriber.subscriber_information
        self.assertEqual(info.address_street.addr1, "3333 SOMEWHERE ST")
        self.assertEqual(info.address_location.city, "ANYWHERE")
        self.assertEqual(info.address_location.state, "LA")
        self.assertEqual(info.address_location.zip, "71104")

    def test_subscriber_dates(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        self.assertEqual(len(subscriber.subscriber_information.dates), 1)
        date = subscriber.subscriber_information.dates[0]
        self.assertEqual(date.type, ("307", "Eligibility"))
        self.assertEqual(date.time, datetime.date(2005, 2, 1))
        self.assertEqual(date.time_range, None)

    def test_subscriber_demographic_information(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        demo = subscriber.subscriber_information.demographic_information
        self.assertEqual(demo.gender, ('F', 'Female'))
        self.assertEqual(demo.birth_date, datetime.date(1937, 3, 5))

    def test_subscriber_eligibility_information(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        self.assertEqual(len(subscriber.eligibility_or_benefit_information),
                109)

    def test_subscriber_eligibility_group_1(self):
        # First Eligibility info has related entity information
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        eb = subscriber.eligibility_or_benefit_information[0]
        self.assertEqual(eb.coverage_information.information_type,
                ('1', 'Active Coverage'))
        self.assertEqual(eb.coverage_information.coverage_level, None)
        self.assertEqual(eb.coverage_information.service_type,
                ('30', 'Health Benefit Plan Coverage'))
        self.assertEqual(eb.coverage_information.insurance_type,
                ('C1', 'Commercial'))
        self.assertEqual(eb.coverage_information.description,
                "MANAGED INDEMNITY")
        name = eb.benefit_related_entity.name
        self.assertEqual(name.entity_identifier,
                ("PR", "Payer"))
        self.assertEqual(name.entity_type,
                ("2", "Non-Person Entity"))
        self.assertEqual(name.org_name,
                "UNITEDHEALTHCARE")
        self.assertFalse(name.is_person)
        self.assertTrue(name.is_organization)

    def test_subscriber_eligibility_group_2(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        eb = subscriber.eligibility_or_benefit_information
        self.assertEqual(eb[1].coverage_information.information_type,
                ('G', 'Out of Pocket (Stop Loss)'))
        self.assertEqual(eb[1].coverage_information.coverage_level,
                ('FAM', 'Family'))
        self.assertEqual(eb[1].coverage_information.insurance_type,
                ('C1', 'Commercial'))
        self.assertEqual(eb[1].coverage_information.benefit_amount,
                Decimal('3000'))
        self.assertTrue(eb[1].coverage_information.in_plan_network)

        self.assertEqual(eb[2].coverage_information.time_period_type,
                ('24', 'Year to Date'))
        self.assertEqual(eb[2].coverage_information.benefit_amount,
                Decimal('3025.9'))
        self.assertTrue(eb[2].coverage_information.in_plan_network)

        self.assertEqual(eb[3].coverage_information.time_period_type,
                ('29', 'Remaining'))
        self.assertEqual(eb[3].coverage_information.benefit_amount,
                Decimal('0'))
        self.assertTrue(eb[3].coverage_information.in_plan_network)

    def test_subscriber_eligibility_group_3(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        eb = subscriber.eligibility_or_benefit_information
        self.assertEqual(eb[4].coverage_information.information_type,
                ('C', 'Deductible'))
        self.assertEqual(eb[4].coverage_information.coverage_level,
                ('FAM', 'Family'))
        self.assertEqual(eb[4].coverage_information.insurance_type, None)
        self.assertEqual(eb[4].coverage_information.benefit_amount,
                Decimal('236'))
        self.assertTrue(eb[4].coverage_information.in_plan_network)

        self.assertEqual(eb[5].coverage_information.time_period_type,
                ('24', 'Year to Date'))
        self.assertEqual(eb[5].coverage_information.benefit_amount,
                Decimal('0'))
        self.assertTrue(eb[5].coverage_information.in_plan_network)

        self.assertEqual(eb[6].coverage_information.time_period_type,
                ('29', 'Remaining'))
        self.assertEqual(eb[6].coverage_information.benefit_amount,
                Decimal('236'))
        self.assertTrue(eb[6].coverage_information.in_plan_network)

    def test_subscriber_eligibility_group_4(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        eb = subscriber.eligibility_or_benefit_information
        self.assertFalse(eb[7].coverage_information.in_plan_network)
        self.assertFalse(eb[8].coverage_information.in_plan_network)
        self.assertFalse(eb[9].coverage_information.in_plan_network)

    def test_subscriber_eligibility_group_5(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        eb = subscriber.eligibility_or_benefit_information
        self.assertEqual(eb[13].coverage_information.coverage_level,
                ('IND', 'Individual'))
        self.assertEqual(eb[13].coverage_information.insurance_type,
                ('C1', 'Commercial'))
        self.assertEqual(eb[13].coverage_information.benefit_amount,
                Decimal('1500'))
        self.assertTrue(eb[13].coverage_information.in_plan_network)

        self.assertEqual(eb[14].coverage_information.time_period_type,
                ('24', 'Year to Date'))
        self.assertEqual(eb[14].coverage_information.benefit_amount,
                Decimal('1500'))
        self.assertTrue(eb[14].coverage_information.in_plan_network)

        self.assertEqual(eb[15].coverage_information.time_period_type,
                ('29', 'Remaining'))
        self.assertEqual(eb[15].coverage_information.benefit_amount,
                Decimal('0'))
        self.assertTrue(eb[15].coverage_information.in_plan_network)

    def test_subscriber_eligibility_group_6(self):
        def _test(i, service_type):
            self.assertEqual(eb[i].coverage_information.information_type,
                    ('I', 'Non-Covered'))
            self.assertEqual(eb[i].coverage_information.service_type,
                    service_type)

        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        eb = subscriber.eligibility_or_benefit_information
        _test(25, ('35', 'Dental Care'))
        _test(26, ('92', 'Generic Prescription Drug'))
        _test(27, ('91', 'Brand Name Prescription Drug'))
        _test(28, ('88', 'Pharmacy'))

        self.assertEqual(eb[29].coverage_information.information_type,
                ('1', 'Active Coverage'))
        self.assertEqual(eb[29].coverage_information.service_type,
                ('AE', 'Physical Medicine'))

    def test_subscriber_eligibility_group_7(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        eb = subscriber.eligibility_or_benefit_information
        self.assertEqual(eb[30].coverage_information.information_type,
                ('A', 'Co-Insurance'))
        self.assertEqual(eb[30].coverage_information.coverage_level,
                ('IND', 'Individual'))
        self.assertEqual(eb[30].coverage_information.service_type,
                ('AE', 'Physical Medicine'))
        self.assertEqual(eb[30].coverage_information.time_period_type,
                ('27', 'Visit'))
        self.assertEqual(eb[30].coverage_information.benefit_percent,
                Decimal('0.2'))
        self.assertTrue(eb[30].coverage_information.in_plan_network)


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
