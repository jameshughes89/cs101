import unittest

from src.circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle_0 = Circle(0)
        self.circle_10 = Circle(10)

    def test_circle_of_radius_0_has_radius_0(self):
        self.assertEqual(0, self.circle_0.radius)

    def test_circle_of_radius_0_has_diameter_0(self):
        self.assertEqual(0, self.circle_0.diameter())

    def test_circle_of_radius_0_has_area_0(self):
        self.assertEqual(0, self.circle_0.area())

    def test_circle_of_radius_0_has_circumference_0(self):
        self.assertEqual(0, self.circle_0.circumference())

    def test_circle_of_radius_10_has_radius_10(self):
        self.assertEqual(10, self.circle_10.radius)

    def test_circle_of_radius_10_has_correct_diameter(self):
        self.assertEqual(20, self.circle_10.diameter())

    def test_circle_of_radius_10_has_correct_area(self):
        self.assertAlmostEqual(314.159265, self.circle_10.area(), 5)

    def test_circle_of_radius_10_has_correct_circumference(self):
        self.assertAlmostEqual(62.831853, self.circle_10.circumference(), 5)

    def test_setting_radius_to_20_updates_radius_to_20(self):
        self.circle_0.radius = 20
        self.assertEqual(20, self.circle_0.radius)

    def test_setting_radius_to_20_returns_correct_diameter(self):
        self.circle_0.radius = 20
        self.assertEqual(40, self.circle_0.diameter())

    def test_setting_radius_to_20_returns_correct_area(self):
        self.circle_0.radius = 20
        self.assertAlmostEqual(1256.637061, self.circle_0.area(), 5)

    def test_setting_radius_to_20_returns_correct_circumference(self):
        self.circle_0.radius = 20
        self.assertAlmostEqual(125.6637061, self.circle_0.circumference(), 5)