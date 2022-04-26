*******************
Propositional Logic
*******************

* Sometimes things are ``True`` or ``False``

    * This course focuses on introductory computer science --- ``True``
    * This topic is titled "Not Logic" --- ``False``

* This is rather intuitive since you use this type of simple logic in every day life to make decisions
* Additionally, you are already familiar with some *operators* we can use on these ``True``/``False`` statements

    * ``and``
    * ``or``
    * ``not``


Truth Table
===========

.. list-table:: Truth Table
    :widths: 50 50 50 50 50
    :header-rows: 1

    * - A
      - B
      - A ``and`` B
      - A ``or`` B
      - ``not`` A
    * - ``True``
      - ``True``
      - ``True``
      - ``True``
      - ``False``
    * - ``True``
      - ``False``
      - ``False``
      - ``True``
      - ``False``
    * - ``False``
      - ``True``
      - ``False``
      - ``True``
      - ``True``
    * - ``False``
      - ``False``
      - ``False``
      - ``False``
      - ``True``


* The above *truth table* is a rather formal representation of some everyday ideas
* To put it slightly different

    * Is *the sky blue* ``and`` is *water wet*? --- ``True``
    * Is *the sky blue* ``and`` is it *over 100 degrees Celsius outside*? --- ``False``
    * Is *the sky blue* ``or`` is it *over 100 degrees Celsius outside*? --- ``True``
    * Is it ``not`` *over 100 degrees Celsius outside*? --- ``True``
    * Is *the sky blue* ``and`` is it ``not`` *over 100 degrees Celsius outside*? --- ``True``


* You may have observed that

    * For ``and``, both statements must be ``True`` to produce ``True``, otherwise it is ``False``
    * For ``or``, only one statement must be ``True`` to produce ``True``, otherwise it is ``False``
    * ``not`` changes ``True`` -> ``False`` and ``False`` -> ``True``

.. note::

    For ``or``, both statements being ``True`` produces ``True``. There is another operator called *exclusive or* that
    is ``True`` only when one of the statements is ``True``. Exclusive or is not going to come up in this course and it
    is only noted here since some people find ``or`` ambiguous at first.


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/NmeQHw0rOaY" frameborder="0" allowfullscreen></iframe>


Boolean Type
============

* `Booleans <http://en.wikipedia.org/wiki/George_Boole>`_ are a type in Python, like integers, strings, and floats

    * ``type(True)`` gives us ``bool``

* Unlike integers, strings, and floats which can take on many different values, booleans can only be one of two values

    * ``True``
    * ``False``


Boolean Operators
-----------------

* Just like the arithmatic operators we use on integers and floats, Booleans have operators too

    * The ones we just used

        * ``and``
        * ``or``
        * ``not``

* Consider the arithmatic operator ``+``

    * It takes two number *operands*
    * It produces a new number as a result
    * e.g., ``1 + 2`` is ``3``

* For Booleans, consider ``and``

    * It takes two *Boolean* operands
    * It produces a new Boolean as a result
    * e.g., ``True and False`` is ``False``


Comparison Operators
--------------------

* As you have probably noticed, asking ``True and False`` is not overly helpful as it is
* Based how we use this logic in real life, we need a way to evaluate statements into their Boolean values
* For example, is it ``not`` *over 100 degrees Celsius outside*?

    * We need a way to check if the given temperature is greater than 100 degrees Celsius

* For these situations, we make use of comparison operators you already use in your everyday life

    * Is five greater than three?
    * ``5 > 3`` is ``True``

* More generally, these comparison operators take values to be compared
* Consider the greater than (``>``) comparison operator

    * It two values as operands
    * It produces a Boolean as a result
    * e.g., ``1 > 7`` is ``False``

* The comparison operators we make use of are

    * Equal ``==``
    * Not equal ``!=``
    * Greater than ``>``
    * Greater than or equal ``>=``
    * Less than ``<``
    * Less than or equal ``<=``

.. admonition:: Activity

    Play around with the above operators on different integers and see if you can find operands that produce
    ``True``/``False`` for each.

    Play around with the operators on different types. For example, what happens when you compare Booleans, floats, and
    strings?


.. warning::

    Mind the use of two equal signs (``==``) for checking equality. Remember, a single equals sign (``=``) is the
    assignment operator.

        * ``some_variable = 5`` assigns the value ``5`` to the variable ``some_variable``
        * ``some_variable == 5`` checks if the value stored in ``some_variable`` is equal to the value ``5``


Composing Operators and Values
==============================

* We have seen different operators that work on different types
* As long as the types check out and we follow the `order of operations <https://docs.python.org/3/reference/expressions.html#operator-precedence>`_, we can compose rather complex expressions

    * Don't worry about memorizing the order of operations
    * They follow what you are used to for the most part
    * When in doubt, make use of parentheses


Evaluating Example Expressions
------------------------------

**``((17 + 2) < 18) or (17 != 18)``**

``(19 < 18) or (17 != 18)``

``False or (17 != 18)``

``False or True``

``True``


**``(101 == 100) and  ((66 - 17) < 54))``**

``False and ((66 - 17) < 54)``

``False and (49 < 54)``

``False and True``

``False``

* Once we evaluated ``(101 == 100)`` as ``False``, we didn't need to evaluate the remainder of the expression
* With ``and``, if one of the operands are ``False``, the whole expression evaluated to ``False``


**``(14 > 0) or ((6 != 7) and ((4 + 17) < 20))``**

``True or ((6 != 7) and ((4 + 17) < 20))``

``True or (True and ((4 + 17) < 20))``

``True or (True and (21 < 20))``

``True or (True and False)``

``True or False``

``True``

* Notice that once we evaluated ``(14 > 0)`` as ``True``, we really didn't need to finish evaluating the remainder of the expression
* This is because, as long as one of the operands for an ``or`` is ``True``, we know the whole expression is ``True``

.. warning::

    If you find yourself writing long and complex boolean expressions, chances are you are doing something wrong. Even
    if we have a long list of conditions you need to check in your program, there are ways to make them more manageable
    and easier to follow.


For Next Class
==============

* If you have not yet, read `Chapter 5 of the text <http://openbookproject.net/thinkcs/python/english3e/conditionals.html>`_