import unittest

from src.point3d import Point3D


class Point3DTest(unittest.TestCase):
    def test_point_0_0_0_has_x_0(self):
        point = Point3D(0, 0, 0)
        self.assertEqual(0, point.x)

    def test_point_0_0_0_has_y_0(self):
        point = Point3D(0, 0, 0)
        self.assertEqual(0, point.y)

    def test_point_0_0_0_has_z_0(self):
        point = Point3D(0, 0, 0)
        self.assertEqual(0, point.z)

    def test_distance_from_point_various_points_returns_correct_distance(self):
        cases = [
            (Point3D(1, 1, 1), Point3D(1, 1, 1)),
            (Point3D(1, 1, 1), Point3D(2, 2, 2)),
            (Point3D(1, 1, 1), Point3D(-2, -2, -2)),
            (Point3D(-1, 1, 4), Point3D(-2, -3, -4)),
        ]
        expecteds = [0, 1.732051, 5.196152, 9]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case[0].distance_from_point(case[1]), 5)

    def test_equals_on_equal_points_returns_true(self):
        point_a = Point3D(1, 1, 1)
        point_b = Point3D(1, 1, 1)
        self.assertTrue(point_a == point_b)

    def test_equals_on_not_equal_points_returns_false(self):
        point_a = Point3D(1, 1, 1)
        point_b = Point3D(-1, -1, -1)
        self.assertFalse(point_a == point_b)

    def test_equal_on_point_and_string_returns_false(self):
        point = Point3D(1, -1, 1)
        self.assertFalse("Point3D(1, -1, 1)" == point)

    def test_repr_arbitrary_point_returns_correct_string(self):
        point = Point3D(1, -1, 1)
        self.assertEqual("Point3D(1, -1, 1)", str(point))
