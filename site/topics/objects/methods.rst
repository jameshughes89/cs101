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

    class Point3D:

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


``__eq__``
^^^^^^^^^^


``__repr__``
^^^^^^^^^^^^


Testing
-------



For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_