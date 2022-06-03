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



