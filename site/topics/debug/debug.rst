*********
Debugging
*********

It's broke, I give up!
======================

* By now, you'll have experienced code that doesn't do what you want it to.
* You may have developed some coping strategies to help you fix things.
* You were probably frustrated.
* You may have just randomly changed stuff until it worked.
* We're sophisticated enough now that we can start looking for more formal processes 
  for tackling these kind of problems.

The importance of debugging
===========================

.. image:: hi.jpg

* The more complex your programs get, the more time you'll spend debugging.
* No matte how *good* you are as a programmer, you still spend **a lot** of time debugging.
* The number one thing my friends in industry tell me that they wish more CS graduates knew more of is **debugging**!

* Beyond being an immediately useful skill for fixing broken programs, the ability to effectively debug demonstrates:
  
    * Knowledge of algorithms and programming in general
    * Knowledge of the programming language
    * The ability to reason logically
    * The ability to reason about flow of execution in code
	 
* That's why we've waited so long to formally discuss debugging. There are a lot of prerequisites.
	

.. Warning::

    Debugging (especially more rigorous approaches) may seem hard and/or boring at first. Hang in there. The ability to logically debug can, literally, save you *days* of time when there is a problem in your code.	

   
Syntax errors
=============
* These are easy to fix. 
* You make a typo and Python tells you the problem, and where it is, straight away.
* You fix the syntax and... problem solved.
* Not much strategy: just look at the code or look at what python yells at you about

.. admonition:: Activity
   
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
