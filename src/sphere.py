import math


class Sphere:
    """
    Class for managing Spheres within a 3D space.
    """

    def __init__(self, point, radius):
        self.point = point
        self.radius = radius

    def diameter(self) -> float:
        return 2 * self.radius

    def surface_area(self) -> float:
        return 4 * math.pi * self.radius ** 2

    def volume(self) -> float:
        return (4/3) * math.pi * self.radius ** 3

    def distance_between_centres(self, other) -> float:
        """
        Calculate and return the distance between the centres of two Spheres.

        :param other: Sphere whose centre to find the distance to from the self Sphere.
        :type other: Sphere
        :return: Distance between the Sphere centres.
        :rtype: float
        """
        return self.point.distance_from_point(other.point)

    def distance_between_edges(self, other) -> float:
        """
        Calculate and return the distance between the edges of two Spheres. If the value is negative, the two Spheres
        overlap.

        :param other: Sphere whose edge to find the distance to from the self Sphere.
        :type other: Sphere
        :return: Distance between the Sphere edges.
        :rtype: float
        """
        return self.distance_between_centres(other) - self.radius - other.radius

    def overlaps(self, other) -> bool:
        """
        Determine if two Sphere objects overlap within the 3D space.

        :param other: Sphere to check if it overlaps the self Sphere overlaps
        :type other: Sphere
        :return: Boolean indicating if the two Spheres overlap
        :rtype: bool
        """
        return self.distance_between_edges(other) < 0

    def __eq__(self, other):
        if isinstance(other, Sphere):
            return self.radius == other.radius == self.point == other.point

    def __repr__(self):
        return f"Sphere({self.point}, {self.radius})"

