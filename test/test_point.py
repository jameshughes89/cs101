import unittest

from src.point3d import Point3D


class TestPoint(unittest.TestCase):
    def test_point_0_0_0_has_x_0(self):
        point = Point3D(0, 0, 0)
        self.assertEqual(0, point.x)

    def test_point_0_0_0_has_y_0(self):
        point = Point3D(0, 0, 0)
        self.assertEqual(0, point.y)

    def test_point_0_0_0_has_z_0(self):
        point = Point3D(0, 0, 0)
        self.assertEqual(0, point.z)

    def test_update_point_x_has_updated_x(self):
        point = Point3D(0, 0, 0)
        point.x = -1
        self.assertEqual(-1, point.x)

    def test_update_point_y_has_updated_y(self):
        point = Point3D(0, 0, 0)
        point.y = -1
        self.assertEqual(-1, point.y)

    def test_update_point_z_has_updated_y(self):
        point = Point3D(0, 0, 0)
        point.z = -1
        self.assertEqual(-1, point.z)

    def test_distance_from_origin_various_points_returns_correct_distance(self):
        cases = [Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(-1, 2, 1), Point3D(-1, -3, -1), Point3D(-1, -4, 2)]
        expecteds = [0, 1.732051, 2.44949, 3.316625, 4.582576]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case.distance_from_origin(), 5)

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

    def test_find_midpoint_various_points_returns_correct_point(self):
        cases = [
            (Point3D(1, 1, 1), Point3D(1, 1, 1)),
            (Point3D(1, 1, 1), Point3D(2, 2, 2)),
            (Point3D(1, 1, 1), Point3D(-2, -2, -2)),
            (Point3D(-1, 1, 4), Point3D(-2, -3, -4)),
        ]
        expecteds = [Point3D(1, 1, 1), Point3D(1.5, 1.5, 1.5), Point3D(-0.5, -0.5, -0.5), Point3D(-1.5, -1, 0)]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertEqual(expect, case[0].find_midpoint(case[1]))

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
        self.assertFalse("Point(1, -1, 1)" == point)

    def test_repr_arbitrary_point_returns_correct_string(self):
        point = Point3D(1, -1, 1)
        self.assertEqual("Point(1, -1, 1)", str(point))
