*****
Input
*****

* We know how to get information *out* of the program
    * ``print``
* And there is a similarly simple way to get information *into* the program
    * ``input``


.. code-block:: python
    :linenos:

    my_inputted_value = input('give me a value: ')

* If you run the above code, you will see ``give me a value: ``
* Python will wait for the user to enter the value they want
* Once the user enters the value, it will be stored in the ``my_inputted_value`` variable

* The string between the parentheses is what will be displayed to the user, but it is entirely optional
    * ``my_inputted_value = input()``
    * If you do leave it blank, nothing will be displayed to the user (this is what we will want when using Kattis)

.. admonition:: Activity

    #. Read in some value into the computer.
    #. Print out the value you inputted.
    #. What is the type of the value? How can I test this?
        * **Hint:** ``type``


The Type Of The Inputted Value
==============================

* What if we want it to be an int?

    >>> my_value = input('give me a value: ')
    >>> my_value = int(my_value)

or

    >>> my_value = int(input('give me a value: '))


* We can actually use this idea to convert types.
   * int will convert something to an int
   * str will convert something to a string
   * float will convert something to a float

but...

    >>> int('hi')
    ValueError: invalid literal for int() with base 10: 'hi'

So it will only work if it's a valid thing to ask

   
For next class
==============

* Read the rest of `chapter 2 of the text <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html>`_
* Read `chapter 4 of the text <http://openbookproject.net/thinkcs/python/english3e/functions.html>`_
