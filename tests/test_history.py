# -*- coding: utf-8 -*-
# vim: set et sw=4 ts=4:

import unittest
from decimal import Decimal

from covwap_online import HistoryVWAP

class TestHistory(unittest.TestCase):

    def setUp(self):
        self.capacity = 10
        self.name = "TEST"

    def test_append_simple(self):
        history = HistoryVWAP(self.name, self.capacity)
        for x in range(1, 10):
            history.append(x, Decimal(x), Decimal(x))

    def test_append_seq(self):
        history = HistoryVWAP(self.name, self.capacity)

        with self.assertRaises(Exception):
            history.append(0, Decimal('1'), 1)

        with self.assertRaises(Exception):
            for x in range(0, 9):
                history.append(1, x, x)

        with self.assertRaises(Exception):
            history.append(-1, Decimal('1'), 1)

    def test_append_types(self):
        history = HistoryVWAP(self.name, self.capacity)

        history.append(1, Decimal('1'), Decimal('1'))

        with self.assertRaises(Exception):
            history.append(2, 1, Decimal('1'))

        with self.assertRaises(Exception):
            history.append(3, Decimal('1'), 1)

        with self.assertRaises(Exception):
            history.append(4, Decimal('1'), 1.2)

        with self.assertRaises(Exception):
            history.append(5, 1.2, Decimal('1'))

        with self.assertRaises(Exception):
            history.append(6, None, Decimal('1'))

        with self.assertRaises(Exception):
            history.append(7, Decimal('1'), None)

        with self.assertRaises(Exception):
            history.append(None, Decimal('1'), Decimal('1'))

    def test_append_capacity(self):
        history = HistoryVWAP(self.name, self.capacity)

        for x in range(1, 100):
            history.append(x, Decimal(x), Decimal(x))

        self.assertEqual(10, len(history))

    def test_result_basic(self):
        history = HistoryVWAP(self.name, self.capacity)

        for x in range(1, 3):
            history.append(x, Decimal(x), Decimal(x))

        self.assertEqual((False, 2,), history.result)

        for x in range(4, 5):
            history.append(x, Decimal(x), Decimal(x))

        self.assertEqual((False, 3,), history.result)

        for x in range(5, 20):
            history.append(x, Decimal(x), Decimal(x))

        self.assertEqual((True, Decimal('15.06896551724137931034482759'),), history.result)

    def test_result_force_basic(self):
        history = HistoryVWAP(self.name, self.capacity)

        for x in range(1, 3):
            history.append(x, Decimal(x), Decimal(x))

        self.assertEqual(Decimal('1.666666666666666666666666667'), history.result_force)

        for x in range(4, 5):
            history.append(x, Decimal(x), Decimal(x))

        self.assertEqual(Decimal('3'), history.result_force)

        for x in range(5, 20):
            history.append(x, Decimal(x), Decimal(x))

        self.assertEqual(Decimal('15.06896551724137931034482759'), history.result_force)
