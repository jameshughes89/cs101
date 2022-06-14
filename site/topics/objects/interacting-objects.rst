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



Testing
-------



For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_