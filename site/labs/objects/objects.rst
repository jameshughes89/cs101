*******
Objects
*******

* Feel free to use your laptop if you have it
* Ensure I have recorded your completion --- failure to do so will result in a grade of 0
* I strongly encourage you to work with others in the lab

    * When you get stuck, do me a favour and ask those sitting around you for help
    * I want people to get used to working together in the labs
    * Peer teaching and peer learning is super effective

.. note::

    To obtain full marks for the lab, you must:

        #. Have completed the pre-lab exercises
        #. Have been working on the lab content
        #. Demonstrate competency in the topics


Pre Lab Exercises
=================

* Have a working implementation of the ``Circle`` class from :doc:`lecture </topics/objects/introduction>`

    * You can obtain the source code from :download:`here <../../../src/circle.py>`
    * Yes, this week's pre-lab exercise is intended to be simple
    * It will provide a nice template for all the classes you will make in this lab


Before Kattis
=============

#. Create a ``Square`` class

    * Single attribute ``side_length``
    * The constructor will take a parameter for specifying the size
    * Method for calculating ``area()``
    * Method for calculating the ``perimeter()``
    * Make instances of the class and write ``assert`` tests to verify correctness


#. Create a ``Rectangle`` class

    * Attribute for ``length``
    * Another attribute for ``width``
    * The constructor will take two parameters for specifying the size
    * Method for calculating ``area()``
    * Method for calculating the ``perimeter()``
    * Make instances of the class and write ``assert`` tests to verify correctness


#. Create a ``RectangularPrism`` class

    * Attributes for ``length``, ``width``, and ``height``
    * The constructor will take three parameters for specifying the size
    * A method for calculating ``surface_area()``
    * A method for calculating ``volume()``
    * Make instances of the class and write ``assert`` tests to verify correctness


#. Create a ``Person`` class

    * Attribute for ``first_name``
    * Attribute for ``last_name``
    * Attribute for ``email_address``
    * The constructor will take three parameters for specifying the values of the attributes
    * A method returning a string of their ``full_name()`` --- e.g. ``Bob Smith``
    * Make instances of the class and write ``assert`` tests to verify correctness


#. Create unittest classes for each of the above classes

    * Write tests for each of the methods in each class
    * Be sure to reference the :doc:`unittest topic </topics/testing/unittest>`
    * You may find the ``Circle`` class' :download:`unittests helpful <../../../test/test_circle.py>`

        * Be sure to remove the ``from src.circle import Circle`` line

    * Run the tests with ``unittest.main(argv=[''], verbosity=2, exit=False)``
    * Ensure all tests pass

Kattis Problems
===============

* You should be using a scrap piece of paper to work out the ideas for the following problems

    * The problems you are to solve are getting too complex to try to solve by just coding
    * Trying to solve problems by just typing away will not yield success


#. https://open.kattis.com/problems/everywhere
#. https://open.kattis.com/problems/babelfish
#. https://open.kattis.com/problems/oddmanout
#. https://open.kattis.com/problems/securedoors
#. https://open.kattis.com/problems/modulo


.. warning::

    Ensure that your your completion has been recorded. Failure to do so may result in a grade of 0.