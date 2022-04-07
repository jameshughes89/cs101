import unittest

from src.functions_topic import (
    celsius_to_fahrenheit,
    concatenate_strings,
    criss_cross_concatenation,
    square_of_sum,
)


class TestFunctionsTopic(unittest.TestCase):
    def test_celsius_to_fahrenheit_positive_celsius_values_returns_correct_fahrenheit_value(self):
        expected = 104
        actual = celsius_to_fahrenheit(40)
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_celsius_to_fahrenheit_negative_celsius_values_returns_correct_fahrenheit_value(self):
        expected = -40
        actual = celsius_to_fahrenheit(-40)
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_celsius_to_fahrenheit_float_celsius_values_returns_correct_fahrenheit_value(self):
        expected = 89.96
        actual = celsius_to_fahrenheit(32.2)
        self.assertAlmostEqual(expected, actual, 3, f"Expected {expected} but was {actual}.")

    def test_square_of_sum_positive_values_returns_correct_value(self):
        expected = 16
        actual = square_of_sum(2, 2)
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_square_of_sum_negative_values_returns_correct_value(self):
        expected = 16
        actual = square_of_sum(-2, -2)
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_square_of_sum_mixed_sign_values_returns_correct_value(self):
        expected = 0
        actual = square_of_sum(2, -2)
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_square_of_sum_float_values_returns_correct_value(self):
        expected = 19.36
        actual = square_of_sum(2.2, 2.2)
        self.assertAlmostEqual(expected, actual, 4, f"Expected {expected} but was {actual}.")

    def test_concatenate_strings_empty_strings_returns_empty_string(self):
        expected = ""
        actual = concatenate_strings("", "")
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_concatenate_strings_returns_contatenated_strings(self):
        expected = "ab"
        actual = concatenate_strings("a", "b")
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_criss_cross_concatenation_empty_strings_returns_empty_string(self):
        expected = ""
        actual = criss_cross_concatenation("", "", "", "")
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")

    def test_criss_cross_concatenation_returns_contatenated_strings_in_correct_order(self):
        expected = "acbd"
        actual = criss_cross_concatenation("a", "b", "c", "d")
        self.assertEqual(expected, actual, f"Expected {expected} but was {actual}.")
