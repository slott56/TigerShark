import unittest
import logging
import sys
import datetime

from tigershark.facade import f271
from tigershark.parsers import M271_4010_X092_A1


class TestParsed271(unittest.TestCase):
    def setUp(self):
        m = M271_4010_X092_A1.parsed_271
        with open('271-example.txt') as f:
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
        self.assertEqual(h.creation_date, datetime.date(2012, 06, 05))
        self.assertEqual(h.creation_time, datetime.time(23, 24, 23))

    def test_number_of_receivers(self):
        self.assertEqual(len(self.f.facades[0].source.receivers), 1)

    def test_number_of_subscribers(self):
        self.assertEqual(
                len(self.f.facades[0].source.receivers[0].subscribers), 1)

    def test_hierarchy(self):
        source = self.f.facades[0].source
        self.assertEqual(source.id, "1")
        self.assertEqual(source.parent_id, '')
        self.assertEqual(source.level, ("20", "Information Source"))
        self.assertTrue(source.has_children)

        receiver = source.receivers[0]
        self.assertEqual(receiver.id, "2")
        self.assertEqual(receiver.parent_id, '1')
        self.assertEqual(receiver.level, ("21", "Information Receiver"))
        self.assertTrue(receiver.has_children)

        subscriber = receiver.subscribers[0]
        self.assertEqual(subscriber.id, "3")
        self.assertEqual(subscriber.parent_id, '2')
        self.assertEqual(subscriber.level, ("22", "Subscriber"))
        self.assertFalse(subscriber.has_children)


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
    )
    unittest.main()
