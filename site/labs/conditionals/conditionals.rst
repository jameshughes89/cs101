************
Conditionals
************

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

#. `Chapter 5 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/conditionals.html#exercises>`_

    * 1
    * 2
    * 3
    * 4
    * 5
    * 10
    * 11
    * 12


#. Where appropriate, include type hints, docstrings, and assertion tests for each of your functions



Before Kattis
=============

#. Write a function ``did_pass(grade: float) -> bool:`` that returns ``True`` if the grade is 50 or above, and ``False`` otherwise

    * Be sure to write some ``assert`` tests to verify correctness


#. Write a function called ``letter_grade(percent_grade: float) -> str:`` that takes a grade as a percentage and returns the appropriate letter grade

    * 0 - 49 -> F, 50 - 59 -> D, 60 - 69 -> C, 70 - 79 -> B, 80 - 89 -> A, 90 - 100 -> A+
    * Write ``assert`` tests to verify correctness


#. Rewrite ``letter_grade(percent_grade: float) -> str:`` such that you reverse the order you check the grade in

    * For example, if you checked ``if grade < 50:`` first, start with checking for an A+
    * Run the ``assert`` tests from the previous question



Kattis Problems
===============

* Do not forget the code we used last time to read input on Kattis

.. code-block:: python
        :linenos:

        data = input()       # Read a WHOLE, SINGLE line of input
        data = data.split()  # Split string into individual pieces
        a_var = int(data[0]) # Take string from data[X], convert it to int...
        b_var = int(data[1]) # ... And store it in some variable


.. warning::

    The above code will only work when the input is 2 integers on the same line. You may need to hack this code to make
    it work for your particular problem.


#. https://open.kattis.com/problems/quadrant
#. https://open.kattis.com/problems/judgingmoose
#. https://open.kattis.com/problems/twostones
#. https://open.kattis.com/problems/spavanac
#. https://open.kattis.com/problems/cetvrta
#. https://open.kattis.com/problems/bus
