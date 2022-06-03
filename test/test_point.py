import unittest

from src.point import Point


class TestCircle(unittest.TestCase):

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

    def test_distance_from_origin_of_point_0_0_returns_0(self):
        point = Point(0, 0)
        self.assertEqual(0, point.distance_from_origin())

    def test_distance_from_origin_of_arbitrary_point_returns_correct_distance(self):
        point = Point(1, 1)
        self.assertAlmostEqual(1.41421356237, point.distance_from_origin())

    def test_distance_from_point_from_point_to_same_point_returns_0(self):
        point_from = Point(1, 1)
        point_to = Point(1, 1)
        self.assertEqual(0, point_from.distance_from_point(point_to))

    def test_distance_from_point_from_arbitrary_point_to_arbitrary_point_returns_correct_distance(self):
        point_from = Point(1, 1)
        point_to = Point(-1, -1)
        self.assertAlmostEqual(2.82842712475, point_from.distance_from_point(point_to))



