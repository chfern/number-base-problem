import unittest

from problem.number_base.app import to_base
from problem.number_base.app import to_base10
from problem.number_base.app import mod


class TestNumberBase(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(mod(235, 10), 5)
        self.assertEqual(mod(235, 8), 3)
        self.assertEqual(mod(-21, 20), -1)

    def test_convert_positive_int_to_base10(self):
        self.assertEqual(to_base10(235, 2), 19)
        self.assertEqual(to_base10(235, 3), 32)
        self.assertEqual(to_base10(235, 4), 49)
        self.assertEqual(to_base10(235, 5), 70)
        self.assertEqual(to_base10(235, 6), 95)
        self.assertEqual(to_base10(235, 7), 124)
        self.assertEqual(to_base10(235, 8), 157)
        self.assertEqual(to_base10(235, 9), 194)
        self.assertEqual(to_base10(235, 10), 235)
        self.assertEqual(to_base10(235, 11), 280)

    def test_convert_non_positive_int_to_base10(self):
        self.assertEqual(to_base10(-235, 2), -19)
        self.assertEqual(to_base10(-235, 3), -32)
        self.assertEqual(to_base10(-235, 4), -49)
        self.assertEqual(to_base10(-235, 5), -70)
        self.assertEqual(to_base10(-235, 6), -95)
        self.assertEqual(to_base10(-235, 7), -124)
        self.assertEqual(to_base10(-235, 8), -157)
        self.assertEqual(to_base10(-235, 9), -194)
        self.assertEqual(to_base10(-235, 10), -235)
        self.assertEqual(to_base10(-235, 11), -280)

    def test_convert_positive_int_to_any_base(self):
        self.assertEqual(to_base(235, 2, 8), 23)
        self.assertEqual(to_base(235, 8, 2), 10011101)
        self.assertEqual(to_base(235, 4, 12), 41)
        self.assertEqual(to_base(235, 12, 4), 11021)
        self.assertEqual(to_base(235, 6, 13), 74)
        self.assertEqual(to_base(235, 13, 6), 1434)

    def test_convert_non_positive_int_to_any_base(self):
        self.assertEqual(to_base(-235, 2, 8), -23)
        self.assertEqual(to_base(-235, 8, 2), -10011101)
        self.assertEqual(to_base(-235, 4, 12), -41)
        self.assertEqual(to_base(-235, 12, 4), -11021)
        self.assertEqual(to_base(-235, 6, 13), -74)
        self.assertEqual(to_base(-235, 13, 6), -1434)
