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


Magic Methods
^^^^^^^^^^^^^

* There exist a number of special, or *magic* methods within Python
* What makes these methods *magic* is that you do not call them directly; you call them indirectly through some other syntax
* In fact, the ``__init__`` method, the constructor, is a magic method

    * You never actually directly call ``__init__`` in your code
    * Instead, the constructor gets invoked when instantiating an instance of the class

        * ``some_point = Point3D(1, 2, 3)``

* `There are many of these special methods <https://docs.python.org/3/reference/datamodel.html#specialnames>`_ , but, in addition to the constructor, we will focus on two important ones

    * ``__eq__`` --- a method for checking object equality
    * ``__repr__`` --- a method for generating a human readable string representation of the object


* It is common to want to check if two things are equal
* For example, like numbers --- ``if some_number == 10:``
* With numbers, Python already knows what equality is
* Similarly with strings and booleans
* However, with custom classes, Python will not know what it means for instances of that class to be equal, unless you tell it

* In the context of the ``Point3D`` class, you may have a good idea of what it means for two instances of this object to be
* But Python cannot read your mind; you need to tell Python what it means for two ``Point3D`` objects to be equal
* By default, Python will try to be helpful if you ask it if two objects of a custom class are equal

    * The default equality check is checking if two reference variables are referencing literally the exact same object in memory

* A more reasonable equality check for ``Point3D`` objects would be if they exist in the same location within the three dimensional space

    * That is, if the ``x``, ``y``, and ``z`` attributes, representing the coordinates, are equal
    * If two ``Point3D`` objects have the same ``x``, ``y``, and ``z`` values, they are equal, otherwise they are not

.. code-block:: python
    :linenos:

    class Point3D:

        # init and/or other methods not shown for brevity

        def __eq__(self, other) -> bool:
            return self.x == other.x and self.y == other.y and self.z == other.z


* The above code showing the ``__eq__`` method is how we define our equals magic method

    * Check if the ``self`` and ``other`` have all their attributes being the same

* You may be tempted to check equality by calling the ``__eq__`` method explicitly

    * ``point_a.__eq__(point_b)``

* Although this will work, it is a little clunky
* Instead, we will indirectly invoke the equality method by using ``==`` like we have used for every other equality check

    * ``point_a == point_b``

* There is, however, one problem with the way we wrote our equality method
* Consider the below example

.. code-block:: python
    :linenos:

    some_point = Point3D(1, 2, 3)
    some_circle = Circle(10)

    print(some_point == some_circle)


* Running this code results in ``AttributeError: 'Circle' object has no attribute 'x'``
* The trouble is that the ``Circle`` instance, which would be ``other`` in the ``Point3D``\'s equality method, does not have an ``x``, ``y``, or ``z`` attribute
* A simple way to fix this is to check if the ``other`` reference variable is even referencing something that can be properly compared to

.. code-block:: python
    :linenos:
    :emphasize-lines: 17

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