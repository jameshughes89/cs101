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

.. admonition:: Activity
    :class: activity

    a = 5           # It's an integer
    b = 5.5         # Float since there is a decimal
    c = a + b       # Mixing types in the expression (int and float), but no big deal
    print(c)        # Results in 10.5


* But Python can only do so much
* For example, Python cannot suddenly figure out what it means to add an integer and a string together

    * Think about it this way, what would you say if I asked you what "Hello" divided by 32 means?


.. admonition:: Activity
    :class: activity

    print(99 + "bottles of beer on the wall")
    TypeError: unsupported operand type(s) for +: 'int' and 'str'


* However, sometimes we can have an issue caused by types that does not generate an error message
* Consider the ``inconsistent`` function defined in the following example

    .. admonition:: Activity
        :class: activity

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

* These are pretty much everything else...
* *Much* harder to track down than simple errors
* Might be obvious (e.g. infinite loop)
* Might be "silent" (your code *looks* like it works, but gives subtly wrong answers in certain conditions)
    * `These can literally be deadly! <https://en.wikipedia.org/wiki/List_of_software_bugs>`_
* We'll look at a few strategies for tackling these...   
	
	
Print
=====

* By far the simplest method I use every day that works a lot of the time. 
* If your code isn't doing what you expect it to, one way to figure what is happening is to insert ``print`` statements into your code.
    * Just be careful with the obscenities.
	
    >>> print('work you piece of s***!')

* By printing the values of variables at various points, you can double-check that the variables really do have the values you expect
* Compare your intuition/expectation with reality

.. admonition:: Activity
    :class: activity

    There is one problem with this function. It ALMOST works, but it's slightly off. Read the description, test it with a ``print``. Is it right or wrong? Move the ``print``. See what happens? etc. etc.

    .. code-block:: python
   
        def count_numbers_up_to(n):
            '''
            This function adds up all the numbers from 0 - n exclusively.
            Eg. 5 -> 0 + 1 + 2 + 3 + 4 -> 10

            :param n: The number we are counting to. Note we do not count n
            :return: The sum of the numbers
            '''

            total = 0
            c = 0
            while c < n:
                c += 1
                total += c
            return total
	  

	print(count_numbers_up_to(5))  
   
   
* Good thing we made sure the function was working perfectly before using it somewhere else and assuming it worked!  


It is that easy!
----------------

* This is a very easy, obvious way to debug.
* It's also quite effective.
* The process is always the same:
    * Generate a hypothesis about values a variable should have at a particular place in your program
    * Put a print statement at that place
    * Compare reality to your hypothesis
    * If they match, your problem is elsewhere
    * If they don't... now you have something to investigate
* You will rarely solve a complex problem with a single ``print``.
* Instead, each ``print`` will lead you to form a new hypothesis... and then test it with another ``print``. 
   
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
