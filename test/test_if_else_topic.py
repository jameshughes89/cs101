import unittest

from src.if_else_topic import (
    hail,
    is_negative,
    is_negative_version_2,
    letter_grade,
    smush,
    smush_version_2,
    smush_version_3,
    three_five_divisible,
)


class IfElseTopicTest(unittest.TestCase):
    def test_smush_positive_parameter_returns_half(self):
        self.assertEqual(5, smush(10))

    def test_smush_negative_parameter_returns_parameter(self):
        self.assertEqual(-10, smush(-10))

    def test_smush_zero_parameter_returns_zero(self):
        self.assertEqual(0, smush(0))

    def test_smush_version_2_positive_parameter_returns_half(self):
        self.assertEqual(5, smush_version_2(10))

    def test_smush_version_2_negative_parameter_returns_parameter(self):
        self.assertEqual(-10, smush_version_2(-10))

    def test_smush_version_2_zero_parameter_returns_zero(self):
        self.assertEqual(0, smush_version_2(0))

    def test_smush_version_3_positive_parameter_returns_half(self):
        self.assertEqual(5, smush_version_3(10))

    def test_smush_version_3_negative_parameter_returns_parameter(self):
        self.assertEqual(-10, smush_version_3(-10))

    def test_smush_version_3_zero_parameter_returns_zero(self):
        self.assertEqual(0, smush_version_3(0))

    def test_is_negative_positive_parameter_returns_False(self):
        self.assertFalse(is_negative(10))

    def test_is_negative_negative_parameter_returns_True(self):
        self.assertTrue(is_negative(-10))

    def test_is_negative_zero_parameter_returns_False(self):
        self.assertFalse(is_negative(0))

    def test_is_negative_version_2_positive_parameter_returns_False(self):
        self.assertFalse(is_negative_version_2(10))

    def test_is_negative_version_2_negative_parameter_returns_True(self):
        self.assertTrue(is_negative_version_2(-10))

    def test_is_negative_version_2_zero_parameter_returns_False(self):
        self.assertFalse(is_negative_version_2(0))

    def test_three_five_divisible_zero_parameter_returns_correct_string(self):
        self.assertEqual("It is!", three_five_divisible(0))

    def test_three_five_divisible_fifteen_parameter_returns_correct_string(self):
        self.assertEqual("It is!", three_five_divisible(15))

    def test_three_five_divisible_negative_thirty_parameter_returns_correct_string(self):
        self.assertEqual("It is!", three_five_divisible(-30))

    def test_three_five_divisible_three_parameter_returns_correct_string(self):
        self.assertEqual("Nope", three_five_divisible(3))

    def test_three_five_divisible_negative_fifty_parameter_returns_correct_string(self):
        self.assertEqual("Nope", three_five_divisible(-50))

    def test_three_five_divisible_one_parameter_returns_correct_string(self):
        self.assertEqual("Nope", three_five_divisible(1))

    def test_hail_zero_parameter_returns_zero(self):
        self.assertEqual(0, hail(0))

    def test_hail_even_parameter_returns_half(self):
        self.assertEqual(1, hail(2))

    def test_hail_odd_parameter_returns_times_three_plus_one(self):
        self.assertEqual(4, hail(1))

    def test_hail_negative_odd_parameter_returns_times_three_plus_one(self):
        self.assertEqual(-14, hail(-5))

    def test_letter_grade_90_returns_A_plus(self):
        self.assertEqual("A+", letter_grade(90))

    def test_letter_grade_80_returns_A(self):
        self.assertEqual("A", letter_grade(80))

    def test_letter_grade_70_returns_B(self):
        self.assertEqual("B", letter_grade(70))

    def test_letter_grade_60_returns_C(self):
        self.assertEqual("C", letter_grade(60))

    def test_letter_grade_50_returns_D(self):
        self.assertEqual("D", letter_grade(50))

    def test_letter_grade_49_returns_F(self):
        self.assertEqual("F", letter_grade(49))
