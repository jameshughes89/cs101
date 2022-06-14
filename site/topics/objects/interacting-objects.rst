***********************************
Objects III --- Interacting Objects
***********************************

* We completed the ``Sphere`` class in the previous topic, and it will work for our needs
* However, there are a few things we could do to improve the design and implementation
* One idea is to make a ``Point3D`` class to manage all the point related things

    * Location in three dimensional space
    * Distance between points
    * Equality on points

* Although there is nothing wrong with the original ``Sphere`` implementation, let's consider that

    * It will make our ``Sphere`` class simpler and easier to understand
    * It allows us to write the methods at a higher-level of abstraction since can deal with ``Point3D`` objects instead of individual coordinates
    * If we wanted to make other three dimensional shapes, they could use something like a ``Point3D`` class to represent their position
    * It allows us to abstract and delegate some functionality to another class
    * It will help with testing since we can test the ``Point3D`` class' functionality and the ``Sphere``\s independently


Point3D Class
=============

* The purpose of the ``Point3D`` class is to replace all the coordinate details from the ``Sphere`` class
* The class will have three attributes that represent a position within some three dimensional space with a Cartesian coordinate system

    * ``x``
    * ``y``
    * ``z``

* The class will also have a few methods, including some that will replace functionality within the ``Sphere`` class

    * A method for measuring the ``Point3D``\s distance from the origin
    * A method for measuring the distance from another ``Point3D`` object
    * A method for finding the midpoint between two points
    * A method for checking if two ``Point3D`` objects are *equal*
    * A method for generating a nice, human readable string representation of the object


Constructor and Attributes
--------------------------

* Below is the start of the ``Point3D`` class, including the constructor and assignment of the attributes

.. code-block:: python
    :linenos:

    import math


    class Point3D:
        """
        A class for representing points in a three dimensional (3D) space.
        """

        def __init__(self, x: float, y: float, z: float):
            self.x = x
            self.y = y
            self.z = z


* That's it --- that's all we need to get started with the ``Point3D`` class


Methods
-------

* The methods we want are

    * A way to measure the distance from another point  --- ``distance_from_point``
    * An ``__eq__`` method for equality
    * A ``__repr__`` for generating a string representation of the object

.. code-block:: python
    :linenos:

    class Point3D:

        # init and/or other methods not shown for brevity

        def distance_from_point(self, other: "Point3D") -> float:
            """
            Calculate the Euclidean distance from this Point3D (self) and the Point3D passed as a parameter.

            :param other: A Point3D to find the the Euclidean distance to from the self Point3D
            :type other: Point3D
            :return: The Euclidean distance between the self Point3D and the parameter Point3D other
            :rtype: float
            """
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


* The above method is following the same pattern as before
* Like within the ``Sphere`` class, we have a method making use of another class method



.. code-block:: python
    :linenos:

    class Point3D:

        # init and/or other methods not shown for brevity

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
            return f"Point3D({self.x}, {self.y}, {self.z})"


* In the above ``__eq__`` method, equality for ``Point3D`` objects will be if all their attributes match
* The ``__repr__`` will follow the same pattern as the ``Sphere`` --- class name with the relevant attributes


Testing
-------

* Below is a series of ``assert`` tests verifying the ``Point3D`` class' correctness
* Like before, these tests *work*, but we area pushing the limits of our simple ``assert`` tests

.. code-block:: python
    :linenos:

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
    assert "Point3D(0, 0, 0)" == str(point_origin)

    point = Point3D(-2, 7, 4)
    assert 0.001 > abs(point.distance_from_origin() - 8.306624)
    assert 0.001 > abs(point.distance_from_point(Point3D(0, 0, 0)) - 8.306624)
    assert 0.001 > abs(point.distance_from_point(Point3D(6, 3, 0)) - 9.797959)
    assert Point3D(5, 5.5, 3) == point.find_midpoint(Point3D(12, 4, 2))
    assert "Point3D(-2, 7, 4)"

    assert point != point_origin
    assert point_origin == Point3D(0, 0, 0)


Sphere Class
============

* With our ``Point3D`` class, we can now make use of it in the ``Sphere`` class to offload the relevant work

    * Keeping track of the location of the centre of the ``Sphere`` within the three dimensional space
    * Measuring distances between points
    * Checking equality between centre points in the space


Constructor and Attributes
--------------------------

.. code-block:: python
    :linenos:

    import math


    class Sphere:
        """
        Class for managing Spheres within a 3D space. This includes tracking it's centre point and radius. Additionally, it
        allows for some basic geometry calculations, distance measurements between Spheres, and checking if two Spheres
        overlap.
        """

        def __init__(self, centre_point: Point3D, radius: float):
            self.centre_point = centre_point
            self.radius = radius


* From looking at the above code, we see that we have removed the ``x``, ``y``, and ``z`` coordinates as explicit attributes for the ``Sphere``
* Instead, we make use of a ``Point3D`` object
* And, as we know, those coordinate attributes exist within the ``Point3D`` class, which are entirely accessible from within the ``Sphere`` class



Methods
-------

* The below methods for calculating the ``diameter``, ``surface_area``, and ``volume`` do not change since they only make use of the ``Sphere`` object's ``radius`` attribute

.. code-block:: python
    :linenos:

    class Sphere:

        # init and/or other methods not shown for brevity

        def diameter(self) -> float:
            return 2 * self.radius

        def surface_area(self) -> float:
            return 4 * math.pi * self.radius**2

        def volume(self) -> float:
            return (4 / 3) * math.pi * self.radius**3


* The method ``distance_between_centres`` is one that ends up being changed by offloading the Euclidean distance calculation to the ``Point3D`` object

.. code-block:: python
    :linenos:

    class Sphere:

        # init and/or other methods not shown for brevity

        def distance_between_centres(self, other: "Sphere") -> float:
            """
            Calculate and return the distance between the centres of two Spheres.

            :param other: Sphere whose centre to find the distance to from the self Sphere.
            :type other: Sphere
            :return: Distance between the Sphere centres.
            :rtype: float
            """
            return self.centre_point.distance_from_point(other.centre_point)


* Notice how this updated method has no responsibility over calculating the distance
* Instead, we simply ask the ``Point3D`` object how far away it is from another ``Point3D`` object


.. code-block:: python
    :linenos:

    class Sphere:

        # init and/or other methods not shown for brevity

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


* The above ``distance_between_edges`` and ``overlaps`` methods remain unchanged from the original implementation of the ``Sphere``

    * They had already offloaded the Euclidean distance calculations to the ``distance_between_centres`` method


* And finally, the magic methods end up getting updated slightly

.. code-block:: python
    :linenos:

    class Sphere:

        # init and/or other methods not shown for brevity

        def __eq__(self, other) -> bool:
            if isinstance(other, Sphere):
                return self.radius == other.radius and self.centre_point == other.centre_point
            return False

* The above updated ``__eq__`` now checks if the ``centre_point`` attributes are the same instead of checking the ``x``, ``y``, and ``z`` explicitly

    * Remember, we defined the ``__eq__`` within the ``Point3D`` class


.. code-block:: python
    :linenos:

    class Sphere:

        # init and/or other methods not shown for brevity

        def __repr__(self) -> str:
            return f"Sphere(centre_point={self.centre_point}, radius={self.radius})"


* And lastly, instead of having our ``__repr__`` extract the ``x``, ``y``, and ``z`` attributes, we simply get the string version of the ``Point3D``

    * With f-strings, Python will automatically convert the ``Point3D`` object to a string

* The final string representation of the ``Sphere`` class will not be slightly different from before
* Before, we would see something like ``Sphere(x=1, y=2, z=3, radius=4)``
* Now we would see something like ``Sphere(centre_point=Point3D(x=1, y=2, z=3), radius=4)``


Testing
-------

* Although we could adapt our simple ``assert`` tests from the original ``Sphere`` implementation, those tests are becoming hard to manage
* Our tests are now needing more setup before they can be run

    * For example, we now may need to make instances of ``Point3D`` objects and ``Sphere`` objects before we can test anything

* It's also difficult to tell the tests apart as they feel a little jumbled together
* It's not easy to know what a test is doing just by looking at it anymore

    * For example, ``assert 0.01 > abs(sphere.distance_between_edges(Sphere(0, 0, 0, 0)) - (-0.26))``
    * We can piece it together, but it's not immediately clear

* It's also hard to get a sense of how thorough the tests are

    * Sure we have tested the distance between ``Sphere`` objects, but maybe we should test the distance if the ``Sphere`` objects are in different octants (3D equivalent of quadrants)

* Further, if we want to be more thorough in the distance tests, there is going to be a lot of duplicate code

* Fortunately, Python provides us with a tool to help us manage our tests --- ``unittest``
* The next topic will cover details on how to start transitioning our tests to the ``unittest`` framework for improved tests


For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_