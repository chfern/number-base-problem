import unittest


def mod(num, denominator):
    return num - (denominator * int(num/denominator))


def to_base10(num, base):
    result = 0
    power = 0

    while num != 0:
        result += (mod(num, 10)) * pow(base, power)
        num -= (mod(num, 10))
        num = int(num / 10)
        power += 1

    return result


def to_base(num, from_base, to_base):
    num_to_divide = to_base10(num, from_base)

    power = 0
    result = 0
    while num_to_divide != 0:
        remainder = mod(num_to_divide, to_base)
        result += remainder * pow(10, power)
        power += 1
        num_to_divide = int(num_to_divide / to_base)

    return result


class TestBaseConverter(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
