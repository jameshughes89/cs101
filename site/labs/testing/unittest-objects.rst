*******
Objects
*******

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

* Have the previous lab complete



Before Kattis
=============

#. Create a ``Person`` class

    * Attribute for ``first_name``
    * Attribute for ``last_name``
    * Attribute for ``email_address``
    * The constructor will take three parameters for specifying the values of the attributes
    * A method returning a string of their ``full_name()`` --- e.g. ``Bob Smith``
    * Write a reasonable ``__eq__`` method
    * Write a reasonable ``__repr__`` method
    * Make instances of the class and write ``assert`` tests to verify correctness


#. Create unittest classes for the ``Person`` class

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
