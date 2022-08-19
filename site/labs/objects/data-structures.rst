***************
Data Structures
***************

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

.. warning::

    You must have completed the specified exercises prior to the start of the lab. If you have not come to lab prepared,
    you will be asked to leave and you will obtain a grade of 0 for the lab.


#. Have all classes from the previous lab complete
#. `Chapter 15 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html#exercises>`_

    * 6


Before Kattis
=============

#. Add to the ``Person`` class from the previous lab

    * A reasonable ``__repr__`` method --- you can decide what the string looks like
    * A reasonable ``__eq__`` method --- you can decide what it means for two ``Person`` objects to be equivalent
    * Make instances of the class and write ``assert`` tests to verify correctness


# Write a ``Contacts`` class that will manage a collection of ``Person`` objects

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


Kattis Problems
===============

Go back and work on Kattis problems from previous labs that you have yet to solve. I'm betting there are several of the
earlier ones you can revisit and solve. Remember, the Kattis problems are great for practice, and practice is the only
way to get better at programming.

.. warning::

    Ensure that your your completion has been recorded. Failure to do so may result in a grade of 0.
