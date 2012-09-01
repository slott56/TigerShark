import datetime
import logging
import sys
import unittest

from tigershark.facade import f271
from tigershark.parsers import M271_4010_X092_A1


class TestParsed271(unittest.TestCase):
    def setUp(self):
        m = M271_4010_X092_A1.parsed_271
        with open('tests/271-example-dependent-rejection.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        self.f = f271.F271_4010(parsed)

    def test_number_of_facades(self):
        self.assertEqual(len(self.f.facades), 1)

    def test_header(self):
        h = self.f.facades[0].header.hierarchical_transaction_info
        self.assertEqual(h.structure, ("0022", "Information Source, "
                "Information Receiver, Subscriber, or Dependent."))
        self.assertEqual(h.purpose, ("11", "Response"))
        self.assertEqual(h.transaction_id, "58446")
        self.assertEqual(h.creation_date, datetime.date(2012, 6, 29))
        self.assertEqual(h.creation_time, datetime.time(17, 45, 29))

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
        self.assertTrue(h.has_children)

        dependent = subscriber.dependents[0]
        h = dependent.hierarchy
        self.assertEqual(h.id, "4")
        self.assertEqual(h.parent_id, '3')
        self.assertEqual(h.level, ("23", "Dependent"))
        self.assertFalse(h.has_children)

    def test_source(self):
        source = self.f.facades[0].source
        name = source.source_information.name
        self.assertEqual(name.entity_identifier,
                ("PR", "Payer"))
        self.assertEqual(name.entity_type,
                ("2", "Non-Person Entity"))
        self.assertEqual(name.org_name, "ANTHEM BLUE CROSS")
        self.assertEqual(name.id_code, "10319")
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
        self.assertEqual(name.org_name, "DR. SPACEMAN")
        self.assertEqual(name.id_code, "1111111111")
        self.assertEqual(name.id_code_qual,
                ("XX", "Health Care Financing Administration National "\
                        "Provider Identifier"))
        self.assertFalse(name.is_person)
        self.assertTrue(name.is_organization)

    def test_subscriber(self):
        self.assertEqual(
                len(self.f.facades[0].source.receivers[0].subscribers), 1)

    def test_dependent(self):
        self.assertEqual(len(self.f.facades[0].source.receivers[0].\
                subscribers[0].dependents), 1)

    def test_subscriber_rejection(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        self.assertEqual(
                len(subscriber.subscriber_information.request_validations),
                1)
        rejection = subscriber.subscriber_information.request_validations[0]
        self.assertEqual(rejection.valid_request, True)
        self.assertEqual(rejection.reject_reason,
                ('72', 'Invalid/Missing Subscriber/Insured ID'))
        self.assertEqual(rejection.follow_up_action_code,
                ('N', 'Resubmission Not Allowed'))

    def test_trace_numbers(self):
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
        _test(0, ("1", "Current Transaction Trace Numbers"),
                 "222222222", "9ZIRMEDCOM", "ELR ID")
        _test(1, ("2",
                "Referenced Transaction Trace Numbers (Value from 270)"),
                "333333333", "9ZIRMEDCOM", "ELI ID")
        _test(2, ("1", "Current Transaction Trace Numbers"),
                "4444444444", "9MEDDATACO", "")

        dependent = subscriber.dependents[0]
        self.assertEqual(len(dependent.trace_numbers), 3)
        _test(0, ("1", "Current Transaction Trace Numbers"),
                 "222222222", "9ZIRMEDCOM", "ELR ID")
        _test(1, ("2",
                "Referenced Transaction Trace Numbers (Value from 270)"),
                "333333333", "9ZIRMEDCOM", "ELI ID")
        _test(2, ("1", "Current Transaction Trace Numbers"),
                "4444444444", "9MEDDATACO", "")

    def test_subscriber_name(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        name = subscriber.subscriber_information.name
        self.assertEqual(name.entity_identifier,
                ("IL", "Insured"))
        self.assertEqual(name.entity_type,
                ("1", "Person"))
        self.assertEqual(name.id_code, "R11111111")
        self.assertEqual(name.id_code_qual,
                ("MI", "Member Identification Number"))
        self.assertTrue(name.is_person)
        self.assertFalse(name.is_organization)

    def test_dependent_name(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        name = subscriber.dependents[0].dependent_information.name
        self.assertEqual(name.entity_identifier,
                ("03", "Dependent"))
        self.assertEqual(name.entity_type,
                ("1", "Person"))
        self.assertEqual(name.first_name, "JANE")
        self.assertEqual(name.last_name, "DOE")
        self.assertEqual(name.id_code, "")
        self.assertTrue(name.is_person)
        self.assertFalse(name.is_organization)

    def test_subscriber_dates(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        self.assertEqual(len(subscriber.subscriber_information.dates), 0)

    def test_dependent_dates(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        dependent = subscriber.dependents[0]
        self.assertEqual(len(dependent.dependent_information.dates), 0)

    def test_subscriber_demographic_information(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        demo = subscriber.subscriber_information.demographic_information
        self.assertEqual(demo, None)

    def test_dependent_demographic_information(self):
        dependents = self.f.facades[0].source.receivers[0].subscribers[0].\
                dependents
        self.assertEqual(len(dependents), 1)
        demo = dependents[0].dependent_information.demographic_information
        self.assertEqual(demo.birth_date, datetime.date(1981, 8, 10))

    def test_subscriber_eligibility_information(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        self.assertEqual(len(subscriber.eligibility_or_benefit_information), 0)

    def test_dependent_eligibility_information(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        dependent = subscriber.dependents[0]
        self.assertEqual(len(dependent.eligibility_or_benefit_information), 0)

if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
