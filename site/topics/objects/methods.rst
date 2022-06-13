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

* In order to define a ``Sphere``, all we really need is a ``radius``
* With a ``radius``, can calculate some values about the ``Sphere``

    * Diameter
    * Surface Area
    * Volume

* But we have an extra requirement --- we need to know *where* the ``Sphere`` is in a three dimensional coordinate space
* Therefore, in addition to a ``radius``, we need to keep track of ``x``, ``y``, and ``z`` coordinates
* With this information, we can start to perform some more sophisticated calculations

    * How far away are two ``Sphere`` objects from one another?
    * Do two ``Sphere`` objects overlap/collide?

* There is nothing stopping us from adding more functionality to our ``Sphere`` class, but we will keep it simple for now


Constructor and Attributes
--------------------------


Methods
-------


``__eq__``
^^^^^^^^^^


``__repr__``
^^^^^^^^^^^^


Testing
-------



For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_