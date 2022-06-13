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


``__eq__``
^^^^^^^^^^


``__repr__``
^^^^^^^^^^^^


Testing
-------



For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_