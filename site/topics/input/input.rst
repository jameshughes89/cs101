************************
Input and Changing Types
************************

* We know how to get information *out* of the program

    * ``print``

* And there is a similarly simple way to get information *into* the program

    * ``input``


.. code-block:: python
    :linenos:

    my_inputted_value = input("give me a value: ")

* If you run the above code, you will see ``give me a value:``
* Python will wait for the user to enter the value they want
* Once the user enters the value, it will be stored in the ``my_inputted_value`` variable

* The string between the parentheses is what will be displayed to the user, but it is entirely optional

    * ``my_inputted_value = input()``
    * If you do leave it blank, nothing will be displayed to the user (this is what we will want when using Kattis)

.. admonition:: Activity
    :class: activity

    #. Read in some value into the computer.
    #. Print out the value you inputted.
    #. What is the type of the value? How can I test this?

        * **Hint:** ``type``


The Type Of The Inputted Value
==============================

* Whenever data is input like this, Python will always assume the data is a string

    * If you enter ``Hello world``, the value of ``my_inputted_value`` would be the string ``"Hello world"``
    * If you enter ``1``, the value of ``my_inputted_value`` would be the string ``"1"``

* This may be fine in some cases, but if we want to input numbers for the purpose of doing some math, this is a problem
* Fortunately, there is a simple way to *try* to change the type of the value
* For example, if we want to enter the integer ``1``

.. code-block:: python
    :linenos:

    my_value_as_string = input("give me a value: ")
    my_value_as_int = int(my_value_as_string)

* In the above example, on the first line of code, if we enter ``1`` as the input, the value of ``my_value_as_string`` will be the string ``"1"``
* On the next line of code we are then taking the value of ``my_value_as_string`` (``"1"``) and converting it to an integer with ``int(...)``
* After everything, the value of ``my_value_as_int`` will be the integer ``1``

* Note that writing ``my_value_as_int = int(input("give me a value: "))`` would achieve the same thing, but on one line of code

    * Removing the middleman (``my_value_as_string``)


Changing Types
==============

* It is possible to use the same idea to convert the types of values, not just when inputting
* For example, if I had the integer ``1`` stored in ``some_integer``, but wanted it to be a string, I could write ``str(some_integer)``

* ``int`` is used to convert something to an integer
* ``str`` is used to convert something to a string
* ``float`` is used to convert something to a float

* However, this assumes that the value whose type is being changed can actually be changed to that type
* Python is happy to change the type of the integer ``1`` to a float or a string
* But if I try to change the type of ``"Hello world"`` to an integer, that's going to be a problem

    * ``int("Hello world")`` will cause an error
    * Python will even say ``ValueError: invalid literal for int() with base 10: 'Hello world'``


.. admonition:: Activity
    :class: activity

    Write a program to:
    
    #. Ask the user to input their weight in pounds and save the value to variable
    #. Convert the inputted value to a float and save the result to a variable
    #. Calculate the mass of the individual in kilograms based on the inputted weight and save the result to a variable
    #. Print out the mass in kilograms

    **Hint:** :math:`1 lbs = 0.453592 kg`


For Next Class
==============

* Read `Chapter 4 of the text <http://openbookproject.net/thinkcs/python/english3e/functions.html>`_
