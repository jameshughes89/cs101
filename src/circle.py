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

