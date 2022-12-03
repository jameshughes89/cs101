import unittest

from src.circle import Circle


class CircleTest(unittest.TestCase):

    def test_circle_of_radius_0_has_radius_0(self):
        circle_0 = Circle(0)
        self.assertEqual(0, circle_0.radius)

    def test_circle_of_radius_0_has_diameter_0(self):
        circle_0 = Circle(0)
        self.assertEqual(0, circle_0.diameter())

    def test_circle_of_radius_0_has_area_0(self):
        circle_0 = Circle(0)
        self.assertEqual(0, circle_0.area())

    def test_circle_of_radius_0_has_circumference_0(self):
        circle_0 = Circle(0)
        self.assertEqual(0, circle_0.circumference())

    def test_circle_of_radius_10_has_radius_10(self):
        circle_10 = Circle(10)
        self.assertEqual(10, circle_10.radius)

    def test_circle_of_radius_10_has_correct_diameter(self):
        circle_10 = Circle(10)
        self.assertEqual(20, circle_10.diameter())

    def test_circle_of_radius_10_has_correct_area(self):
        circle_10 = Circle(10)
        self.assertAlmostEqual(314.159265, circle_10.area(), 5)

    def test_circle_of_radius_10_has_correct_circumference(self):
        circle_10 = Circle(10)
        self.assertAlmostEqual(62.831853, circle_10.circumference(), 5)

    def test_equals_on_equal_circles_returns_true(self):
        circle_a = Circle(1)
        circle_b = Circle(1)
        self.assertEqual(circle_a, circle_b)

    def test_equals_on_not_equal_circles_returns_false(self):
        circle_a = Circle(1)
        circle_b = Circle(2)
        self.assertNotEqual(circle_a, circle_b)

    def test_equal_on_circle_and_string_returns_false(self):
        circle = Circle(1)
        self.assertFalse("Circle(1)" == circle)

    def test_repr_arbitrary_circle_returns_correct_string(self):
        circle = Circle(1)
        self.assertFalse("Circle(1)" == str(circle))
