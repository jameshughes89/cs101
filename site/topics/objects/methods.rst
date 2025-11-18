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


* That's it --- that is all we need to get started with the ``Sphere`` class
* Like before, we can even start making instances of a ``Sphere``
* However, like before, the class will not be particularly useful here without the needed functionality


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

    import math


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

    import math


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

    import math


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

    import math


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

Magic Methods
^^^^^^^^^^^^^

* There exist a number of special, or *magic* methods within Python
* What makes these methods *magic* is that you do not call them directly; you call them indirectly through some other syntax
* In fact, the ``__init__`` method, the constructor, is a magic method

    * You never actually directly call ``__init__`` in your code
    * Instead, the constructor gets invoked when instantiating an instance of the class

        * ``some_sphere = Sphere(1, 2, 3, 4)``

* `There are many of these special methods <https://docs.python.org/3/reference/datamodel.html#specialnames>`_
* In addition to the constructor, we will focus on two very important ones here

    * ``__eq__`` --- a method for checking object equality
    * ``__repr__`` --- a method for generating a human readable string representation of the object


``__eq__``
""""""""""

* It is common to want to check if two things are equal
* For example, like numbers --- ``if some_number == 10:``
* With numbers, strings, booleans, and other types, Python already knows what equality is
* However, with custom classes, Python will not know what it means for instances of that class to be equal, unless you tell it

* In the context of the ``Sphere`` class, you may have a good idea of what it means for two instances of this object to be equal
* But Python cannot read your mind; you need to tell Python what it means for two ``Sphere`` objects to be equal
* By default, Python will try to be helpful if you ask it if two objects of a custom class are equal

    * The default equality check is checking if two reference variables are referencing literally the exact same object in memory (aliases)

* A more reasonable equality check for ``Sphere`` objects would be if they are the same size and  exist in the same location within the three dimensional space

    * That is, if the ``radius``, ``x``, ``y``, and ``z`` attributes are equal

.. code-block:: python
    :linenos:

    import math


    class Sphere:

        # init and/or other methods not shown for brevity

        def __eq__(self, other) -> bool:
            return self.x == other.x and self.y == other.y and self.z == other.z and self.radius == other.radius


* The above code showing the ``__eq__`` method is how we define our equals magic method

    * For our needs, check if ``self`` and ``other`` have all their attributes being the same

* You may be tempted to then check equality by calling the ``__eq__`` method explicitly

    * ``sphere_a.__eq__(sphere_b)``

* Although this will work, it is a little clunky and bad style
* Instead, we will indirectly invoke the equality method by using ``==`` like we have used for every other equality check

    * ``sphere_a == sphere_b``

* There is, however, one problem with the way we wrote our equality method
* Consider the below example

.. code-block:: python
    :linenos:

    some_sphere = Sphere(1, 2, 3, 4)
    some_circle = Circle(10)

    print(some_sphere == some_circle)


* Running this code results in ``AttributeError: 'Circle' object has no attribute 'x'``
* The trouble is that the ``Circle`` instance, which would be ``other`` in the ``Sphere``\'s equality method, does not have an ``x``, ``y``, or ``z`` attribute
* A simple way to fix this is to check if the ``other`` reference variable is even referencing something that can be properly compared to

.. code-block:: python
    :linenos:
    :emphasize-lines: 9

    import math


    class Sphere:

        # init and/or other methods not shown for brevity

        def __eq__(self, other) -> bool:
            if isinstance(other, Sphere):
                return self.x == other.x and self.y == other.y and self.z == other.z and self.radius == other.radius
            return False


.. note::

    There was nothing stopping us from defining ``__eq__`` for our ``Circle`` class. In fact, it is arguably something
    we should do. Below is an example of an equality check for the ``Circle`` class.

    .. code-block:: python
        :linenos:

        import math


        class Circle:

            # init and/or other methods not shown for brevity

            def __eq__(self, other) -> bool:
                if isinstance(other, Circle):
                    return self.radius == other.radius
                return False


``__repr__``
""""""""""""

* It is nice to have a good, human readable representation of the values within our program
* For example, think of the number of times you have printed the values of variables when doing some quick tests of your code

.. code-block:: python
    :linenos:

    some_list = ["a", "b", "c"]
    if condition:
        some_list.append("x")
    print(some_list)


* If you were to try this with our newly created ``Sphere`` class, we would get something not overly helpful

.. code-block:: python
    :linenos:

    sphere = Sphere(1, 2, 3, 4)
    print(sphere)                   # Results in <__main__.Sphere object at 0x7f99a2edac10>


* The default behaviour will be the name of the class along with the memory address of where the object is
* Chances are, this is not overly helpful to you
* To address this, we write another magic method --- ``__repr__``

* ``__repr__`` is the representation function, which is for getting a nice string representation of the instance of the class
* This ``__repr__`` method is called whenever we need a string representation of our object

    * ``print(some_sphere)`` will automatically call it
    * ``str(some_sphere)`` will call it
    * ``repr(some_sphere)`` will call it too

* Based on what the object is, there may be a very natural way one would want to represent the object as a string

    * For example, the ``List`` class' ``__repr__`` returns a string of the form ``["a", "b", "c", "d"]``

* But sometimes, like with a ``Sphere``, it may not be obvious and we just want to get enough information about the ``Sphere`` to be helpful for us
* If this is the case, a common representation is ``Sphere(x=1, y=2, z=3, radius=4)`` -- class name, and then relevant attribute values within parentheses

.. code-block:: python
    :linenos:

    import math


    class Sphere:

        # init and/or other methods not shown for brevity

        def __repr__(self) -> str:
            return f"Sphere(x={self.x}, y={self.y}, z={self.z}, radius={self.radius})"


* With the ``__repr__`` written, if I were to call ``print``, ``str``, or ``repr`` on an instance of the class, I would see the values specified

.. note::

    Like with the ``__eq__`` method, we could go back and write a ``__repr__`` for the ``Circle`` class.

    .. code-block:: python
        :linenos:

        import math


        class Circle:

            # init and/or other methods not shown for brevity

            def __repr__(self) -> str:
                return f"Circle(radius={self.radius})"


Testing
-------

* Below is a collection of ``assert`` tests for the ``Sphere`` class
* Though, you may feel that at this stage it's getting harder to get a feel for how complete your tests are

.. code-block:: python
    :linenos:

    sphere_origin_0 = Sphere(0, 0, 0, 0)
    assert 0 == sphere_origin_0.x
    assert 0 == sphere_origin_0.y
    assert 0 == sphere_origin_0.z
    assert 0 == sphere_origin_0.radius
    assert 0 == sphere_origin_0.diameter()
    assert 0 == sphere_origin_0.surface_area()
    assert 0 == sphere_origin_0.volume()
    assert 0 == sphere_origin_0.distance_between_centres(Sphere(0, 0, 0, 0))
    assert 0 == sphere_origin_0.distance_between_edges(Sphere(0, 0, 0, 0))
    assert True == sphere_origin_0.overlaps(Sphere(0, 0, 0, 0))
    assert True == (sphere_origin_0 == Sphere(0, 0, 0, 0))
    assert False == (sphere_origin_0 == Sphere(0, 0, 0, 1))
    assert "Sphere(x=0, y=0, z=0, radius=0)" == str(sphere_origin_0)

    sphere = Sphere(1, 2, 3, 4)
    assert 1 == sphere.x
    assert 2 == sphere.y
    assert 3 == sphere.z
    assert 4 == sphere.radius
    assert 8 == sphere.diameter()
    assert 0.01 > abs(sphere.surface_area() - 201.06)
    assert 0.01 > abs(sphere.volume() - 268.08)
    assert 0.01 > abs(sphere.distance_between_centres(Sphere(0, 0, 0, 0)) - 3.74)
    assert 0.01 > abs(sphere.distance_between_edges(Sphere(0, 0, 0, 0)) - (-0.26))
    assert True == sphere.overlaps(Sphere(0, 0, 0, 0))
    assert False == (sphere == Sphere(0, 0, 0, 0))
    assert True == (sphere == Sphere(1, 2, 3, 4))
    assert "Sphere(x=1, y=2, z=3, radius=4)" == str(sphere)


For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_