******************************
Objects II --- More on Methods
******************************

* The ``Circle`` class discussed in the previous topic introduced:

    * How to write classes
    * How to write and make use of a constructor
    * Attributes, both how to set them and how to access them
    * How to write and use methods
    * How to make instances of the class

* In this topic, we will create more classes containing more complex functionality
* Additionally, we will see objects interacting with one another and how objects can provide a nice level of abstraction


* The goal is to define a ``Sphere`` class

    * Like the ``Circle`` class, it will know its radius
    * It will also know its position within some three dimensional space
    * It will provide functionality to measure distances between ``Sphere`` objects and check if they overlap/collide

* The catch is, we also need a way to specify the point in the three dimensional space
* To address this, we will define a ``Point3D`` class

    * It will know its position in the three dimensional space based on a three dimensional coordinate system
    * Provide some simple geometry functionality
    * Provide a way to measure distance between ``Point3D`` objects, which will help with implementing the ``Sphere`` class' functionality


Point3D Class
=============


Constructor and Attributes
--------------------------


Methods
-------

* The three methods we want are

    * A way to measure the distance from the origin --- ``distance_from_origin``
    * A way to measure the distance from another point  --- ``distance_from_point``
    * A way to find the midpoint between two points --- ``find_midpoint``


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


* The above example of ``distance_from_point``, like before, follows the same pattern as before for writing a method for a class

    * It has ``self`` as the first parameter in the method's parameter list
    * It uses ``self`` as a reference variable to access the instance's attributes

* What you may find odd is that the method takes a parameter, ``other``, that should be of type ``Point3D`` --- the class we are writing
* But this does not break any rules --- we are writing a method that can be invoked on an instance of the ``Point3D`` class that takes an instance of a ``Point3D`` as a parameter
* This makes sense since the method's intended functionality is to find the distance between two points

    * The distance from the ``Point3D`` the method was invoked on to the ``Point3D`` that was passed as a parameter

* If this still makes you uneasy, consider how we would use this method

.. code-block:: python
    :linenos:

    point_a = Point3D(1, 1, 1)
    point_b = Point3D(2, 2, 2)
    distance = point_a.distance_from_point(point_b)
    print(distance)                                     # Results in 1.732051


* In the above example, I invoked the method ``distance_from_point`` on ``point_a`` and passed ``point_b`` as the parameter

    * In this case, the method would produce the same result if one called ``point_b.distance_from_point(point_a)`` instead

* If we take a moment to analyze the code within the function, we may get a better sense of the ``self`` reference variable

    * Below is the relevant code from the ``distance_from_point`` method

.. code-block:: python
    :linenos:

    def distance_from_point(self, other: "Point3D") -> float:
        math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


* This code is simply calculating the Euclidean distance between points in three dimensional space
* But notice that we are making use of two reference variables --- ``self`` and ``other``

    * This may be where ``self`` starts to make a little more sense

* Again, consider ``point_a.distance_from_point(point_b)``

    * In this context, ``point_a`` would be the ``self`` ``Point3D`` object reference
    * ``point_b`` would be the ``other`` reference

.. note::

    You may have also noticed how the type hint for ``other`` is the *string* ``"Point3D"``, as opposed to just
    ``Point3D``, like how the function's return type hint is just ``float`` instead of the string ``"float"``.  This is
    because the ``Point3D`` class, as far as Python is concerned, is not defined yet. This is because the method
    ``distance_from_point`` is being defined within the class ``Point3D`` that you are currently defining.


.. code-block:: python
    :linenos:

    class Point3D:

        # init and/or other methods not shown for brevity

        def distance_from_origin(self) -> float:
            """
            Calculate the Euclidean distance from this Point3D (self) and the origin (0, 0, 0).

            :return: The Euclidean distance from the self Point3D and the origin
            :rtype: float
            """
            return self.distance_from_point(Point3D(0, 0, 0))


* Above is the ``distance_from_origin`` method
* What's interesting here is the method makes use of one of the class' existing methods --- ```distance_from_point```

    * Here, it's just that the point we want to calculate the distance to is the origin

* What is important to notice here is the use of ``self`` before the method call
* Again, in order to access any of the object's methods, we must access the object through a reference variable

.. code-block:: python
    :linenos:

    class Point3D:

        # init and/or other methods not shown for brevity

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


* In ``find_midpoint`` above, a new ``Point3D`` object is being created and then returned by the function


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