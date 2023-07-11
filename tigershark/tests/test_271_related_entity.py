import unittest
import logging
import sys
import datetime

from tigershark.facade import f271
from tigershark.parsers import M271_4010_X092_A1


class TestParsed271(unittest.TestCase):
    def setUp(self):
        m = M271_4010_X092_A1.parsed_271
        with open('tests/271-related-entity.txt') as f:
            parsed = m.unmarshall(f.read().strip())
        self.f = f271.F271_4010(parsed)

    def test_number_of_facades(self):
        self.assertEqual(len(self.f.facades), 1)

    def test_header(self):
        h = self.f.facades[0].header.hierarchical_transaction_info
        self.assertEqual(h.structure, ("0022", "Information Source, "
                "Information Receiver, Subscriber, or Dependent."))
        self.assertEqual(h.purpose, ("11", "Response"))
        self.assertEqual(h.transaction_id, "11111")
        self.assertEqual(h.creation_date, datetime.date(2012, 9, 27))
        self.assertEqual(h.creation_time, datetime.time(14, 3, 33))

    def test_number_of_receivers(self):
        self.assertEqual(len(self.f.facades[0].source.receivers), 1)

    def test_number_of_subscribers(self):
        self.assertEqual(
                len(self.f.facades[0].source.receivers[0].subscribers), 1)

    def test_number_of_dependents(self):
        self.assertEqual(len(
            self.f.facades[0].source.receivers[0].subscribers[0].dependents),
            1)

    def test_subscriber_related_entity(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        for eb in subscriber.eligibility_or_benefit_information:
            self.assertEqual(eb.benefit_related_entity, None)

    def test_dependent_related_entity(self):
        subscriber = self.f.facades[0].source.receivers[0].subscribers[0]
        dependent = subscriber.dependents[0]
        self.assertEqual(
                len(dependent.eligibility_or_benefit_information), 14)
        eb = dependent.eligibility_or_benefit_information[11]
        ebr = eb.benefit_related_entity
        self.assertNotEqual(ebr, None)
        self.assertEqual(ebr.name, None)
        self.assertNotEqual(ebr.address_street, None)
        self.assertEqual(ebr.address_street.addr1, "123 RELATED ST # 1")
        self.assertEqual(ebr.address_location.city, "ANYTOWN")
        self.assertEqual(ebr.address_location.state, "CA")
        self.assertEqual(ebr.address_location.zip, "902101234")
        self.assertEqual(len(ebr.contact_information), 1)
        self.assertEqual(ebr.contact_information[0].contact_phone,
                "8005554160")

        eb = dependent.eligibility_or_benefit_information[12]
        ebr = eb.benefit_related_entity
        self.assertNotEqual(ebr, None)
        self.assertNotEqual(ebr.name, None)
        self.assertNotEqual(ebr.address_street, None)
        self.assertEqual(ebr.name.org_name, "EMPLOYER")
        self.assertEqual(ebr.address_street.addr1, "123 RELATED ST # 2")
        self.assertEqual(ebr.address_location.city, "ANYTOWN")
        self.assertEqual(ebr.address_location.state, "WA")
        self.assertEqual(ebr.address_location.zip, "98101")
        self.assertEqual(len(ebr.contact_information), 1)
        self.assertEqual(ebr.contact_information[0].contact_phone,
                "2065551234")


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
