import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def diameter(self) -> float:
        return 2 * self.radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def circumference(self) -> float:
        return 2 * math.pi * self.radius


circle_zero = Circle(0)
assert 0 == circle_zero.radius
assert 0 == circle_zero.diameter()
assert 0 == circle_zero.area()
assert 0 == circle_zero.circumference()

circle_10 = Circle(10)
assert 10 == circle_10.radius
assert 20 == circle_10.diameter()
assert 0.001 < abs(circle_10.area() - 125.66)
assert 0.001 < abs(circle_10.circumference() - 1256.64)

