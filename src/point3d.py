import math


class Point3D:
    """
    A class for representing points in a three dimensional (3D) space.
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_from_origin(self) -> float:
        """
        Calculate the Euclidean distance from this Point3D (self) and the origin (0, 0, 0).

        :return: The Euclidean distance from the self Point3D and the origin
        :rtype: float
        """
        return self.distance_from_point(Point3D(0, 0, 0))

    def distance_from_point(self, other) -> float:
        """
        Calculate the Euclidean distance from this Point3D (self) and the Point3D passed as a parameter.

        :param other: A Point3D to find the the Euclidean distance to from the self Point3D
        :type other: Point3D
        :return: The Euclidean distance between the self Point3D and the parameter Point3D other
        :rtype: float
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def find_midpoint(self, other):
        """
        Return a new Point3D that is the midpoint between this Point3D (self) and the Point3D passed as a parameter.

        :param other: A Point3D to find the the midpoint to from the self Point3D
        :type other: Point3D
        :return: A Point3D at the midpoint between the self Point3D and the parameter Point3D other
        :rtype: Point3D
        """
        midpoint_x = (self.x - other.x) / 2 + other.x
        midpoint_y = (self.y - other.y) / 2 + other.y
        midpoint_z = (self.z - other.z) / 2 + other.z
        return Point3D(midpoint_x, midpoint_y, midpoint_z)

    def __eq__(self, other) -> bool:
        """
        Check if the self Point3D is equal to the Point3D passed as a parameter. Points3D are considered equal if they
        have the same x, y, and z values.

        This is a "magic method" that can be used with `==`.

        :param other: A Point3D to compare to the self point3D
        :type other: Point3D
        :return: A boolean indicating if the two Point3Ds are equivalent.
        :rtype: boolean
        """
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __repr__(self) -> str:
        """
        Generate and return a string representation of the Point3D object.

        This os a "magic method" that can be used with `str(some_point3d)` or for printing.

        :return: A string representation of the Point3D
        :rtype: string
        """
        return f"Point({self.x}, {self.y}, {self.z})"


point_origin = Point3D(0, 0, 0)
assert 0 == point_origin.x
assert 0 == point_origin.y
assert 0 == point_origin.distance_from_origin()
assert 0 == point_origin.distance_from_point(Point3D(0, 0, 0))
assert 0.001 > abs(point_origin.distance_from_point(Point3D(1, 1, 1)) - 1.732051)
assert 0.001 > abs(point_origin.distance_from_point(Point3D(-1, -1, -1)) - 1.732051)
assert Point3D(1, 1, 1) == point_origin.find_midpoint(Point3D(2, 2, 2))
assert Point3D(-1, -1, -1) == point_origin.find_midpoint(Point3D(-2, -2, -2))
assert Point3D(0, 0, 0) == point_origin.find_midpoint(Point3D(0, 0, 0))
assert "Point(0, 0, 0)" == str(point_origin)

point = Point3D(-2, 7, 4)
assert 0.001 > abs(point.distance_from_origin() - 8.306624)
assert 0.001 > abs(point.distance_from_point(Point3D(0, 0, 0)) - 8.306624)
assert 0.001 > abs(point.distance_from_point(Point3D(6, 3, 0)) - 9.797959)
assert Point3D(5, 5.5, 3) == point.find_midpoint(Point3D(12, 4, 2))
assert "Point(-2, 7, 4)"

assert point != point_origin
assert point_origin == Point3D(0, 0, 0)
