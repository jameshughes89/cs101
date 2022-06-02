import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def distance_from_point(self, point) -> float:
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def find_midpoint(self, point):
        midpoint_x = (self.x - point.x)/2 + point.x
        midpoint_y = (self.y - point.y)/2 + point.y
        return Point(midpoint_x, midpoint_y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

