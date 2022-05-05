import unittest

from src.lists_topic import contains_while, index_of_for


class TestListsTopic(unittest.TestCase):
    def test_contains_while_search_in_empty_list_returns_false(self):
        self.assertFalse(contains_while("a", []))

    def test_contains_while_search_for_empty_list_in_empty_list_returns_false(self):
        self.assertFalse(contains_while([], []))

    def test_contains_while_search_for_no_matching_element_in_list_returns_false(self):
        self.assertFalse(contains_while("b", ["a", 1, 2.0, False]))

    def test_contains_while_search_for_matching_first_element_in_list_returns_true(self):
        self.assertTrue(contains_while("a", ["a", 1, 2.0, False]))

    def test_contains_while_search_for_matching_last_element_in_list_returns_true(self):
        self.assertTrue(contains_while(False, ["a", 1, 2.0, False]))

    def test_index_of_for_search_in_empty_list_returns_negative_1(self):
        self.assertEqual(-1, index_of_for("a", []))

    def test_index_of_for_search_for_empty_list_in_empty_list_returns_negative_1(self):
        self.assertEqual(-1, index_of_for([], []))

    def test_index_of_for_search_for_no_matching_element_in_list_returns_negative_1(self):
        self.assertEqual(-1, index_of_for("b", ["a", 1, 2.0, False]))

    def test_index_of_for_search_for_matching_first_element_in_list_returns_0(self):
        self.assertEqual(0, index_of_for("a", ["a", 1, 2.0, False]))

    def test_index_of_for_search_for_matching_last_element_in_list_returns_last_index(self):
        self.assertEqual(3, index_of_for(False, ["a", 1, 2.0, False]))

    def test_index_of_for_search_for_duplicate_matching_elements_returns_index_of_first_occurrence(self):
        self.assertEqual(1, index_of_for(1, ["a", 1, 1, 2.0, False]))
