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


Algorithm
=========

* The above functions are all examples of *algorithms*
* An algorithm is a description of steps one could take to solve a given problem

    * Driving directions and cookie recipes are algorithms

* Although algorithms can be explained in a natural language like English, when programming we write our algorithms in code
* Finding an algorithm to solve a problem is non-trivial

    * You can make a career out of coming up with algorithms
    * There are certain open problems that, if you solve, will literally get you a million dollars and plenty of fame


.. admonition:: Activity
    :class: activity

    #. Write down (in English) an algorithm for calculating the sum of all the even numbers between ``0`` and ``n``.
    #. Convert the algorithm into a Python function ``sum_even_numbers(n: int) -> int``.
    #. Write some ``assert`` tests


For Next Class
==============

* Read `Chapter 8 of the text <http://openbookproject.net/thinkcs/python/english3e/strings.html>`_


