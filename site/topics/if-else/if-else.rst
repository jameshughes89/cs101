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

   
Exclusive Alternatives
======================

* Sometimes we need to check various conditions and a single ``if``/``else`` isn't enough
* For example, what if I want a function to take a percentage grade and return a letter grade

.. code-block:: python
    :linenos:

    def letter_grade_broken(percent_grade: float) -> str:
        """
        Calculate the letter grade associated with the provided percent grade.

        :rtype: str
        :param percent_grade: A grade as a percent
        :return: Letter grade for the provided percentage
        """
        letter_grade = ""
        if percent_grade >= 90:
            letter_grade = "A+"
        if percent_grade >= 80:
            letter_grade = "A"
        if percent_grade >= 70:
            letter_grade = "B"
        if percent_grade >= 60:
            letter_grade = "C"
        if percent_grade >= 50:
            letter_grade = "D"
        else:
            letter_grade = "F"
        return letter_grade

* The above example ``letter_grade_broken`` may be one of the first ideas you come up with, but unfortunately it has a problem
* If we run ``assert "A+" == letter_grade_broken(99)``

    * ``letter_grade_broken(99)`` would actually return ``"D"``

* The trick to understanding the problem is to take our time and look at the code

    * Call ``letter_grade_broken(99)``
    * ``percent_grade`` is assigned the value ``99``
    * Check if ``percent_grade >= 90``

        * ``percent_grade >= 90``
        * ``99 >= 90``
        * ``True``

    * Since the expression is evaluated to ``True``, the indented code is run
    * Assign ``letter_grade`` the value ``"A+"``
    * The execution continues
    * Check if ``percent_grade >= 80``

        * ``percent_grade >= 80``
        * ``99 >= 80``
        * ``True``

    * Since the expression is evaluated to ``True``, the indented code is run
    * Assign ``letter_grade`` the value ``"A"``
    * ...

* The trouble here is that we really only want one of these ``if`` code blocks to run

    * We want them to be *mutually exclusive* alternatives

* There are a few ways one could fix this

    * Have a ``return`` in each indented block since that would stop execution of the function once a ``return`` is reached
    * Reverse the order of the ``if``\s
    * Check upper and lower bounds (e.g. ``percent_grade >= 80 and percent_grade < 90``)

* But arguably the better way to address this is with ``elif``\s

    * Can be read as *else, if...*

* These allow us to have at most one of the code blocks in the chain of conditions to run
* In other words, as soon as one of the ``if``\s is true, all other ``if``\s are skipped and the program continues running after the ``else``
* When using ``elif``\s, always end with a final ``else``

.. code-block:: python
    :linenos:

    def letter_grade(percent_grade: float) -> str:
        """
        Calculate the letter grade associated with the provided percent grade.

        :rtype: str
        :param percent_grade: A grade as a percent
        :return: Letter grade for the provided percentage
        """
        letter_grade = ""
        if percent_grade >= 90:
            letter_grade = "A+"
        elif percent_grade >= 80:
            letter_grade = "A"
        elif percent_grade >= 70:
            letter_grade = "B"
        elif percent_grade >= 60:
            letter_grade = "C"
        elif percent_grade >= 50:
            letter_grade = "D"
        else:
            letter_grade = "F"
        return letter_grade


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/-ZpxIvRshzg" frameborder="0" allowfullscreen></iframe>
   
   
Nested conditionals
===================

* Computer scientists love "nesting" things: putting things inside other things.

.. image:: dolls.jpeg

* You can "nest" a conditional inside another conditional::

    if x > 0:
        if y > 0:
            print('First Quadrant')
        else:
            print('Fourth Quadrant')
    else:
        if y > 0:
            print('Second Quadrant')
        else:
            print('Third Quadrant')
			
* In the above example, we *could* have done it without nesting by using ``and`` and whatnot, but for fun we can nest it

* Again, no limit to how deep you nest... but mind the readability of your code!
    * Actually, technically, Python has a limit of 20 nested statements, but other languages have much deeper limits
    * In a more mathematical/theoreticaltical sense, there is no limit 

* Do not go to anyone with this::

	if a > 0:
	   if b > 0:
	      if c > 0:
	         if d > 0:
	            if e > 0:
	               if f > 0:
	                  if g > 0:
	                     if h > 0:
	                        if i > 0:
	                           if j > 0:	
	                              if k > 0:
	                                 if l > 0:
	                                    if m > 0:
	                                       if n > 0:
	                                          if o > 0:
	                                             if p > 0:
	                                                if q > 0:
	                                                   if r > 0:
	                                                      if s > 0:
	                                                         if t > 0:
	                                                            if u > 0:
	                                                               if v > 0:	
	                                                                  if w > 0:
	                                                                     if x > 0:
	                                                                        if y > 0:
	                                                                           if z > 0:
	                                                                              print('I want my TA to hate me')
	else:
	   print("I'm making a huge mistake")


Libraries
=========
* Most of you are here because you are pragmatic people who want to *get stuff done*
* The fastest way to *get stuff done* is by leveraging stuff that other people have done.
* Remember functions? Wouldn't it be awesome if there were huge collections of functions that already existed... and did a lot of the stuff you want to do? 
* Python has a *huge* variety of existing **libraries**/**packages**.
	   
	   
NumPy
=====
* The most important library for us is *Numerical Python* ("NumPy" for short).
* For anyone working with real data in Python, NumPy is awesome
* Because it isn't 'built in' to Python, we have to tell Python that we want to use NumPy:
    >>> import numpy
    

NumPy Types
===========
* Recall that Python values have types.
* NumPy defines a `whole bunch of new types <http://docs.scipy.org/doc/numpy/user/basics.types.html>`_.
* When you call NumPy functions, Python will, as always, try it's best to guess at type conversions for you.
* *but*... you can be explicit about it, too:
    >>> x = numpy.float32(7.3)
    >>> print x
    7.3
    
    >>> type(x)
    <class 'numpy.float32'>

* Check this out:
    >>> numpy.float128(3.33)
    3.330000000000000071
    >>> numpy.float64(3.33)
    3.33


* Floating point precision...
* Let's think for a second about real numbers vs. computers. 	
	

* You can convert regular Python types, and NumPy types, back and forth as you need.
* If you aren't sure what type a variable has, remember that you can always check with ``type()``

.. admonition:: Activity

    Write a Python function that takes two Python ``float`` s as inputs, converts them both into ``numpy.float32`` type and then returns the product.


For next class
==============

* Read `chapter 6 of the text <http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html>`_


