import unittest

from src.functions_topic import *


class TestFunctionsTopic(unittest.TestCase):

    def test_concatenate_strings_empty_strings_returns_empty_string(self):
        self.assertEqual("", concatenate_strings("", ""))

    def test_concatenate_strings_returns_contatenated_strings(self):
        self.assertEqual("ab", concatenate_strings("a", "b"))

    def test_criss_cross_concatenation_empty_strings_returns_empty_string(self):
        self.assertEqual("", criss_cross_concatenation("", "", "", ""))

    def test_criss_cross_concatenation_returns_contatenated_strings_in_correct_order(self):
        self.assertEqual("acbd", criss_cross_concatenation("a", "b", "c", "d"))
