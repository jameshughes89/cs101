*********
Debugging
*********

* At this stage we have written quite a few algorithms
* We have also gotten comfortable writing assertion tests for our algorithms
* However, at this stage we've likely had more bugs than working code

    * Having bugs in your code is normal --- programmers spend more time debugging than actually writing code
    * It would be weird if you didn't have bugs
    * Remember, your code will be wrong every time you run it until it's correct

* You have probably come up with a system for debugging
* In this topic, we will discuss a few popular and accessible debugging strategies

* Before getting started however, it is important to emphasize what this is all about

    * It's not just about getting your program to work
    * It's about understanding your program and understanding why it is behaving the way it is


.. image:: hi.jpg


The Importance of Debugging
===========================

* As our programs get more and more complex, the types of errors we come across can increase in complexity
* No matter how *good* of a programmer you are, you will still spend much of your time debugging
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


* Other times the error messages are quite cryptic

    * Fortunately, you can often copy/paste the error into Google and find an explanation

* Common error messages that you will come across (if you have not already) are

    * Syntax errors
    * Indentation Errors
    * Name Errors
    * Type Error
    * Index Error


Syntax Errors
-------------

* Syntax errors will cause error messages that are often quite helpful
* These messages typically tell you where the error is, as seen in the above example
* There is not much of a debugging strategy with these errors as you just look at what Python tells you

.. admonition:: Activity
    :class: activity
   
    See if you can find all the errors in the following example. You may be able to find them all just by looking at the
    code, but feel free to copy/paste the code into Colab to see if the error messages help.

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
* For example, Python cannot suddenly figure out what it means to add an integer and a string together

    * Think about it this way, what would you say if I asked you what "Hello" divided by 32 means?


.. code-block:: python
    :linenos:

    print(99 + "bottles of beer on the wall")
    TypeError: unsupported operand type(s) for +: 'int' and 'str'



* However, sometimes we can have an issue caused by types that does not generate an error message
* Consider the ``inconsistent`` function defined in the following example

    .. code-block:: python
        :linenos:

        def inconsistent(a, b):
            return a + b


* There is nothing wrong with this function, but what would happen if you called the function with the following two sets of arguments

    * ``inconsistent(1, 1)`` returns ``2``
    * ``inconsistent("1", "1")`` returns ``"11"``


* It may seem obvious that one should just not call the function with the wrong argument types
* But also consider reading input from the user, and how Python's ``input`` returns a string, even if the inputs are numbers

    * How many times have you made the mistake in assuming the input were numbers when in fact they were strings?




Logic errors
============

* Logic errors can be quite difficult to debug
* Everything may seem like it's working, but at the end of the day, something is off
* Sometimes the errors may be obvious, like an infinite loop
* And sometimes they can be quite sneaky --- the errors can be in *edge cases*, so things work *most of the time*

    * Here's hoping you tested your code thoroughly

* There are a few strategies for distilling these bugs
* A few accessible strategies for debugging are discussed below
* Most people develop their own strategies as they gain experience
* But just like everything else, you will get better at debugging the more you practice


Print
-----

* Probably the simplest method for debugging is to call ``print`` in your code

    * Print out the value of some variable
    * Add a print to see if Python actually executed a specific code block

* Prints are great since they allow for a quick investigation into what we expect vs. what is actually happening

.. admonition:: Activity
    :class: activity

    There is a problem with the following function. It almost works, but it's slightly off. Read the description, see if
    you can identify the issue, and then make use of ``print``\s to print out the values and hopefully pinpoint and fix
    the issue.

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



* The process of debugging with ``print`` typically follows a pattern

    * Form a hypothesis about the value of a variable at a specific place in your program
    * Add a ``print`` to print out the variable's value
    * Compare your expectation with reality
    * If they matched, perhaps the problem is elsewhere
    * If they do not match, investigate why they differ

* Each ``print`` enables us to form a new hypothesis and continue debugging
* Depending on the complexity of the problem, you may find that you need multiple ``print``\s in order to make any progress

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/EnJhV2j8YR0" frameborder="0" allowfullscreen></iframe>


   
Pencil & Paper (or better, a whiteboard)
========================================

* Sometimes you end up chasing your tail with ``print`` statements.
* The function you are debugging is so borked that you can't make heads or tails of it.
* Time for a more holistic approach:
    * Write down a grid with a column for every variable in your function.
    * "Execute" your function, by hand, one line at a time.
    * When your function changes variables, change them in your written grid.
    * No, seriously, **one line at a time**. If you skip a few lines and write down what you *think* they did, you might as well not bother doing this at all.
        * Remember, you're here in the first place because what *is* happening is *different* than what you *think* is happening.
	  
* This seems painful, and it can be.
* If you do it right though, you can *very often* find the problem with your program.
* A lot of the best programmers advocate this method when you're stumped. There's a reason for that.   

Rubber Duck Debugging
=====================

* `Rubber Duck Debugging. <https://en.wikipedia.org/wiki/Rubber_duck_debugging>`_	
* A shockingly effectively form of debugging
* `If you don't have your own rubber duck, don't worry.  <https://play.google.com/store/apps/details?id=com.jameshughes89.dougtheduck>`_ 


Delta debugging
===============

* Still stuck? (or don't want to try Pencil & Paper debug?)
* Here's another approach:
    * Comment out your whole function (by preceding every line with ``#`` )
    * Run it.
    * (of course, nothing happens)
    * Now uncomment a single "semantic unit". No more than a line or two.
    * Maybe add a ``print`` after the uncommented lines
    * Run it.
    * Did it do what you expect?
        * No? You've found at least one problem
        * Yes? Repeat the above process: uncomment a tiny bit of the function, run it, and check that it's doing what you think it is.

* You should code like this in the first place, but if you were bad and didn't here is a way to kinda' go back and address it. 		

   
For next class
==============
* `Seriously, get PyCharm installed! <https://www.jetbrains.com/pycharm/download>`_

* Read `appendix A of the text <http://openbookproject.net/thinkcs/python/english3e/app_a.html>`_  
