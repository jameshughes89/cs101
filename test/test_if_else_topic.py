import unittest

from if_else_topic import is_negative, is_negative_version_2, smush


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
