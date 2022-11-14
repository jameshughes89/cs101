import unittest

from src.point3d import Point3D
from src.sphere import Sphere


class SphereTest(unittest.TestCase):
    def test_sphere_centre_point_returns_correct_point3D(self):
        sphere = Sphere(Point3D(0, 0, 0), 1)
        self.assertEqual(Point3D(0, 0, 0), sphere.centre_point)

    def test_sphere_radius_returns_correct_radius(self):
        sphere = Sphere(Point3D(0, 0, 0), 1)
        self.assertEqual(1, sphere.radius)

    def test_diameter_various_spheres_returns_correct_diameter(self):
        cases = [
            Sphere(Point3D(0, 0, 0), 0),
            Sphere(Point3D(0, 0, 0), 1),
            Sphere(Point3D(1, 1, 1), 0),
            Sphere(Point3D(10, 11, 12), 10.1),
        ]
        expecteds = [0, 2, 0, 20.2]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case.diameter(), 5)

    def test_surface_area_various_spheres_returns_correct_surface_area(self):
        cases = [
            Sphere(Point3D(0, 0, 0), 0),
            Sphere(Point3D(0, 0, 0), 1),
            Sphere(Point3D(1, 1, 1), 0),
            Sphere(Point3D(10, 11, 12), 10),
        ]
        expecteds = [0, 12.56637, 0, 1256.63706]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case.surface_area(), 5)

    def test_volume_various_spheres_returns_correct_volume(self):
        cases = [
            Sphere(Point3D(0, 0, 0), 0),
            Sphere(Point3D(0, 0, 0), 1),
            Sphere(Point3D(1, 1, 1), 0),
            Sphere(Point3D(10, 11, 12), 10),
        ]
        expecteds = [0, 4.18879, 0, 4188.7902]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case.volume(), 5)

    def test_distance_between_centres_various_spheres_returns_correct_distance(self):
        cases = [
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(0, 0, 0), 1)),
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(1, 1, 1), 1)),
            (Sphere(Point3D(1, 1, 1), 1), Sphere(Point3D(1, 1, 1), 10)),
            (Sphere(Point3D(-1, -1, -1), 1), Sphere(Point3D(1, 1, 1), 10)),
        ]
        expecteds = [0, 1.732051, 0, 3.464102]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case[0].distance_between_centres(case[1]), 5)

    def test_distance_between_edges_various_spheres_returns_correct_distance(self):
        cases = [
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(0, 0, 0), 1)),
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(1, 1, 1), 1)),
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(10, 10, 10), 1)),
            (Sphere(Point3D(-1, -1, -1), 1), Sphere(Point3D(10, 10, 10), 10)),
        ]
        expecteds = [-2, -0.267949, 15.320508, 8.052559]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertAlmostEqual(expect, case[0].distance_between_edges(case[1]), 5)

    def test_overlaps_various_spheres_returns_correct_boolean(self):
        cases = [
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(0, 0, 0), 1)),
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(1, 1, 1), 1)),
            (Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(10, 10, 10), 1)),
            (Sphere(Point3D(-1, -1, -1), 10), Sphere(Point3D(10, 10, 10), 10)),
            (Sphere(Point3D(-1, 1, 4), 5), Sphere(Point3D(-2, -3, -4), 4)),
        ]
        expecteds = [True, True, False, True, True]
        for (case, expect) in zip(cases, expecteds):
            with self.subTest(case=case, expect=expect):
                self.assertEqual(expect, case[0].overlaps(case[1]))

    def test_equals_on_equal_spheres_returns_true(self):
        sphere_a = Sphere(Point3D(1, 2, 3), 1)
        sphere_b = Sphere(Point3D(1, 2, 3), 1)
        self.assertEqual(sphere_a, sphere_b)

    def test_equals_on_not_equal_spheres_returns_false(self):
        sphere_a = Sphere(Point3D(1, 2, 3), 1)
        sphere_b = Sphere(Point3D(1, 2, 3), 2)
        self.assertNotEqual(sphere_a, sphere_b)

    def test_equal_on_sphere_and_string_returns_false(self):
        sphere = Sphere(Point3D(1, 2, 3), 4)
        self.assertNotEqual("Sphere(centre_point=Point3D(x=1, y=2, z=3), radius=4)", sphere)

    def test_repr_arbitrary_sphere_returns_correct_string(self):
        sphere = Sphere(Point3D(1, 2, 3), 4)
        self.assertEqual("Sphere(centre_point=Point3D(x=1, y=2, z=3), radius=4)", str(sphere))
