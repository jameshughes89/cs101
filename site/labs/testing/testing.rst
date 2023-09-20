*******
Testing
*******

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

#. `Chapter 2 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html#exercises>`_

    * 5 but have it in a function that returns the result
    * Also write assertion tests for the function, include type hints, and write a docstring


#. `Chapter 4 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/functions.html#exercises>`_

    * 7 **but** write assertion tests for the function, include type hints, and write a docstring
    * 8 **but** write assertion tests for the function, include type hints, and write a docstring



Before Kattis
=============

* :doc:`If you forget how to do the testing and type hint related stuff, go back to the class notes </topics/testing/testing>`

#. Write a function to calculate the density of an object

    * :math:`d = \frac{m}{V}`
    * The function will have the mass and volume as parameters
    * The function will return the density
    * Write an effective docstring for this function
    * Include typehints for this function
    * Write assertion tests for this function


#. Write a function to calculate acceleration

    * :math:`a = \frac{u - v}{t}`
    * The function will have the starting speed, ending speed, and time as parameters
    * The function will return the acceleration
    * Write an effective docstring for this function
    * Include typehints for this function
    * Write assertion tests for this function


#. Write a function to convert latitudes/longitudes from degrees, minutes, and seconds to a decimal value of a degree

    * :math:`1 minute = \frac{1}{60} degrees`
    * :math:`1 second = \frac{1}{60} minute = \frac{1}{3600} degrees`
    * `Wikipedia explains this in more detail <https://en.wikipedia.org/wiki/Minute_and_second_of_arc>`_
    * This function will have the degrees, minutes, and seconds as parameters
    * This function will return the latitude/longitude value as degrees with a decimal
    * Write an effective docstring for this function
    * Include typehints for this function
    * Write assertion tests for this function



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


* Skip any of the following problems if you did them already.
* Although not necessary, for practice, write each solution in a function with docstrings, typehints, and assertion tests

#. https://open.kattis.com/problems/hello
#. https://open.kattis.com/problems/carrots
#. https://open.kattis.com/problems/r2
#. https://open.kattis.com/problems/faktor
#. https://open.kattis.com/problems/ladder
#. https://open.kattis.com/problems/planina
#. https://open.kattis.com/problems/leggjasaman
#. https://open.kattis.com/problems/metronome
#. https://open.kattis.com/problems/ovissa
#. https://open.kattis.com/problems/fifa
#. https://open.kattis.com/problems/vidsnuningur