import unittest

from src.point import Point


class TestPoint(unittest.TestCase):
    def test_point_0_0_has_x_0(self):
        point = Point(0, 0)
        self.assertEqual(0, point.x)

    def test_point_0_0_has_y_0(self):
        point = Point(0, 0)
        self.assertEqual(0, point.y)

    def test_update_point_x_has_updated_x(self):
        point = Point(0, 0)
        point.x = -1
        self.assertEqual(-1, point.x)

    def test_update_point_y_has_updated_y(self):
        point = Point(0, 0)
        point.y = -1
        self.assertEqual(-1, point.y)

    def test_distance_from_origin_returns_correct_distance(self):
        cases = [Point(0, 0), Point(1, 1), Point(-1, 2), Point(-1, -3), Point(-1, -4)]
        expected = [0, 1.41421, 2.23607, 3.16228, 4.12311]
        for (case, expect) in zip(cases, expected):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case.distance_from_origin(), 5)

    def test_distance_from_arbitrary_point_point_to_equal_point_returns_0(self):
        point_from = Point(1, 1)
        point_to = Point(1, 1)
        self.assertEqual(0, point_from.distance_from_point(point_to))

    def test_distance_from_point_arbitrary_point_to_arbitrary_point_same_quadrant_returns_correct_distance(self):
        point_from = Point(1, 1)
        point_to = Point(3, 3)
        self.assertAlmostEqual(2.82842712475, point_from.distance_from_point(point_to))

    def test_distance_from_point_arbitrary_point_to_arbitrary_point_across_quadrants_returns_correct_distance(self):
        point_from = Point(1, 1)
        point_to = Point(-1, -1)
        self.assertAlmostEqual(2.82842712475, point_from.distance_from_point(point_to))

    def test_find_midpoint_between_arbitrary_point_and_arbitrary_point_same_quadrant_returns_correct_point(self):
        point_from = Point(1, 1)
        point_to = Point(3, 3)
        self.assertEqual(Point(2, 2), point_from.find_midpoint(point_to))

    def test_find_midpoint_between_arbitrary_point_and_arbitrary_point_across_quadrants_returns_correct_point(self):
        point_from = Point(1, 1)
        point_to = Point(-2, -2)
        self.assertEqual(Point(-0.5, -0.5), point_from.find_midpoint(point_to))

    def test_find_midpoint_between_arbitrary_point_and_equal_point_returns_equal_point(self):
        point_from = Point(1, -1)
        point_to = Point(1, -1)
        self.assertEqual(Point(1, -1), point_from.find_midpoint(point_to))

    def test_equals_on_equal_points_returns_true(self):
        point_a = Point(1, 1)
        point_b = Point(1, 1)
        self.assertTrue(point_a == point_b)

    def test_equals_on_not_equal_points_returns_false(self):
        point_a = Point(1, 1)
        point_b = Point(-1, -1)
        self.assertFalse(point_a == point_b)

    def test_equal_on_point_and_string_returns_false(self):
        point = Point(1, -1)
        self.assertFalse("Point(1, -1)" == point)

    def test_repr_arbitrary_point_returns_correct_string(self):
        point = Point(1, -1)
        self.assertEqual("Point(1, -1)", str(point))
