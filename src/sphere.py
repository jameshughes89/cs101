import math

from src.point3d import Point3D


class Sphere:
    """
    Class for managing Spheres within a 3D space. This includes tracking it's centre point and radius. Additionally, it
    allows for some basic geometry calculations, distance measurements between Spheres, and checking if two Spheres
    overlap.
    """

    def __init__(self, centre_point: Point3D, radius: float):
        self.centre_point = centre_point
        self.radius = radius

    def diameter(self) -> float:
        return 2 * self.radius

    def surface_area(self) -> float:
        return 4 * math.pi * self.radius**2

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.radius**3

    def distance_between_centres(self, other: "Sphere") -> float:
        """
        Calculate and return the distance between the centres of two Spheres.

        :param other: Sphere whose centre to find the distance to from the self Sphere.
        :type other: Sphere
        :return: Distance between the Sphere centres.
        :rtype: float
        """
        return self.centre_point.distance_from_point(other.centre_point)

    def distance_between_edges(self, other: "Sphere") -> float:
        """
        Calculate and return the distance between the edges of two Spheres. If the value is negative, the two Spheres
        overlap.

        :param other: Sphere whose edge to find the distance to from the self Sphere.
        :type other: Sphere
        :return: Distance between the Sphere edges.
        :rtype: float
        """
        return self.distance_between_centres(other) - self.radius - other.radius

    def overlaps(self, other: "Sphere") -> bool:
        """
        Determine if two Sphere objects overlap within the 3D space. Two Spheres that are touching (distance of 0
        between edges) are considered overlapping.

        :param other: Sphere to check if it overlaps the self Sphere overlaps
        :type other: Sphere
        :return: Boolean indicating if the two Spheres overlap
        :rtype: bool
        """
        return self.distance_between_edges(other) <= 0

    def __eq__(self, other) -> bool:
        if isinstance(other, Sphere):
            return self.radius == other.radius and self.centre_point == other.centre_point
        return False

    def __repr__(self) -> str:
        return f"Sphere(centre_point={self.centre_point}, radius={self.radius})"
