*****
Loops
*****

* ``if``/``else`` are great for having a block of code run when some condition is ``True``
* Sometimes we need a block to repeatedly run *while* some condition is ``True``


Reusing Variables
=================

* Before we look at loops, consider the following code

.. code-block:: python
    :linenos:

    a = 5
    print(a)

    b = 6
    print(a)

    a = a + b
    print(a)

    a = 3
    a = a + 1
    print(a)


.. admonition:: Very Quick Activity

    What is the value of ``a`` at each print statement? In other words, ``a`` is printed out four times --- what values
    are printed out?


* The point being emphasized is that there is nothing stopping us from reusing variables

    * Assign a value to some variable
    * Update/change the value stored in that variable


* A very common pattern for incrementing the value of some variable in programming is as follows

.. code-block:: python
    :linenos:

    a = a + 1

* The above example sill add one to whatever value is stored in ``a`` and then store that new value back to ``a``
* For example

    * If ``a`` starts with the value ``5``
    * Calculate ``a + 1``, which is ``6`` in this example
    * Store the newly calculated value of ``6`` in ``a``

* This and similar pattens are so common that many programming languages have shorthands for this


.. code-block:: python
    :linenos:

    a += 1      # Effectively the same as a = a + 1

* The above example is effectively identical to the previous
* It means, add ``1`` to ``a`` and put the newly calculated value back into ``a``


.. admonition:: Activity
    :class: activity
    
    Start with ``a = 5``.

    #. Figure out what ``a += 2`` does.
    #. See what happens when you use ``a *= 2``.
    #. Try other operators to see what works.


While loops
===========

* So far, if we need to run the same code multiple times, we repeat the code as many times as we need

    * For example, if I wanted to ``print("Hello, world!)`` five times, I need to write that print statement 5 times

* The trouble with this is

    * It's annoying
    * It doesn't scale well
    * It's prone to errors
    * It will not work for some variable number of times

        * For example, what if I want to print ``n`` times where ``n`` is some parameter to a function

* This is where the ``while`` statement comes in
* It will repeat some code ``while`` some condition is ``True``

.. code-block:: python
    :linenos:

    counter = 0
    while counter < 10:
        print(counter)
        counter += 1


* The above example will print out the numbers ``0`` -- ``9``

    * We initialized a ``counter`` variable outside the loop
    * The ``while`` has a conditional expression that gets evaluated
    * If it is evaluated to ``True``, the indented code runs

        * ``print`` out the value of ``counter``
        * Increment the value of ``counter``
        * Repeat the loop until the condition is ``False``


.. admonition:: Activity
    :class: activity

    What would happen if ``counter += 1`` was not included in the loop? Try to answer based on what you know. Confirm
    what happens by trying to run the code.


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/I3wMZ5jkiyc" frameborder="0" allowfullscreen></iframe>


Tracing Through A Function By Hand
----------------------------------

* Trace through the below code by hand for a few values of ``n``
* See if you can figure out what this function is doing

.. code-block:: python
    :linenos:

    def trace_through_me_by_hand(n: int) -> int:
        result = 1
        while n > 1:
            result = result * n
            n -= 1
        return result


* ``while`` loops can get complex quickly (if only there were comments)
* When tracing through the code, don't try to do it all in your head
* Create a table to keep track of the values
* Below is an example with ``trace_through_me_by_hand(4)``

+------------------------+---------------+
|          n             | result        |
+========================+===============+ 
|          4             | 1 -> 4        |  
+------------------------+---------------+ 
|          3             | 4 -> 12       |  
+------------------------+---------------+ 
|          2             | 12 -> 24      |  
+------------------------+---------------+ 
|          1             | Stop          |  
+------------------------+---------------+ 


.. admonition:: Activity
    :class: activity

    Write a function called ``int_sum(n)`` that takes a single integer ``n`` as a parameter and returns the sum of all
    the numbers between ``0`` and ``n`` inclusively (include ``n`` in the summation).

    When you finish writing the function, do not run it right away --- trace through the program by hand like with the
    ``trace_through_me_by_hand`` above.

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/sUNBswKrmJY" frameborder="0" allowfullscreen></iframe>


.. admonition:: Activity
    :class: activity

    Create a new function called ``int_sum_print`` that is the same as ``int_sum``, however this function should
    ``print`` out the values of all the variables each time in the loop. Ideally this should be formatted similar to the
    table created with ``trace_through_me_by_hand``, but do not worry too much about how the ``print``\s format the
    output.


Iterative Methods
=================

* Below is an example of *Newton's Method*, which is a handy strategy for approximating roots
* The point of this example is to see how we can use a loop to perform Newton's Method

    * The point is **not** to focus too much on the math or Newton's Method itself

.. admonition:: Activity
    :class: activity

    Find the solution to the equation :math:`3x^{3} + 2x^{2} = x + 10`. In other words, for what value of :math:`x` is
    this true?


Newton's Method
---------------

* To start, since we want to know when the left-hand and right-hand sides are equal, we want to know when their difference is zero
* We can re-arrange the equation

    :math:`3x^{3} + 2x^{2} = x + 10`

    :math:`3x^{3} + 2x^{2} - (x + 10) = 0`

    :math:`3x^{3} + 2x^{2} - x - 10 = 0`


* Turns out there is an iterative algorithm we can follow to find an approximation to this equation

   
* Okay, that's a tough one, so you get some help. How do we go about it?
* Let's use something called `Newton's Method <http://en.wikipedia.org/wiki/Newton's_method>`_ .
* Since I promised this is a no-prerequisite course...
* Here's what you do:
    * Pick a value ``x`` between 0 and 1. Any will do. Seriously.
    * Compute: 
        * .. image:: xminuscosxminusxqueu.png
    * The answer to that equation is an *approximation* of the solution
    * It's not a very *good* approximation yet. What to do?
    * Set ``x`` equal to the new approximation and plug in to the formula again.
    * Presto! New approximation.
    * Still not good enough? Guess what?
    * Set ``x`` equal to the new approximation and plug in to the formula again.

* What you want to do is:
    * write a function ``approx_x`` that, given an approximation for x, computes the formula I gave you
    * write another function, that calls this function ``while x != approx_x``

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/9jrhr9rbwzc" frameborder="0" allowfullscreen></iframe>

Algorithm
=========

* What you just saw, Newton's method, is an example of an **algorithm**.
* An algorithm is a description of a series of steps to solve a problem.
* Algorithms can be presented in natural language, but are easier to turn into a program when presented in a formal language.
* Finding an algorithm to solve most problems is *very hard*. You can make a career, get tenure, make millions of dollars in patent licensing, etc., "just" by developing algorithms.
* As programmers though, we usually leverage existing algorithms and other things to make our lives easier. We often won't be starting from scratch (although, right now you are...)
* The two most important concepts you will learn in this course (or really, what a computer scientist spends years learning) are:
    * **ALGORITHM**
    * **DATA STRUCTURE**
* So we're half done! (Just kidding)

.. admonition:: Activity
    :class: activity 

    Write down (in English) an algorithm for printing out the sum of all the even numbers between 1 and ``n``. 

    Now convert the algorithm into a Python function. 

    Test it.
   
  

For next class
==============

* Read `chapter 8 of the text <http://openbookproject.net/thinkcs/python/english3e/strings.html>`_


