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


if __name__ == "__main__":
    unittest.main()
