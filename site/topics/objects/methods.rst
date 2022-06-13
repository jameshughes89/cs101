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

* Below is the start of the ``Sphere`` class, including the constructor and the assignment of attributes
* It follows the same pattern as the ``Circle`` class discussed in the previous topic
* The only differences here with the ``Sphere`` are trivial

    * An ``import`` to help with math calculations
    * The name of the class is different
    * The parameters and attributes are for a ``Sphere``


.. code-block:: python
    :linenos:

    import math


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


* That's it --- that is all we need to get started with the ``Point3D`` class
* Like before, we can even start making instances of a ``Sphere``
* However, like before, the class will not be particularly useful here without the needed functionality


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