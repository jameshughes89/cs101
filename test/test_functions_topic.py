import unittest

from src.functions_topic import (
    celsius_to_fahrenheit,
    concatenate_strings,
    criss_cross_concatenation,
    square_of_sum,
)


class FunctionsTopicTest(unittest.TestCase):
    def test_celsius_to_fahrenheit_positive_celsius_values_returns_correct_fahrenheit_value(self):
        self.assertEqual(104, celsius_to_fahrenheit(40))

    def test_celsius_to_fahrenheit_negative_celsius_values_returns_correct_fahrenheit_value(self):
        self.assertEqual(-40, celsius_to_fahrenheit(-40))

    def test_celsius_to_fahrenheit_float_celsius_values_returns_correct_fahrenheit_value(self):
        self.assertAlmostEqual(89.96, celsius_to_fahrenheit(32.2), 3)

    def test_square_of_sum_positive_values_returns_correct_value(self):
        self.assertEqual(16, square_of_sum(2, 2))

    def test_square_of_sum_negative_values_returns_correct_value(self):
        self.assertEqual(16, square_of_sum(-2, -2))

    def test_square_of_sum_mixed_sign_values_returns_correct_value(self):
        self.assertEqual(0, square_of_sum(2, -2))

    def test_square_of_sum_float_values_returns_correct_value(self):
        self.assertAlmostEqual(19.36, square_of_sum(2.2, 2.2), 4)

    def test_concatenate_strings_empty_strings_returns_empty_string(self):
        self.assertEqual("", concatenate_strings("", ""))

    def test_concatenate_strings_returns_contatenated_strings(self):
        self.assertEqual("ab", concatenate_strings("a", "b"))

    def test_criss_cross_concatenation_empty_strings_returns_empty_string(self):
        self.assertEqual("", criss_cross_concatenation("", "", "", ""))

    def test_criss_cross_concatenation_returns_contatenated_strings_in_correct_order(self):
        self.assertEqual("acbd", criss_cross_concatenation("a", "b", "c", "d"))
