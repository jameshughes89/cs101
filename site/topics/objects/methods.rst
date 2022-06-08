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


Point3D Class
=============

* We will start with the ``Point3D`` class since it will be utilized by the ``Sphere`` class
* The class will have three attributes that represent a position within some three dimensional space with a Cartesian coordinate system

    * ``x``
    * ``y``
    * ``z``

* The class will also have a few methods that may come in handy for the ``Sphere`` class

    * A method for measuring the ``Point3D``\s distance from the origin
    * A method for measuring the distance from another ``Point3D`` object
    * A method for finding the midpoint between two points

* The class will also make use of some handy *magic methods* --- methods you don't invoke *directly* (more on this later)

    * A method for checking if two ``Point3D`` objects are *equal*
    * A method for generating a nice, human readable string representation of the object


Constructor and Attributes
--------------------------

* Below is the start of the ``Point3D`` class, including the constructor and assignment of the attributes
* You will find it follows the same pattern as the ``Circle`` class already discussed
* The only real differences are trivial

    * The ``import math``, which will help with some geometry calculations
    * The name of the class is different
    * The parameters the ``__init__`` method has
    * The attributes


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
* Like before, we can even start making instances of the ``Point3D`` class
* Though, also like before, the class is not particularly helpful without the required methods


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