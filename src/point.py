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

    def __eq__(self, other) -> bool:
        """
        Check if the self Point is equal to the Point passed as a parameter. Points are considered equal if they have
        the same x and y values.

        This is a "magic method" that can be used with `==`.

        :param other: A Point to compare to the Self point
        :type other: Point
        :return: A boolean indicating if the two points are equivenent.
        :rtype: boolean
        """
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self) -> str:
        """
        Generate and return a string representation of the Point object.

        This os a "magic method" that can be used with `str(some_point)` or for printing.e

        :return: A string representation of the Point
        :rtype: string
        """
        return f"Point({self.x}, {self.y})"


point_origin = Point(0, 0)
assert 0 == point_origin.x
assert 0 == point_origin.y
assert 0 == point_origin.distance_from_origin()
assert 0 == point_origin.distance_from_point(Point(0, 0))
assert 0.001 > abs(point_origin.distance_from_point(Point(1, 1)) - 1.4142135)
assert 0.001 > abs(point_origin.distance_from_point(Point(-1, -1)) - 1.4142135)
assert Point(1, 1) == point_origin.find_midpoint(Point(2, 2))
assert Point(-1, -1) == point_origin.find_midpoint(Point(-2, -2))
assert Point(0, 0) == point_origin.find_midpoint(Point(0, 0))
assert "Point(0, 0)" == str(point_origin)

point = Point(-2, 7)
assert 0.001 > abs(point.distance_from_origin() - 7.2801099)
assert 0.001 > abs(point.distance_from_point(Point(0, 0)) - 7.2801099)
assert 0.001 > abs(point.distance_from_point(Point(6, 3)) - 8.94427)
assert Point(5, 5.5) == point.find_midpoint(Point(12, 4))
assert "Point(-2, 7)"

assert point != point_origin