import unittest

from converter import float_to_string_converter


class TestConverterFloatToString(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(float_to_string_converter(2000.0), "2 000")

    def test_positive_float(self):
        self.assertEqual(float_to_string_converter(2000.22), "2 000.22")

    def test_negative_integer(self):
        self.assertEqual(float_to_string_converter(-2000.0), "-2 000")

    def test_negative_float(self):
        self.assertEqual(float_to_string_converter(-2000.22), "-2 000.22")

    def test_zero(self):
        self.assertEqual(float_to_string_converter(0.0), "0")

    def test_small_float(self):
        self.assertEqual(float_to_string_converter(0.0000000000012), "1.2e-12")

    def test_large_float(self):
        self.assertEqual(float_to_string_converter(875867843675.55533), "875 867 843 675.5553")

    def test_inf(self):
        self.assertEqual(float_to_string_converter(float("inf")), "inf")

    def test_negative_inf(self):
        self.assertEqual(float_to_string_converter(float("-inf")), "-inf")

    def test_nan(self):
        self.assertEqual(float_to_string_converter(float("NaN")), "NaN")

    def test_test(self):
        self.assertEqual(float_to_string_converter(0.1 + 0.2), "0.3")


if __name__ == "__main__":
    unittest.main()
