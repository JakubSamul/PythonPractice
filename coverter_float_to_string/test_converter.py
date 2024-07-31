import unittest

from converter import float_to_string_converter


class TestConverterFloatToString(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(float_to_string_converter(2000.0), "2 000")

    def test_positive_float(self):
        self.assertEqual(float_to_string_converter(2000.22), "2 000.22")

    def test_negative_iteger(self):
        self.assertEqual(float_to_string_converter(-2000.0), "-2 000")

    def test_negative_float(self):
        self.assertEqual(float_to_string_converter(-2000.22), "-2 000.22")

    def test_zero(self):
        self.assertEqual(float_to_string_converter(0.0), "0")

    def test_small_float(self):
        self.assertEqual(float_to_string_converter(0.0000000000012), "0.00")

    def test_large_float(self):
        self.assertEqual(float_to_string_converter(8475838847488221.437), "8 475 838 847 488 221.44")

    def test_inf(self):
        self.assertEqual(float_to_string_converter(float("inf")), "inf")

    def test_negative_inf(self):
        self.assertEqual(float_to_string_converter(float("-inf")), "-inf")


if __name__ == "__main__":
    unittest.main()
