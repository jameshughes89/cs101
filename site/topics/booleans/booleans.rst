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
    is ``True`` only when one of the statements is ``True``. Exclusive or is not going to come up in this course. It is
    only noted here since some people find ``or`` ambiguous at first.


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/NmeQHw0rOaY" frameborder="0" allowfullscreen></iframe>


* To make parts of the program *conditionally* executed, we need a *formal* way to describe conditions.
* We need: logic.
* Let's try some comparison:
    >>> 19 == 87
    False

    >>> 5 == 5
    True

* Note that ``==`` is *comparison* while ``=`` is *assignment*. They are not the same! Python will punish you if you forget this!
    * You'll all mess this up eventually
    * Just be thankful this isn't C/C++

.. admonition:: Activity

    Figure out what the other comparison operators in Python are. Hint: ``3`` doesn't equal ``5``, it is *____ than* 5.

* These operators can be applied to any two expressions (could be simply a value or variable, but can be more complex):
    >>> a = 15
    >>> b = 37
    >>> (a+b)*9 > (b-a)*3 + 2
    True

* What is the *type* of the result of applying a comparison operator?





The Boolean type
================
* A value that is either ``True`` or ``False`` (and nothing else) has type `Boolean <http://en.wikipedia.org/wiki/George_Boole>`_.
* We've used comparison operators (e.g., ``<, >, ==``) in conditionals.
* What's going on "under the hood" with the comparison, though?
    >>> 5 > 2
    True
    
    >>> 5 < 2
    False
	
* A comparison like ``a > b`` is just an *expression*, like ``a + b``.
* The difference is that the value it produces isn't an integer, it's either ``True`` or ``False``
* This may seem like a subtle thing, but it's a big deal:
    * An operator that takes 2 numbers and produces a number: 
        * `1 + 1 -> 2`
    * An operator that takes 2 booleans and produces a boolean: 
        * `True and False -> False`
    * An operator that athes 2 numbers and produces a boolean: 
        * `1 < 2 -> True`
   

    >>> type(5 > 2)
    <class 'bool'>

.. admonition:: Activity

    Write a function ``is_negative(n)`` that *returns* ``True`` if the argument ``n`` is negative and ``False`` otherwise.

    Verify that the return type is correct.

     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/xrBzzvmLCvQ" frameborder="0" allowfullscreen></iframe>   


More about returns
==================

* We've already seen that functions can return a value at the end.
* In fact, a function can return a value *at any time*, not just the end.
* We can take advantage of this fact to have multiple returns!::

    def divisible_by(a, b):
        if a % b == 0:
            return True
        else:
            return False

.. admonition:: Activity

    * What is the result of the function call ``divisible_by(4, 2)``? 
    * How about ``divisible_by(4, 3)``? 
    * Now write a new function ``not_divisible_by(a, b)`` that returns ``True`` when ``a`` is *not* divisible by ``b`` and ``False`` otherwise.
    * Now write this function to do the same thing with only **1** return statement.
    * Now write it with only **1** line of code within the function (so, 2 lines including the function header).
   
* Functions returning Boolean values are pretty handy. Why? Where do you see yourself using them?


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

    The last two examples are quite contrived and are entirely unrealistic to use. These were simply used here to
    demonstrate the evaluation of the expressions. If you find yourself writing long boolean expressions like this, you
    are likely doing something wrong.


For Next Class
==============

* If you have not yet, read `Chapter 5 of the text <http://openbookproject.net/thinkcs/python/english3e/conditionals.html>`_