import unittest

from src.if_else_topic import is_negative, is_negative_version_2, smush, letter_grade


class TestIfElseTopic(unittest.TestCase):
    def test_smush_positive_parameter_returns_half(self):
        self.assertEqual(5, smush(10))

    def test_smush_negative_parameter_returns_parameter(self):
        self.assertEqual(-10, smush(-10))

    def test_smush_zero_parameter_returns_zero(self):
        self.assertEqual(0, smush(0))

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
