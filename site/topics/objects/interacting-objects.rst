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


Constructor and Attributes
--------------------------


Methods
-------

* The methods we want are

    * A way to measure the distance from the origin --- ``distance_from_origin``
    * A way to measure the distance from another point  --- ``distance_from_point``
    * A way to find the midpoint between two points --- ``find_midpoint``
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


        def distance_from_origin(self) -> float:
            """
            Calculate the Euclidean distance from this Point3D (self) and the origin (0, 0, 0).

            :return: The Euclidean distance from the self Point3D and the origin
            :rtype: float
            """
            return self.distance_from_point(Point3D(0, 0, 0))


        def find_midpoint(self, other: "Point3D") -> "Point3D":
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


* The above three methods are following the same pattern as before
* Like within the ``Sphere`` class, we have a method making use of another class method

    * The ``distance_from_origin`` method simply calls ``distance_from_point``, where the argument provided is a ``Point3D`` of the origin

* Another interesting observation is, within the method ``find_midpoint``, a new ``Point3D`` object is being created and then returned by the function

    * In other words, a ``Point3D`` object has the ability to create and return a new instance of a ``Point3D`` object


Magic Methods
^^^^^^^^^^^^^



Testing
-------



Sphere Class
============


Constructor and Attributes
--------------------------


Methods
-------



Testing
-------



For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_