import unittest

from src.point3d import Point3D
from src.sphere import Sphere


class TestSphere(unittest.TestCase):
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
            Sphere(Point3D(10, 11, 12), 10),
        ]
        expecteds = [0, 2, 0, 20]
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
