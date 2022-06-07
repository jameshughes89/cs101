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


Constructor/Instantiation and Attributes
========================================

* With just the ``class Circle``, we can actually start making instances of the class

.. code-block:: python
    :linenos:

    some_circle = Circle()
    print(type(some_circle))    # Results in something like <class '__main__.Circle'>


* However, this is not particularly useful as we have yet to really describe the ``Circle`` class
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

    * The ``__init__`` method is called the *instantiation* method, but is commonly referred to as the *constructor*

* We can also see that we are creating an *attribute* called ``radius`` that will have the value ``0`` upon the creation of a ``Circle`` object

* You will notice a special variable called ``self`` in the parameter list and before the attribute ``radius``

    * ``self`` is a reference variable to an instance of the class
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


* In the above example, we created two ``Circle`` objects and then assigned each their own ``radius`` value
* Both ``circle_a`` and ``circle_b`` are of the class ``Circle``, but they are two separate instances of the class

.. note::

    Consider the line ``circle_a.radius = 1``. The variable ``circle_a`` is a reference to some ``Circle`` object, and
    from that object I am assigning the value of ``1`` to that object's ``radius`` attribute. On this line of code, the
    ``self`` reference variable within the ``Circle`` class is an alias for the object referenced by ``circle_b``.
    However, on the following line, ``circle_b.radius = 5``, the ``self`` within the ``Circle`` class will be an alias
    for the object referenced to by ``circle_b``.


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


* In the above example, we include a parameter for the ``radius``, which will be used to set the attribute on instantiation
* This way we do not need to set the values ourselves after they are created, as seen in the following example

.. code-block:: python
    :linenos:

    circle_a = Circle(1)
    circle_b = Circle(5)

    print(circle_a.radius)      # Results in 1
    print(circle_b.radius)      # Results in 5



__repr__
========

There are a lot of other special functions for classes that you don't *need*, but are super handy. Here are 2 cool ones. 

    .. code-block:: python
        :linenos:
      
        def __repr__(self):
            '''
            A method which will return some string representation of the object. This will he handy for debugging and stuff.
            '''
            return 'First Name: ' + self.first_name + '\nlast_name: ' + self.last_name + '\nStudent Number: ' + self.student_num + '\nCurrent Average: ' + str(self.current_avg)

.. admonition:: Activity
    :class: activity

    1. Add this function to your code. 

    2. Now in your other script call the ``__repr__() `` method on the ``a_student`` object.

    3. Call ``print(a_student)``. What happens?
   
    4. Run this ``a = str(a_student)``, and then check out the ``type`` of ``a``. 

__eq__
======

What does it mean for 2 ``EnthusiasticStudent`` objects to be *equal*?

.. admonition:: Activity
    :class: activity

    1. Create 2 instances of an ``EnthusiasticStudent`` object. Call them ``a`` and ``b``.

    2. Call ``a == b``. What happened? How would python know what it means for two ``EnthusiasticStudent`` objects to be equal?

    3. Copy the below code and re-run. 


    .. code-block:: python
        :linenos:
      
        def __eq__(self, anotherThing):
            '''
            A method to check if 2 EnthusiasticStudent are the same. What does it mean for 2 things to be the same? 
            Well, WE get to make that up!
            (Although, we should pick something that makes sense...)
            '''
            return self.student_num == anotherThing.student_num


    4. Now call ``a.__eq__(b)``. What happens?

    5. Now call ``a == b``. What happens?


The above code may also make it somewhat obvious why the ``self`` reference is important. Which instance of the object do we want the ``student_num`` attribute from?

			
For Next Class
==============

* Read `Chapter 16 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html>`_