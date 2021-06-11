Class #4 -- Logic, if/else 
=================

Conditionals
^^^^^^^^^^^^

* We're pretty good at telling python *exactly what to do* now.
* But there is no room for choice. It's just: *do these steps in this order*
* That doesn't give us much flexibility (or computational power)



.. admonition:: Activity

    Using **only** the Python features/statements **we've seen so far**, can you write a program that will divide a number in half *only if* that number is a multiple of 2?
   
* We need to work towards *conditional execution*

Logic First
^^^^^^^^^^^
* Sometimes things are `True` or `False`
* I'm betting you actually are pretty familiar with some LOGIC
    * AND
    * OR
    * NOT

.. admonition:: Activity

    Write out the truth tables for the logical operations **AND**, **OR** and **NOT**. 
   
    Don't know what a 'logical operator' or 'truth table' is? No problem, Ask: 

    * Wikipedia 
    * Google 
    * Your neighbour
    * Just don't ask me!
   
   
* To make parts of the program *conditionally* executed, we need a *formal* way to describe conditions.
* We need: logic.
* Let's try some comparison:
    >>> 19 == 87
    False

    >>> 5 == 5
    True
	
* Note that ``==`` is *comparison* while ``=`` is *assignment*. They are not the same! Python will punish you if you forget this! 
    * You'll all mess this up eventually
    * Just be thankful this isn't C/C++

.. admonition:: Activity

    Figure out what the other comparison operators in Python are. Hint: ``3`` doesn't equal ``5``, it is *____ than* 5.

* These operators can be applied to any two expressions (could be simply a value or variable, but can be more complex):
    >>> a = 15
    >>> b = 37
    >>> (a+b)*9 > (b-a)*3 + 2
    True
	
* What is the *type* of the result of applying a comparison operator?
 

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/NmeQHw0rOaY" frameborder="0" allowfullscreen></iframe>   

   
Conditional execution
^^^^^^^^^^^^^^^^^^^^^
* Now we can test if a comparison statement is ``True`` or ``False``.
* We need a way to use that to control our program.
* ``if`` some condition is ``True``, do something::

    if grade < 50:
        print('should have gone to class more often.')
  
* If the condition following the keyword ``if`` is ``True``, the code after the ``:`` gets executed.
* If the condition is ``False``, the code gets skipped over.
* As usual, the block that gets executed/skipped is denoted with indentation 
* The block can be as long as you want; no maximum size (though the minimum size is 1)
* (like in a function definition)

* **NOTE:** Remember that the thing in the if statement is either `True` or `False`!

.. admonition:: Activity

    Using only the Python features/statements we've seen so far, can you write a program that will divide a number in half *only if* that number is a multiple of 2?

    **HINT**: You may want to look up the Python modulus operator: ``%``.   
   
   
Compound conditions
^^^^^^^^^^^^^^^^^^^
* We can use the logical operators ``and``, ``or`` and ``not`` to combine conditions.
* The combinations can be arbitrarily complex::

    if (grade < 90 and personality_type == 'A' and desired_career == 'med school') or (grade < 100 and personality_type == 'AAA'):
        print('Time to ask for extra credit!')


.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/8OAsHilB0jw" frameborder="0" allowfullscreen></iframe>   
   
   
   
Alternative execution
^^^^^^^^^^^^^^^^^^^^^
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

   
Chains of alternatives
^^^^^^^^^^^^^^^^^^^^^^
* Sometimes a binary ``if``/``else`` isn't enough.
* What if I want several, *mutually exclusive*, alternatives?::

    if year < 1960:
        print('Jazz')
    elif year < 1980:
        print('Rock')
    elif year < 1990:
        print('Synthpop')
    elif year < 2003:
        print('Alternative')
    else:
        print('Music died when I got my first real job')

* ``elif`` is a contraction of ``else if``
* **NOTE**: Only *one* of the ``elifs`` gets executed, that's *it*. The remaining ones are completely ignored.
* You can chain as many as you want
    * If these were just ``if`` s, what would happen if ``year`` was ``1980``?
        * Let's try it quick.
* **Always** end with a plain ``else`` to catch any conditions not covered in the chain.

.. admonition:: Activity

    Write a Python function that takes an integer from 0-100 representing a course grade and returns a string representing the letter grade: A,B,C,D or F. You can pick the cutoffs.

      .. raw:: html

      	<iframe width="560" height="315" src="https://www.youtube.com/embed/-ZpxIvRshzg" frameborder="0" allowfullscreen></iframe>  
   
   
Nested conditionals
^^^^^^^^^^^^^^^^^^^
* Computer scientists love "nesting" things: putting things inside other things.

.. image:: ../img/dolls.jpeg

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
			
* In the above example, we *could* have done it without nesting and using just ``and`` and whatnot, but the nesting does make things easy to follow. 

* Again, no limit to how deep you nest... but mind the readability of your code!

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
^^^^^^^^^^
* Most of you are here because you are pragmatic people who want to *get stuff done*
* The fastest way to *get stuff done* is by leveraging stuff that other people have done.
* Remember functions? Wouldn't it be awesome if there were huge collections of functions that already existed... and did a lot of the stuff you want to do? 
* One of reasons we're using Python is because it has a *huge* variety of existing **libraries**/**packages**.
* No matter what you want to do, there's probably a library that can help you.
	   
	   
NumPy
^^^^^^
* The most important library for us is *Numerical Python* ("NumPy" for short).
* We're going to get quite a bit of mileage out of NumPy, and some of it's affiliated packages, in this course.
* NumPy is *not* a core part of Python, but it is included in Anaconda.
* For a scientist (or anyone really) working with real data in Python, NumPy is *absolutely essential*
* Because it isn't 'built in' to Python, we have to tell Python that we want to use NumPy:
    >>> import numpy

NumPy Types
^^^^^^^^^^^^
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


    .. image:: ../img/monster.jpeg


* Floating point precision...
* Let's think for a second about real numbers vs. computers. 	
	

* You can convert regular Python types, and NumPy types, back and forth as you need.
* If you aren't sure what type a variable has, remember that you can always check with ``type()``

.. admonition:: Activity

    Write a Python function that takes two Python ``float`` s as inputs, converts them both into ``numpy.float32`` type and then returns the product.   
   
   
   
   
   
      
For next class
^^^^^^^^^^^^^^^

* Read `chapter 6 of the text <http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html>`_


