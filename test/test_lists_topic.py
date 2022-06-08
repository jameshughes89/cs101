import unittest

from src.lists_topic import contains_while, index_of_for, my_sum


class ListsTopicTest(unittest.TestCase):
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

    def test_my_sum_empty_list_returns_0(self):
        self.assertEqual(0, my_sum([]))

    def test_my_sum_single_element_returns_value_of_element(self):
        self.assertEqual(1, my_sum([1]))

    def test_my_sum_positive_and_negative_values_returns_correct_sum(self):
        self.assertEqual(0, my_sum([1, -1]))

    def test_my_sum_arbitrary_list_returns_correct_sum(self):
        self.assertEqual(15, my_sum([0, 1, 2, 3, 4, 5]))
