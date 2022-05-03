*****
Loops
*****

* ``if``/``else`` are great for having a block of code run when some condition is ``true``
* Sometimes we need a block to repeatedly run *while* some condition is ``true``


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
    
    * Write a function to add ``+1`` to some variable 5 times and return the value.
    * Now do the same thing, but 10 times.
    * Now do the same thing again, but 100 times.
    * Now do the same thing again, but 736251442443 times.

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
* It will repeat some code ``while`` some condition is ``true``


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

* Consider this code::

    def do_stuff(n):
        answer = 1
        while n > 1:
            answer = answer * n
            n = n - 1
        return answer

.. admonition:: Activity
    :class: activity

    What does the code above do? Trace through it, using pen and paper, for a few example values of ``n!``

* The pattern ``a = a + 1`` shows up *so often* that Python permits a shorthand for it: ``a += 1``. If you like the shorthand, use it. If you don't: don't. It's not mandatory; just saves some typing.

* ``while`` loops can get complicated quickly. Much of the time, it is by no means obvious what they do (if only the coder wrote **comments**).
* If you're faced with such a loop, *trace* through the execution of the loop by building a table of values.
* Let's trace ``do_stuff(4)``. We'll look at the values of ``n`` and ``answer`` right after the ``while`` statement.

+------------------------+---------------+
|         n              | answer        | 
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

    Write a function ``int_sum(n)`` that takes a single integer ``n`` as a parameter and returns the *sum* of all of the numbers between ``1`` and ``n``. 

    Trace through your function for the call ``int_sum(5)``

     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/sUNBswKrmJY" frameborder="0" allowfullscreen></iframe>
 
.. admonition:: Activity
    :class: activity

    Modify ``int_sum(n)`` so that it prints out a Trace table, like the one you did by hand, every time it runs.

    Don't worry about formatting the table, just ``print`` out the values.

Encapsulation
=============
* Big word for a simple idea: take your code and "encapsulate" it in a function.
* That's it.
* Normal development process for scientific software:
    * Screw around with Python for a while
    * Get something that you like
    * Get tired of typing those commands over and over
    * *Encapsulate* that set of commands in a function
    * Back to messing around at the interpreter prompt, but with your new function
    * Get something you like
    * Get tired of typing those commands over and over...
    * ...
 
OMG some actual *science*!
==========================
* Okay, maybe not. But we're taking a step in that direction.

.. admonition:: Activity
    :class: activity

    Find the solution to the equation (for what value of ``x`` is this statement true?):
   
    * .. image:: cosx.png
   
    No need to worry about degrees/radians here. Just use ``cos`` and ``sin``.
   
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


