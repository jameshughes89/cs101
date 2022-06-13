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



Sphere Class
============


Constructor and Attributes
--------------------------


Methods
-------

* The methods we want are

    * Calculate the ``diameter``, ``surface_area`` and ``volume``
    * Measure the ``distance_between_centres`` of two ``Sphere`` objects
    * Measure the ``distance_between_edges`` of two ``Sphere`` objects
    * Check if a ``Sphere`` ``overlaps`` another in the three dimensional space
    * A way to check if two ``Sphere`` objects are equivalent (``__eq__``)
    * A way to generate a human readable string representation of a ``Sphere`` (``__repr__``)


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


* The above three methods follow the same pattern we saw with the ``Circle``
* These look like regular functions, but the difference is

    * They are associated with an instance of a ``Sphere``
    * They have a ``self`` parameter, which is a reference variable to the ``Sphere`` instance
    * Accessing any of the object's attributes are done through the use of the ``self`` reference variable


* Below is the ``distance_between_centres`` method, where we see some things that may feel odd

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
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


* The method takes a parameter, ``other``, that should be of type ``Sphere`` --- the class we are writing
* But this does not break any rules --- we are writing a method that can be invoked on an instance of the ``Sphere`` class that takes an instance of a ``Sphere`` as a parameter
* This is OK since the intended functionality is to find the distance between two ``Sphere`` objects

    * The distance from the ``Sphere`` the method was invoked on to the ``Sphere`` that was passed as a parameter

* If this still makes you uneasy, consider how we would use this method

.. code-block:: python
    :linenos:

    sphere_a = Sphere(1, 1, 1, 10)
    sphere_b = Sphere(2, 2, 2, 15)
    distance = sphere_a.distance_between_centres(sphere_b)
    print(distance)                                         # Results in 1.732051


* In the above example, I invoked the method ``distance_between_centres`` on ``sphere_a`` and passed ``sphere_b`` as the argument
* If we take a moment to analyze the code within the function, we may get a better sense of the ``self`` reference variable

    * Below is the relevant code from the ``distance_between_centres`` method

.. code-block:: python
    :linenos:

    def distance_between_centres(self, other: "Sphere") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)


* This code calculates the Euclidean distance between the centres in three dimensional space
* But notice that we are making use of two reference variables --- ``self`` and ``other``

    * This may be where ``self`` starts to make a little more sense

* Again, consider ``sphere_a.distance_between_centres(sphere_b)``

    * In this context, ``sphere_a`` would be the ``self`` ``Sphere`` object reference
    * And ``sphere_b`` would be the ``other`` reference

.. note::

    You may have also noticed how the type hint for ``other`` is the *string* ``"Sphere"``, as opposed to just
    ``Sphere``, like how the function's return type hint is just ``float`` instead of the string ``"float"``.  This is
    because the ``Sphere`` class, as far as Python is concerned, is not defined yet as the method
    ``distance_between_centres`` is being defined within the class ``Sphere`` that is currently being defined.


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


* In ``distance_between_edges`` above, notice how the method makes a call to the method ``distance_between_centres``
* Since the ``distance_between_edges`` needs the distance between centres in order to complete it's calculation, there is no need to re-write that code --- just call ``distance_between_centres``
* But, like the attributes, if we want to access the instance's methods, we must access them via the reference variable ``self``


.. code-block:: python
    :linenos:

    class Sphere:

        # init and/or other methods not shown for brevity

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


* Similarly, the ``overlaps`` method can be written by making use of the already existing method ``distance_between_edges``


``__eq__``
^^^^^^^^^^


``__repr__``
^^^^^^^^^^^^


Testing
-------



For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_