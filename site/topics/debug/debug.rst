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

   
Syntax errors
=============
* These are easy to fix. 
* You make a typo and Python tells you the problem, and where it is, straight away.
* You fix the syntax and... problem solved.
* Not much strategy: just look at the code or look at what python yells at you about

.. admonition:: Activity
    :class: activity
   
    Fix this Python function::
   
        deff borken(a(
            a = a + * 3
            walrus
            return a + 2   
		 
        broken(5)
   
Type errors
===========

* As we've seen many times, Python is pretty good at transparently guessing how to change types when you ask it do something that involves multiple types::
  
    >>> 2.03 + 4
    6.0299999999999994
     
* **But** sometimes you might ask the impossible:

     >>> 2.03 + 'octopus'
     TypeError: unsupported operand type(s) for +: 'float' and 'str'

* Again, this is a simple error where you get a message telling you exactly what is wrong.


.. admonition:: Activity
    :class: activity
   
    This following code fine and all, but, like... what are the types of ``n`` and ``m`` supposed to be? The result of calling ``concat(5,5)`` and ``concat('5','5')`` are very different.
   
    .. code-block:: python

        def concat(n,m):
            return n + m
		 
         
Other simple errors
===================

* If an error is "simple", it generates a message from Python.
* This tells you *what* is wrong and *where* it's wrong.
* If you don't understand the error message... cut and paste it into Google.
    * This is literally what I do. 


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
