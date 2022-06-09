**************************
Objects I --- Introduction
**************************


* Objects are a way to combine data and functionality together within our programs
* Motivation for this is, it may help with abstraction and encapsulation
* Further, you may find it a little more natural and analogous to how you think of the world

* Consider the ``List``\s you have been using --- these are objects

    * They have some data associated with them,

        * Their size
        * the information stored in the list

    * But they also have functionality associated with them too

        * ``append``
        * ``remove``


* You are already used to working with some objects (e.g., ``List``)
* But you have not defined your own objects
* In this topic, the basics of how to define your own objects will be covered

	  
Classes vs Objects
==================

* We are going to make ``Circle`` objects
* However, in order to start making our own objects, we first must define a *class*
* A class is simply the code that defines what it means for something to be an object of the class
* For example, we will define a ``Circle`` class, which contains all the information needed for Python to start making instances of ``Circle``\s

    * You can think of the class as the blueprints for making objects

* Going back to ``List``\s

    * There exists a class definition (blueprints) for ``List``\s
    * With the one class, I can then create as many instances of ``List``\s as I want


Circle Class
============

* Just like the rest of the class, we will lean by doing
* In other words, we will define the ``Circle`` class and then make a few instances of ``Circle`` objects

* However, there is one big question --- what is a circle; what data and functionality should it have?

    * Turns out, we get to invent this
    * We decide what data will be stored
    * We decide what functionality it will have

* For our needs, we will have a ``Circle``:

    * Know its radius --- this is an *attribute*, the data
    * Be able to perform basic geometry calculations --- these are *methods*, the functionality


Starting the Class
------------------

* To start writing our ``Circle`` class, we use the ``class`` keyword

.. code-block:: python
    :linenos:

    class Circle:
        """
        A class for representing circle based on its radius. The class provides functionality to perform basic geometry
        calculations (diameter, area, circumference).
        """

* The above example contains the start of the class
* The ``class Circle:`` starts the class

    * Anything indented is part of the ``Circle`` class definition
    * Like how anything indented under an ``if`` is part of the ``if`` block

* The docstring comment is a simple description of the class


Constructor/Initialization and Attributes
-----------------------------------------

* With just the ``class Circle``, we can actually start making instances of the class

.. code-block:: python
    :linenos:

    some_circle = Circle()
    print(type(some_circle))    # Results in something like <class '__main__.Circle'>


* However, this is not particularly useful as we have yet to really describe the ``Circle`` class


Constructor
^^^^^^^^^^^

* To start making the class useful, we will write a special function that tells Python how to setup the class for our needs

.. code-block:: python
    :linenos:

    class Circle:
        """
        A class for representing circle based on its radius. The class provides functionality to perform basic geometry
        calculations (diameter, area, circumference).
        """

        def __init__(self):
            """
            Creates a Circle object with a radius of 0.
            """
            self.radius = 0


* In the above example, we see the use of the special function called ``__init__``, which describes how to initialize an instance of the class

    * The ``__init__`` method is called the *constructor*, or the *initialization* method

* We can also see that we are creating an *attribute* called ``radius`` that will have the value ``0`` upon the creation of a ``Circle`` object

* You will notice a special variable called ``self`` in the parameter list and before the attribute ``radius``

    * ``self`` is a reference variable to *this*, the current instance of the class (itself)
    * All methods within the class require that the first parameter is the ``self`` reference variable
    * Additionally, accessing any attributes or methods within the class require the use of the ``self`` reference variable
    * The ``self`` variable can feel a little weird at first, but it is something that will start to make sense as we go


* With ``__init__`` written with the setup of the attribute ``radius``, we can now start to assign values

.. code-block:: python
    :linenos:

    circle_a = Circle()
    circle_b = Circle()

    circle_a.radius = 1
    circle_b.radius = 5

    print(circle_a.radius)      # Results in 1
    print(circle_b.radius)      # Results in 5


* In the above example, we created two ``Circle`` objects and then assigned a value to their respective ``radius`` attributes
* Both ``circle_a`` and ``circle_b`` are of the class ``Circle``, but they are two separate instances of the class with two separate ``radius`` attributes


Constructor Parameters
^^^^^^^^^^^^^^^^^^^^^^

* We can also include parameters for the ``__init__`` method, as seen below

.. code-block:: python
    :linenos:

    class Circle:
        """
        A class for representing circle based on its radius. The class provides functionality to perform basic geometry
        calculations (diameter, area, circumference).
        """

        def __init__(self, radius: float):
            """
            Creates a Circle object with the specified radius.

            :param radius: The radius of the Circle
            :type radius: float
            """
            self.radius = radius


* In the above example, we include a parameter for the ``radius``, which will be used to set the attribute when a ``Circle`` object is created
* This way we do not need to set the values ourselves after they are created, as seen in the following example

.. code-block:: python
    :linenos:

    circle_a = Circle(1)
    circle_b = Circle(5)

    print(circle_a.radius)      # Results in 1
    print(circle_b.radius)      # Results in 5


Functionality and Methods
-------------------------

* The ``Circle`` class has the attribute ``radius``. but as of now, that's all it can do --- store a radius value
* Further, there are other features of a circle  we may want to capture

    * Diameter of a circle
    * Area of a circle
    * Circumference of a circle

* Fortunately, although these values are not stored within the ``Circle`` class as attributes, they can be calculated based on the ``Circle``\'s ``radius``
* Consider the ``diameter`` method below that we could add to the ``Circle`` class below ``__init__``

.. code-block:: python
    :linenos:

    class Circle:

        # init and/or other methods not shown for brevity

        def diameter(self) -> float:
            """
            Calculate and return the diameter of the Circle based on its radius.

            :return: diameter of the Circle
            :rtype: float
            """
            return 2 * self.radius


* The method itself is not overly sophisticated --- the diameter of a circle is twice its radius
* But you will notice, once again, the use of ``self``

    * Every method that belongs to the class must start with ``self`` in the parameter list
    * Since we are accessing the specific ``Circle`` object's ``radius``, we make use of the reference variable ``self``

* The following two methods follow the same pattern, but perform their respective calculations

.. code-block:: python
    :linenos:

    class Circle:

        # init and/or other methods not shown for brevity

        def area(self) -> float:
            """
            Calculate and return the area of the Circle based on its radius.

            :return: Area of the Circle
            :rtype: float
            """
            return math.pi * self.radius**2

        def circumference(self) -> float:
            """
            Calculate and return the circumference of the Circle based on its radius.

            :return: Circumference of the Circle
            :rtype: float
            """
            return 2 * math.pi * self.radius


* To make use of these methods, we call the method on the specific ``Circle`` object we want

.. code-block:: python
    :linenos:

    circle_a = Circle(1)
    circle_b = Circle(5)

    print(circle_a.area())              # Results in 3.141592653589793
    print(circle_b.circumference())     # Results in 31.41592653589793


* In the above example, notice how the methods are called with parentheses

    * Also notice that, although the methods in the ``Circle`` class have the ``self`` variable specified in its parameter list, no actual value is explicitly passed as an argument

* When calling ``circle_a.area()``, I am asking the ``Circle`` object referenced by ``circle_a`` to calculate and return its area
* Similarly, when calling ``circle_b.circumference()``, I am asking the instance ``circle_b`` to calculate and return its circumference

.. note::

    Consider ``circle_a.area()``. The variable ``circle_a`` is a reference to some ``Circle`` object, and I am asking
    for that instance to calculate and return its ``area``. Here, ``circle_a`` and the ``self`` variable from within the
    ``Circle`` class are referencing the same ``Circle`` object. When looking at the ``area`` method's code, it makes
    use of its attribute ``radius``, which is accessed via a reference variable to the instance of the ``Circle`` object
    the method was invoked on --- ``self``.


Testing the Class
-----------------

* As always, we want to ensure our programs are correct, so we will write some tests
* Unlike the ``assert`` tests we have done so far, we need to create instances of the objects first before we can test them

.. code-block:: python
    :linenos:

    circle_0 = Circle(0)
    assert 0 == circle_0.radius
    assert 0 == circle_0.diameter()
    assert 0 == circle_0.area()
    assert 0 == circle_0.circumference()

    circle_10 = Circle(10)
    assert 10 == circle_10.radius
    assert 20 == circle_10.diameter()
    assert 0.001 > abs(circle_10.area() - 314.1592)
    assert 0.001 > abs(circle_10.circumference() - 62.8319)


For Next Class
==============

* Download and look through the :download:`Circle class <../../../src/circle.py>`
* Read `Chapter 16 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html>`_