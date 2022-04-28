*******
If/Else
*******

.. admonition:: Activity

    Using only what we have learned so far, write a function ``smush(a_number)`` that checks if the number is
    positive or negative. If ``a_number`` is positive, the function will return half the value of ``a_number``. If
    the number is not positive, simply return ``a_number``.


Conditional Expressions
=======================

* Booleans were discussed in the previous topic

    * We discussed them as a type
    * How to use Boolean operators
    * How to use comparison operators

* But Booleans allow us to do a lot more than just evaluate an expression to ``True``/``False``
* Consider ``smush`` from the above activity
* We know how to *ask* if ``a_number`` is positive

    * ``a_number > 0``

* The key now is to tell Python that, ``if`` some condition is ``True``, do something

.. code-block:: python
    :linenos:
    :lines-emphasis: 11

    def smush(a_number: float) -> float:
        """
        Returns half the value of the parameter a_number if the value is positive,
        otherwise, return the value of a_number.

        :rtype: float
        :param a_number: Some arbitrary number.
        :return: Half of a_number when it is positive, a_number when not positive.
        """
        return_value = a_number
        if a_number > 0:
            return_value = return_value / 2
        return return_value


    # Tests for smush
    assert 5 == smush(10)
    assert -10 == smush(-10)
    assert 0 == smush(0)


* In the above example we made use of an ``if`` statement
* When the evaluated Boolean value after the ``if`` is ``True``, the indented code is executed, otherwise the indented code block is ignored

* If we follow the code within the function when ``a_number`` is ``10``, the execution is as follows

    * Assign the value of ``a_number`` (``10``) to ``return_value``
    * Evaluate ``a_number > 0``

        * ``10 > 0``
        * ``True``

    * Since the expression evaluated to ``True``, the indented code is run
    * Divide ``return_value`` by ``2`` and assign it back into ``return_value``
    * Return the value stored in ``return_value`` (``5``)


* Similarly, if we follow the code when ``a_number`` is ``-10``, the execution is as follows

    * Assign the value of ``a_number`` (``-10``) to ``return_value``
    * Evaluate ``a_number > 0``

        * ``-10 > 0``
        * ``False``

    * Since the expression evaluated to ``False``, the indented code is skipped
    * Return the value stored in ``return_value`` (``-10``)


.. admonition:: Activity

    Write a function ``is_negative(a_number)`` that returns ``True`` if ``a_number`` is negative and ``False``
    otherwise.

   
   
Compound conditions
===================
* We can use the logical operators ``and``, ``or`` and ``not`` to combine conditions.
* The combinations can be arbitrarily complex::

    if (grade < 90 and personality_type == 'A' and desired_career == 'med school') or (grade < 100 and personality_type == 'AAA'):
        print('Time to ask for extra credit!')


.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/8OAsHilB0jw" frameborder="0" allowfullscreen></iframe>

   
   
Alternative execution
=====================
* This pattern is very common::

    if x > 10:
        do_something()
	
    if not(x > 10):
        do_something_else()

* Programmers are lazy and don't want to type the condition (here ``x > 10``) twice (this also introduces the chance for more bugs)
* So ``if`` statements have a special ``else`` statement that can go with them::

    if x > 10:
        do_something()
    else:
        do_something_else()
		
* Does exactly the same thing as the preceding code... but...
* Involves less typing and is easier to read and understand. 

.. admonition:: Activity

    Write a Python function called ``hail`` that takes an integer as its argument. If the integer is even, return the value of the integer divided by 2. If it's odd, return the value of the integer multiplied by 3 and with 1 added. 

    That is: ``n`` goes to ``2/n`` if even, ``3*n+1`` if odd. 

    **HINT**: You may want to look up the Python modulus operator: ``%``.
   
   

      .. raw:: html

      	<iframe width="560" height="315" src="https://www.youtube.com/embed/k0LcSJzANgU" frameborder="0" allowfullscreen></iframe>
		
    `This is actually some neat math stuff <https://en.wikipedia.org/wiki/Collatz_conjecture>`_

    Isn't it interesting that we're writing a function that's doing exactly what the math is saying?

   
Chains of alternatives
======================
* Sometimes a binary ``if``/``else`` isn't enough.
* What if I want several, *mutually exclusive*, alternatives?::

    if year < 1960:
        print('Jazz')
    elif year < 1980:
        print('Rock')
    elif year < 1990:
        print('Synthpop')
    elif year < 2003:
        print('Alternative')
    else:
        print('Music died when I got my first real job')

* ``elif`` is a contraction of ``else if``
* **NOTE**: Only *one* of the ``elifs`` gets executed, that's *it*. The remaining ones are completely ignored.
* You can chain as many as you want
    * If these were just ``if`` s, what would happen if ``year`` was ``1980``?
        * Let's try it quick.
* **Always** end with a plain ``else`` to catch any conditions not covered in the chain.

.. admonition:: Activity

    Write a Python function that takes an integer from 0-100 representing a course grade and returns a string representing the letter grade: A,B,C,D or F. You can pick the cutoffs.

      .. raw:: html

      	<iframe width="560" height="315" src="https://www.youtube.com/embed/-ZpxIvRshzg" frameborder="0" allowfullscreen></iframe>  
   
   
Nesting Conditionals
====================

.. image:: dolls.jpeg

* You can "nest" conditionals inside other conditionals

.. code-block:: python
    :linenos:

    # Find quadrant with 'nested If's
    if x > 0:
        if y > 0:
            print("First Quadrant")
        else:
            print("Fourth Quadrant")
    else:
        if y > 0:
            print("Second Quadrant")
        else:
            print("Third Quadrant")

* For simplicity, ignore point :math:`(0,0)` being in the third quadrant
* In the above example, we *could* have done it without nesting by using ``and``\s
* But some may find the nested version of the code more intuitive and readable

.. code-block:: python
    :linenos:

    # Find quadrant with 'and's
    if x > 0 and y > 0:
        print("First Quadrant")
    elif x > 0 and y < 0
        print("Fourth Quadrant")
    elif x < 0 and y > 0:
        print("Second Quadrant")
    else:
        print("Third Quadrant")


For Next Class
==============

* Read `chapter 6 of the text <http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html>`_


