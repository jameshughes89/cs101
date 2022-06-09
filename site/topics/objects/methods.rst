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