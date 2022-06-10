import math

from src.point3d import Point3D


class Sphere:
    """
    Class for managing Spheres within a 3D space. This includes tracking it's location in three dimensional space and
    radius. Additionally, it allows for some basic geometry calculations, distance measurements between Spheres, and
    checking if two Spheres overlap.
    """

    def __init__(self, x: float, y: float, z: float, radius: float):
        self.x = x
        self.y = y
        self.z = z
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
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

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
            return self.x == other.x and self.y == other.y and self.z == other.z and self.radius == other.radius
        return False

    def __repr__(self) -> str:
        return f"Sphere({self.x}, {self.y}, {self.z}, {self.radius})"


sphere_origin_0 = Sphere(0, 0, 0, 0)
assert 0 == sphere_origin_0.x
assert 0 == sphere_origin_0.y
assert 0 == sphere_origin_0.z
assert 0 == sphere_origin_0.radius
assert 0 == sphere_origin_0.diameter()
assert 0 == sphere_origin_0.surface_area()
assert 0 == sphere_origin_0.volume()
assert 0 == sphere_origin_0.distance_between_centres(Sphere(0, 0, 0, 0))
assert 0 == sphere_origin_0.distance_between_edges(Sphere(0, 0, 0, 0))
assert True == sphere_origin_0.overlaps(Sphere(0, 0, 0, 0))
assert True == (sphere_origin_0 == Sphere(0, 0, 0, 0))
assert False == (sphere_origin_0 == Sphere(0, 0, 0, 1))
assert "Sphere(0, 0, 0, 0)" == str(sphere_origin_0)

sphere = Sphere(1, 2, 3, 4)
assert 1 == sphere.x
assert 2 == sphere.y
assert 3 == sphere.z
assert 4 == sphere.radius
assert 8 == sphere.diameter()
assert 0.01 > abs(sphere.surface_area() - 201.06)
assert 0.01 > abs(sphere.volume() - 268.08)
assert 0.01 > abs(sphere.distance_between_centres(Sphere(0, 0, 0, 0)) - 3.74)
assert 0.01 > abs(sphere.distance_between_edges(Sphere(0, 0, 0, 0)) - (-0.26))
assert True == sphere.overlaps(Sphere(0, 0, 0, 0))
assert False == (sphere == Sphere(0, 0, 0, 0))
assert True == (sphere == Sphere(1, 2, 3, 4))
assert "Sphere(1, 2, 3, 4)" == str(sphere)
