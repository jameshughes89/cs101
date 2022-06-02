import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self) -> float:
        return 2 * self.radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def circumference(self) -> float:
        return 2 * math.pi * self.radius


circle_0 = Circle(0)
assert 0 == circle_0.radius
assert 0 == circle_0.diameter()
assert 0 == circle_0.area()
assert 0 == circle_0.circumference()

circle_10 = Circle(10)
assert 10 == circle_10.radius
assert 20 == circle_10.diameter()
assert 0.001 > abs(circle_10.area() - 314.1592)
assert 0.001 > abs(circle_10.circumference() - 62.8319)
