*********
Debugging
*********

* At this stage we have written quite a few algorithms
* We have also gotten comfortable writing assertion tests for our algorithms
* By this point, we have also seen plenty of bugs

    * Having bugs in your code is normal
    * Debugging is a large part of programming
    * Finding and fixing bugs is part of the process

* You have probably already started developing your own debugging habits
* In this topic, we will look at a few accessible debugging strategies

* Before getting started, it is worth emphasizing what this is all about

    * It's not just about getting your program to work
    * It's about understanding your program and understanding why it is behaving the way it is


.. image:: debugging_bug.png


The Importance of Debugging
===========================

* As programs get more complex, errors can become harder to track down
* No matter how experienced you are, debugging remains part of programming
* Beyond the obvious benefit of fixing your code, debugging helps us improve many important skills:

    * Knowledge of algorithms
    * Knowledge of the programming language
    * The ability to reason logically
    * The ability to reason about flow of execution in code


Error Messages
==============

* In many cases, Python will generate an error message giving you an idea of what went wrong
* Sometimes these error messages are very helpful

.. code-block:: python

    line 17
    print(5 + 5 +)
                ^
    SyntaxError: invalid syntax


* Other times the error messages are less clear

    * Often, you can search for the error message and find an explanation

* Common error messages you will come across are

    * Syntax errors
    * Indentation errors
    * Name errors
    * Type errors
    * Index errors


Syntax Errors
-------------

* Syntax errors often produce fairly helpful messages
* These messages typically tell you where the error is, as seen in the above example
* Usually, the main job is to read what Python is telling you

.. admonition:: Activity
    :class: activity

    See if you can find all the errors in the following example. You may be able to find them just by looking at the
    code, but feel free to copy/paste the code into Colab to see what Python reports.

    .. code-block:: python
        :linenos:

        deff borken(a(
            a = a + * 3
            walrus
            return a + 2

        broken(5)



Type Errors
-----------

* As we have seen, Python is pretty good about figuring out types

.. code-block:: python
    :linenos:

    a = 5           # It's an integer
    b = 5.5         # Float since there is a decimal
    c = a + b       # Mixing types in the expression (int and float), but no big deal
    print(c)        # Results in 10.5


* But Python can only do so much
* For example, Python cannot figure out what it should mean to add an integer and a string together

    * Think about it this way: what would it mean for ``"Hello" / 32``?


.. code-block:: python
    :linenos:

    print(99 + "bottles of beer on the wall")
    TypeError: unsupported operand type(s) for +: 'int' and 'str'



* Sometimes a type-related issue does not generate an error message
* Consider the ``inconsistent`` function defined in the following example

    .. code-block:: python
        :linenos:

        def inconsistent(a, b):
            return a + b


* There is nothing wrong with this function, but notice what happens with these two calls

    * ``inconsistent(1, 1)`` returns ``2``
    * ``inconsistent("1", "1")`` returns ``"11"``


* It may seem obvious to just avoid the wrong argument types
* But remember that Python's ``input`` returns a string, even if the user typed digits

    * This is a very common source of bugs




Logic errors
============

* Logic errors can be quite difficult to debug
* Everything may seem like it's working, but the program still behaves incorrectly
* Sometimes the errors may be obvious, like an infinite loop
* Sometimes they show up only in *edge cases*, so things work *most of the time*

    * Here's hoping you tested your code thoroughly

* There are a few strategies for narrowing these bugs down
* A few accessible strategies for debugging are discussed below
* Most people develop their own habits as they gain experience
* Like anything else, debugging improves with practice


Print
-----

* Probably the simplest debugging method is to call ``print`` in your code

    * Print out the value of some variable
    * Add a print to see if Python actually executed a specific code block

* Prints are useful because they let us compare what we expect with what is actually happening

.. admonition:: Activity
    :class: activity

    There is a problem with the following function. It almost works, but it is slightly off. Read the description, see if
    you can identify the issue, and then use ``print``\s to inspect values and track down the problem.

    .. code-block:: python
        :linenos:

        def sum_numbers_up_to(n: int) -> int:
            """
            This function adds up all the numbers from 0 - n exclusively.
            Eg. 5 -> 0 + 1 + 2 + 3 + 4 -> 10

            :param n: The number we are summing to. Note we do not count n
            :return: The sum of the numbers
            """

            total = 0
            c = 0
            while c < n:
                c += 1
                total += c
            return total

        assert 0 == sum_numbers_up_to(0)
        assert 10 == sum_numbers_up_to(5)



* Debugging with ``print`` often follows a simple pattern

    * Form a hypothesis about the value of a variable at a specific place in your program
    * Add a ``print`` to print out the variable's value
    * Compare your expectation with reality
    * If they matched, perhaps the problem is elsewhere
    * If they do not match, investigate why they differ

* Each ``print`` gives us a little more information
* Depending on the problem, you may need several ``print``\s

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/EnJhV2j8YR0" frameborder="0" allowfullscreen></iframe>



Pencil & Paper
--------------

* One challenge with debugging logic errors is avoiding assumptions about your code

    * Do not assume a variable has a specific value
    * Do not assume any specific functionality of a block of code

* This is easier said than done, especially when you keep rerunning your code

    * Like in the case of using ``print``

* A good alternative is to not run your program on the computer
* Instead, execute the program on paper

    * Create a table to keep track of each variable and the current value
    * *Execute* the program on paper one line at a time, keeping track of the values of the variables

* Benefits of this approach include

    * It slows you down
    * It becomes easier to *not* make assumptions
    * It requires you to be deliberate and thoughtful

* This can feel tedious, but it often helps

.. note::

    The point here is to take your time and think about every line of code. Rushing through and making assumptions will
    inevitably cause this strategy to fail.

    Remember, you are here in the first place because what your program is actually doing is different from what you
    expected --- it would be rather silly to use your incorrect assumptions about what is going on in your program to
    solve the problem caused by your incorrect assumptions.


Delta Debugging
---------------

* Another strategy is *Delta Debugging*
* Delta Debugging is a more systematic way to isolate where an issue is arising
* A simple version of the strategy is

    * Comment out every line of code and run it
    * *Un*-comment out a logical unit of code and run it

        * This should only be a line or two of code
        * You might also add a ``print``

    * Did it do what you expected?

        * No? You found at least part of the problem
        * Yes? Keep looking


* You may have realized that this is effectively the recommended coding strategy from earlier in the course

    * Write only a few lines at a time and validate that it is working correctly with tests


Rubber Duck Debugging
---------------------

* `Rubber Duck Debugging <https://en.wikipedia.org/wiki/Rubber_duck_debugging>`_
* A surprisingly effective form of debugging
* One helpful strategy is to explain your code to *something*
* Sometimes you have a friend
* Sometimes you have your mom
* Sometimes you have a pet
* And sometimes you have a rubber duck

* The point is that explaining your code out loud often helps you notice what you skipped over mentally

For Next Topic
==============

* Read `Appendix A of the text <https://openbookproject.net/thinkcs/python/english3e/app_a.html>`_
