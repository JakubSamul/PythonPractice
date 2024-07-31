import unittest

from converter import float_to_string_converter


class TestConverterFloatToString(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(float_to_string_converter(2000.0), "2 000")


if __name__ == "__main__":
    unittest.main()
