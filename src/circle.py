import math


class Circle:
    """
    A class for representing circle based on its radius. The class provides functionality to perform basic geometry
    calculations (diameter, area, circumference).
    """

    def __init__(self, radius: float):
        """
        Creates a Circle object with the specified radius.

        :param radius: The radius of the Circle
        :type radius: float
        """
        self.radius = radius

    def diameter(self) -> float:
        """
        Calculate and return the diameter of the Circle based on its radius.

        :return: diameter of the Circle
        :rtype: float
        """
        return 2 * self.radius

    def area(self) -> float:
        """
        Calculate and return the area of the Circle based on its radius.

        :return: Area of the Circle
        :rtype: float
        """
        return math.pi * self.radius**2

    def circumference(self) -> float:
        """
        Calculate and return the circumference of the Circle based on its radius.

        :return: Circumference of the Circle
        :rtype: float
        """
        return 2 * math.pi * self.radius

    def __eq__(self, other) -> bool:
        """
        Check if the Circle (self) is equal to the parameter Circle other. Circles are equal if they have the same
        radius.

        This is a "magic method" that can be used with `==`.

        :param other: A Circle to be compared to self Circle
        :type other: Circle
        :return: A boolean indicating if the two Circles are equivalent
        """
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __repr__(self) -> str:
        """
        Generate and return a string representation of the Circle object.

        This os a "magic method" that can be used with `str(some_circle)` or for printing.

        :return: A string representation of the Circle
        :rtype: string
        """
        return f"Circle(radius={self.radius})"


circle_0 = Circle(0)
assert 0 == circle_0.radius
assert 0 == circle_0.diameter()
assert 0 == circle_0.area()
assert 0 == circle_0.circumference()
assert "Circle(radius=0)" == str(circle_0)

circle_10 = Circle(10)
assert 10 == circle_10.radius
assert 20 == circle_10.diameter()
assert 0.001 > abs(circle_10.area() - 314.1592)
assert 0.001 > abs(circle_10.circumference() - 62.8319)
assert "Circle(radius=10)" == str(circle_10)

assert circle_10 == Circle(10)
assert circle_0 != circle_10
