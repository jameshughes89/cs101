import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def distance_from_point(self, point) -> float:
        pass

    def find_midpoint(self, point):
        pass

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass