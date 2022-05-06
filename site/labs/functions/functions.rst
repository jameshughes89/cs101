*********
Functions
*********

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

#. `Chapter 2 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html#exercises>`_

    * 5 **but** have it in a function that returns the result

#. `Chapter 4 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/functions.html#exercises>`_

    * 8


Before Kattis
=============

* :doc:`If you forget how to do the function related stuff, go back to the class notes </topics/functions/functions>`

#. Write a function called ``add_five_print(some_integer)``

    * The code you write must be within a function
    * The function will take one parameter ``some_integer``
    * The function adds five to the parameter and ``print``\s out the result
    * The function will not return anything
    * Call the function a few times to verify that it works properly

    .. code-block:: python
        :linenos:

        def add_five_print(some_integer):
            # stuff goes here


#. Write a function called ``add_two_numbers_print(some_integer, some_other_integer)``

    * The code you write must be within a function
    * The function will take two parameters ``some_integer`` and  ``some_other_integer``
    * The function will calculate their sum and ``print`` out the result
    * The function will not return anything
    * Call the function a few times to verify that it works properly

    .. code-block:: python
        :linenos:

        def add_two_numbers_print(some_integer, some_other_integer):
            # stuff goes here


#. Write a function called ``add_two_numbers_return(some_integer, some_other_integer)``

    * The code you write must be within a function
    * The function will take two parameters ``some_integer`` and  ``some_other_integer``
    * The function will calculate their sum
    * The function will ``return`` the result
    * Call the function a few times to verify that it works properly


#. Run the following code and take note of the output

    .. code-block:: python
        :linenos:

        result = add_two_numbers_return(4, 5)
        print(result)


#. Run the following code and take note of the output

    .. code-block:: python
        :linenos:

        result = add_two_numbers_print(4, 5)
        print(result)


#. Why do these two functions behave differently when called?

    * Take note of when and where ``print`` is called


#. Write a function called ``this_is_tough(n1, n2, n3, n4)``

    * The code you write must be within a function
    * This function will take four parameters ``n1``, ``n2``, ``n3``, and ``n4``
    * This function will sum all four numbers
    * The function will ``return`` the result
    * You can **not** make use of the addition operator (``+``) directly within this function
    * You **must** make use of ``add_two_numbers_return`` three times
    * Verify correctness by running the function a few times


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

#. https://open.kattis.com/problems/hello
#. https://open.kattis.com/problems/carrots
#. https://open.kattis.com/problems/r2
#. https://open.kattis.com/problems/faktor
#. https://open.kattis.com/problems/ladder
#. https://open.kattis.com/problems/planina

**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
