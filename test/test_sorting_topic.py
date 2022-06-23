import unittest

from src.sorting_topic import selection_sort


class SortingTopicTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
            [],  # Empty
            [3, 6, 4, 8, 7, 9, 0, 1, 2, 5],  # Unsorted Unique
            [8, 4, 3, 9, 4, 1, 5, 3, 2, 1, 5, 8, 9, 7, 6, 7, 0, 6, 0, 2],  # Unsorted Duplicates
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # All Equal
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  # Already Sorted
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],  # Reverse Order
        ]
        self.expecteds = [
            [],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        ]

    def test_selection_sort_multiple_cases_returns_sorted_list(self):
        for case, expect in zip(self.cases, self.expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertEqual(expect, selection_sort(case))
