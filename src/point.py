import math


class Point:
    """
    A class for representing points on a two dimensional (2D) Cartesian plane.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        """
        Calculate the Euclidean distance from this Point (self) and the origin (0, 0).

        :return: The Euclidean distance from the self Point and the origin
        :rtype: float
        """
        return math.sqrt(self.x**2 + self.y**2)

    def distance_from_point(self, point) -> float:
        """
        Calculate the Euclidean distance from this Point (self) and the Point passed as a parameter.

        :param point: A Point to find the the Euclidean distance to from the self Point
        :type point: Point
        :return: The Euclidean distance between the self Point and the parameter Point
        :rtype: float
        """
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def find_midpoint(self, point):
        """
        Return a new Point that is the midpoint between this Point (self) and the Point passed as a parameter.

        :param point: A Point to find the the midpoint to from the self Point
        :type point: Point
        :return: A Point at the midpoint between the self Point and the parameter Point
        :rtype: Point
        """
        midpoint_x = (self.x - point.x)/2 + point.x
        midpoint_y = (self.y - point.y)/2 + point.y
        return Point(midpoint_x, midpoint_y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

