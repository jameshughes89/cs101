***************
Data Structures
***************

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

#. Have all classes from the previous lab complete
#. `Chapter 15 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html#exercises>`_

    * 6


#. Write *unit tests* for the class

    * Writing tests for collections can be difficult, so do your best
    * Use the `CountryCatalogueTest` class as an example from assignment 4.



Before Kattis
=============

#. Have a complete ``Person`` class from the previous lab
#. Write a ``Contacts`` class that will manage a collection of ``Person`` objects

    * The class will keep track of many instances of ``Person`` objects
    * A method for getting the ``size()`` of the ``Contacts``
    * No duplicate/equivalent ``Person`` objects are allowed to be in the collection
    * A method for adding a ``Person`` to the ``Contacts`` called ``add`` that takes a ``Person`` as a parameter

        * If someone tries to ``add`` a duplicate/equivalent ``Person``, the method should ``raise`` a ``ValueError``


    * A method to remove a ``Person`` called ``remove`` that takes a ``Person`` as a parameter (the one to be removed)

        * If someone tries to ``remove`` a nonexistent ``Person``, the method should ``raise`` a ``ValueError``


    * A ``__repr__`` that returns a string containing the details of all ``Person`` objects

        * Be sure to make use of the ``Person`` class' ``__repr__`` method


    * Make an instance of the class, add/remove ``Person`` objects to it, and write ``assert`` tests to verify correctness


#. Create unittest classes for the ``Contacts`` class

    * Write tests for each of the methods in each class
    * You may find the ``Course`` class' :download:`unittests helpful <../../../test/test_course.py>`
    * Run the tests with ``unittest.main(argv=[''], verbosity=2, exit=False)``
    * Ensure all tests pass



Kattis Problems
===============

Go back and work on Kattis problems from previous labs that you have yet to solve. I'm betting there are several of the
earlier ones you can revisit and solve. Remember, the Kattis problems are great for practice, and practice is the only
way to get better at programming.
