*****************
Topic #6 -- Loops
*****************

Reusing variables
=================
* Consider this code fragment::

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

    What is the value of the variable ``a`` at the various ``print`` function in the above code?
   
* A very common pattern we'll use is incrementing a variable used as a counter::

    a = a + 1

* This reminds me of the ``+1`` thing we used to do on calculators in elementary school.

* Try this a few times::

    a += 1
   
* What does this do?

.. admonition:: Activity
    
    * Write a function to add ``+1`` to some variable 5 times and return the value.
    * Now do the same thing, but 10 times.
    * Now do the same thing again, but 100 times.
    * Now do the same thing again, but 736251442443 times.

First loops
===========

* So far, if we want Python to do the same thing over and over, we have to tell it explicitly by repeating those instructions over and over.
    * There has to be a better way!

* We want to automate the process of repeating things.
* If I can put a block of instructions into a function and call that function...
* ... why can't I put a block of instructions somewhere and say "Hey, do that block of
  instructions until I tell you to stop"?
* The ``while`` statement allows us to do exactly this.
* *While* some condition is ``true``, keep doing the code in the indented block::

    a = 1
    while a < 11:
        print(a)
        a = a + 1

* That code will print the numbers from 1 to 10. Take a minute to note three things:
    * Before the ``while`` statement, we *initialize* the loop variable ``a``
    * The ``while`` statement is followed by a condition (which can be any boolean function/statement/expression!). If the condition is ``True``, the body of the loop gets executed, otherwise it gets skipped. (don't forget the ``:`` !)
    * What would happen if we didn't have ``a = a + 1``?

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/I3wMZ5jkiyc" frameborder="0" allowfullscreen></iframe>

.. admonition:: Activity --- Featuring LOOPS

    * Write a function to add ``+1`` to some variable 5 times and return the value.
    * Now do the same thing, but 10 times.
    * Now do the same thing again, but 100 times.
    * Now do the same thing again, but 1927462829873 times....

* Consider this code::

    def do_stuff(n):
        answer = 1
        while n > 1:
            answer = answer * n
            n = n - 1
        return answer

.. admonition:: Activity

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

    Write a function ``int_sum(n)`` that takes a single integer ``n`` as a parameter and returns the *sum* of all of the numbers between ``1`` and ``n``. 

    Trace through your function for the call ``int_sum(5)``

     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/sUNBswKrmJY" frameborder="0" allowfullscreen></iframe>
 
.. admonition:: Activity

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

    Write down (in English) an algorithm for printing out the sum of all the even numbers between 1 and ``n``. 

    Now convert the algorithm into a Python function. 

    Test it.
   
  

For next class
==============

* Read `chapter 8 of the text <http://openbookproject.net/thinkcs/python/english3e/strings.html>`_


