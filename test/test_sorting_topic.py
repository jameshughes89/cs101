import unittest

from src.sorting_topic import selection_sort


class SortingTopicTest(unittest.TestCase):
    def test_selection_sort_empty_list_returns_empty_list(self):
        self.assertEqual([], selection_sort([]))

    def test_selection_sort_all_unique_values_returns_sorted_list(self):
        case = [3, 6, 4, 8, 7, 9, 0, 1, 2, 5]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, selection_sort(case))

    def test_selection_sort_duplicate_values_returns_sorted_list(self):
        case = [8, 4, 3, 9, 4, 1, 5, 3, 2, 1, 5, 8, 9, 7, 6, 7, 0, 6, 0, 2]
        expected = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        self.assertEqual(expected, selection_sort(case))

    def test_selection_sort_all_equal_values_returns_equal_list(self):
        case = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected = case[:]
        self.assertEqual(expected, selection_sort(case))

    def test_selection_sort_all_already_sorted_returns_equal_list(self):
        case = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = case[:]
        self.assertEqual(expected, selection_sort(case))

    def test_selection_sort_reverse_order_returns_sorted_list(self):
        case = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, selection_sort(case))
