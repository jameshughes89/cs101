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

 
   
Compound Conditions
===================

* When we make use of an ``if`` statement, the value being checked needs to ultimately be evaluated to a Boolean
* This means that we can make use of more complex compound Boolean expressions

    * Comparison operators
    * Arithmatic operators
    * Boolean operators

.. code-block:: python
    :linenos:
    :lines-emphasis: 10

    def three_five_divisible(a_number: float) -> str:
        """
        Checks if a number is divisible by both three and five. If it is, return
        a string "It is!", otherwise "Nope".

        :rtype: str
        :param a_number: Some arbitrary number.
        :return: String indicating if the number is divisible by three and five
        """
        if a_number % 3 == 0 and a_number % 5 == 0:
            return "It is!"
        return "Nope"


    # Tests for three_five_divisible
    assert "It is!" == three_five_divisible(0)
    assert "It is!" == three_five_divisible(15)
    assert "It is!" == three_five_divisible(-30)
    assert "Nope" == three_five_divisible(3)    # Divisible by 3 but not 5
    assert "Nope" == three_five_divisible(-50)  # Divisible by 5 but not 3
    assert "Nope" == three_five_divisible(1)    # Divisible by neither


.. note::

    The modulo operator ``%`` (often called just "mod") effectively does division and returns the **remainder**. For
    example, ``10 % 3`` is ``1`` since ``10/3`` is ``3`` remainder ``1``.

    In the ``three_five_divisible`` example, we are checking if the remainder of the division is ``0``, which would mean
    that the value can be evenly divided.

    Another common use of ``%`` is checking if a value is even or not --- ``x % 2`` is ``0`` when ``x`` is even since
    it would mean that ``x`` can be evenly divided by ``2``.


* The above function ``three_five_divisible`` needs to check if a number is divisible by 3 ``and`` 5
* This means that there are two conditions we need to check for being ``True``

* If we follow the code within the function when ``a_number`` is ``15``, the execution is as follows

    * Evaluate ``a_number % 3 == 0 and a_number % 5 == 0``

        * ``15 % 3 == 0 and 15 % 5 == 0``
        * ``0 == 0 and 0 == 0``
        * ``True and True``
        * ``True``


    * Since the expression evaluated to ``True``, the indented code is run
    * Return ``"It is!"``, function ends

* If we follow the code within the function when ``a_number`` is ``9``, the execution is as follows

    * Evaluate ``a_number % 3 == 0 and a_number % 5 == 0``

        * ``9 % 3 == 0 and 9 % 5 == 0``
        * ``0 == 0 and 4 == 0``
        * ``True and False``
        * ``False``

    * Since the expression evaluated to ``False``, the indented code is skipped
    * Return ``"Nope"``


.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/8OAsHilB0jw" frameborder="0" allowfullscreen></iframe>
   
   
Alternative Execution
=====================

* This pattern is very common

.. code-block:: python
    :linenos:2864

    if x > 10:
        do_something()
    if not(x > 10):
        do_something_else()


* When we have an either/or situation we make use of ``else``

.. code-block:: python
    :linenos:

    if x > 10:
        do_something()
    else:
        do_something_else()


* The two examples above will effectively do the same thing, but the 2nd is nicer

    * Write less
    * Intuitive and easy to read/understand
    * Eliminate potential bugs


.. admonition:: Activity

    Write a function called ``hail`` that takes an integer as an argument. If the integer is even, return the value of
    that integer divided by 2. If it is odd, return the value multiplied by 3 and with one added. In other words,
    given a number :math:`n`, return :math:`n/2` when it is even and :math:`3n + 1` when it is odd. **Hint:** Don't
    forget about ``%``.
   
    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/k0LcSJzANgU" frameborder="0" allowfullscreen></iframe>
		
    `This is actually some neat math stuff <https://en.wikipedia.org/wiki/Collatz_conjecture>`_. Isn't it cool that
    we're writing a Python function that's doing exactly what the math is saying?


.. note::

    If we revisit ``smush``, we can rewrite the function in a few different ways that are all correct.

    .. code-block:: python
        :linenos:

        def smush_version_2(a_number: float) -> float:
            """
            Returns half the value of the parameter a_number if the value is positive,
            otherwise, return the value of a_number.

            :rtype: float
            :param a_number: Some arbitrary number.
            :return: Half of a_number when it is positive, a_number when not positive.
            """
            if a_number > 0:
                return_value = a_number / 2
            else:
                return_value = a_number
            return return_value


    In ``smush_version_2``, an ``else`` is used and the function has only one ``return``. The use of the ``else`` here
    is not required (as seen in the original ``smush``), but the use of ``else`` in this situation may make the function
    a little clearer. Additionally, some programmers prefer having their functions have only one ``return``, but this is
    by no means *more correct*.

    .. code-block:: python
        :linenos:

        def smush_version_3(a_number: float) -> float:
            """
            Returns half the value of the parameter a_number if the value is positive,
            otherwise, return the value of a_number.

            :rtype: float
            :param a_number: Some arbitrary number.
            :return: Half of a_number when it is positive, a_number when not positive.
            """
            if a_number > 0:
                return a_number / 2
            else:
                return a_number

    Another possibility is ``smush_version_3``. You will notice how similar it is to version 2, but here we use two
    ``return``\s in the ``if`` and ``else`` blocks. Again, this is not *more correct* and it is only shown here to
    demonstrate how the same functionality can be implemented differently.

   
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

