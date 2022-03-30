*********
Functions
*********


* Script/program files are a nice way to organize many statements
* However, eventually you will find yourself writing the same series of statements over and over
    * Or copying and pasting in your editor

* This is troubling since
    * It is tedious
    * You can introduce errors
    * Your code can become harder to maintain


Functions
=========

* We like to group together sequences of statements that serve a coherent purpose
* In Python, and many other programming languages, we do this with *functions*


Defining a Function
-------------------

* Once you've **defined** a function, you can *call* it exactly the same way you call *built-in functions* like ``print``

.. code-block:: python
    :linenos:

    def celsius_to_fahrenheit(temp_in_celsius):
        partial_conversion = temp_in_celsius * 9/5
        temp_in_fahrenheit = partial_conversion + 32
        return temp_in_fahrenheit


* Above is an example definition of a function that converts temperature units from Celsius to Fahrenheit
* The details on all the parts will be discussed as we move through this topic
* You can probably already get a sense that
    * It is a group of statements that serves a single purpose
    * It can be reused every time we want to do the conversion without having to write the whole conversion formula out


Calling a Function
------------------

* Given the function definition of ``celsius_to_fahrenheit``, we can now *call* the function
    * ``celsius_to_fahrenheit(0)`` gives us ``32.0``
    * ``celsius_to_fahrenheit(-40)`` gives us ``-40.0``
    * ``celsius_to_fahrenheit(32)`` gives us ``89.6``

* It's always good to test your functions a little to verify that they are doing what you expect

* When we call a function, Python executes the statements within the function in the order that they appear
* Functions allow for
    * Reuse --- Just call it any time you need it
    * Maintainability --- If there is a bug in the function, you only need to change the function once
    * Readability --- ``celsius_to_fahrenheit`` is a lot easier to recognize when compared to something like ``(C * 9/5) + 32``

* More importantly they *facilitate abstraction*
    * More on this later


.. admonition:: Quick Activity

    Write your own function to do something with math. Honestly, whatever you want. 


Function Parameters
-------------------

* Notice how the function ``celsius_to_fahrenheit`` has a *parameter* called ``temp_in_celsius``
* When defining functions, we want them to be very general
    * For example, it would be rather silly to write a function ``twenty_degrees_celsius_to_fahrenheit`` that was only capable of converting 20 degrees Celsius to Fahrenheit
        * What happens if we want to calculate 30 degrees Celsius in Fahrenheit, write another function called ``thirty_degrees_celsius_to_fahrenheit``?
    * Instead, we wrote the function such that the temperature in Celsius is a parameter that we can specify when calling the function
        * ``celsius_to_fahrenheit(20)``
        * ``celsius_to_fahrenheit(30)``

.. code-block:: python
    :linenos:

    # This is rather silly and useless
    def twenty_degrees_celsius_to_fahrenheit():
        partial_conversion = 20 * 9/5
        temp_in_fahrenheit = partial_conversion + 32
        return temp_in_fahrenheit


* If it helps, just think of the parameters as variables that belong to the function

* You have already been specifying the parameter in the ``print`` function
    * The value you want printed out is the value you are setting for the parameter that ``print`` takes

* In reality, you have been using this idea in math class for years

    :math:`f(x) = x * 9/5 + 32`

* This is the definition of a function called :math:`f` that takes a parameter :math:`x`
* If I asked you what :math:`f(20)` is, you can calculate the result

    :math:`f(20) = 20 * 9/5 + 32`

    :math:`f(20) = 36 + 32`

    :math:`f(20) = 68`

* This is the same idea we used in ``celsius_to_fahrenheit``, but in Python instead of our typical math syntax


Execution of a Function
-----------------------

* Below is a simple and arbitrary function (``square_of_sum``) that takes two parameters (``a`` and ``b``) and calculates what the square of their sum is

.. code-block:: python
    :linenos:

    def square_of_sum(a, b):
        c = a + b
        d = c * c
        return d


* If I were to call this function with ``square_of_sum(2, 3)``, Python handles the execution like this
    #. Python will check to see if it knows about a function called ``square_of_sum``
    #. Python takes the values supplied to it when called (``2`` and ``3``) and assigns them to their respective parameters
        * ``a = 2`` and ``b = 3``
    #. The sum of ``a`` and ``b`` is put into a variable ``c``
    #. The variable ``c`` is multiplied with itself (effectively squaring it) and the result is assigned to ``d``
    #. The function returns the value associated with ``d``

* What happens if we don't give it enough, or too many parameters?

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/clFWPflvEKI" frameborder="0" allowfullscreen></iframe><br><br>


Return
======

* Every function you call *returns* a value
* Notice that we wrote ``return`` at the end of the previous functions
* This allows me to specify the value being returned by the function

* Consider the following example

.. code-block:: python
    :linenos:

    temperature = celsius_to_fahrenheit(20)
    print(temperature)


* Here, the function call ``celsius_to_fahrenheit(20)`` will execute the function
* When the function finishes executing, it returns the value ``68``
* The value ``68`` is stored in the variable ``temperature``
* The value of ``temperature`` (``68``) is printed out

* If you do not write a ``return`` statement in a function, the function will still return a value, but the value will be ``None``
* ``None`` is a special type and value that means *nothing*

.. admonition:: Activity

    Write a function ``print_celsius_to_fahrenheit`` that is identical to ``celsius_to_fahrenheit``, except instead of
    ``return``ing the final value, it just ``prints`` the value out within the function (just replace the final line
    with ``print(temp_in_fahrenheit)``).

    Run the following and see if you can figure out why it is doing what it is doing:
        * ``print(print_celsius_to_fahrenheit(20))``
        * ``print(celsius_to_fahrenheit(20))``
        * ``print_celsius_to_fahrenheit(20)``
        * ``celsius_to_fahrenheit(20)`` **NOTE:** This one is lying to you


.. Warning::

    Colab is misleading you when you call ``celsius_to_fahrenheit(20)``. Colab will make it seem as if
    ``celsius_to_fahrenheit(20)`` is printing out the result, but it is not --- Colab is being "nice" and just
    displaying any values produced on the last line of code, regardless of if you printed it out. To demonstrate this
    to yourself, run the following:

    .. code-block:: python
        :linenos:

        celsius_to_fahrenheit(20)
        print("Now you do not see any value from celsius_to_fahrenheit")


    In the above example, if you want to keep track of the value returned by ``celsius_to_fahrenheit``, simply assign it
    to a variable for later ``some_variable = celsius_to_fahrenheit(20)``.


.. admonition:: Activity

    Write a function called ``euclidean_distance(x1, y1, x2, y2)`` that calculates and returns the Euclidean distance
    between two points. Remember, Euclidean distance is defined as :math:`\sqrt{(x1 - x2)^{2} + (y1 - y2)^{2}}`

    Does Python have a square root function? How do you calculate the square of a value in Python?
    `How would I find out? <https://www.google.ca/>`_


Abstraction
===========

.. admonition:: Activity

    Write down a "program" to make spaghetti (not in python, like on paper). You can only use the following statements: 

    * ``locate [object]`` 
    * ``grasp [limb]`` 
    * ``release [limb]`` 
    * ``move_limb_to [location]``
    * ``wait [time in seconds]``

    Assume you start from a clean, empty, kitchen.


.. admonition:: Activity

    Write down a "program" to make spaghetti (not in python, like on paper). You can use plain English prose and assume
    you are addressing a human being who is familiar with a kitchen and making pasta.

    Assume you start from a clean, empty, kitchen.


* You have now created two different programs for making spaghetti at two different levels of abstraction, which version was easier?


Making Use of Abstraction
-------------------------

* You have been making use of the ``print`` function every time you needed to display something
* Fortunately, you did not need to worry about setting individual pixels on your display to show the characters
* ``print`` has collected all the complex information and instructions needed to print
* Because of this, we can think about ``print`` every time we need to print instead of worrying about the underlying workings of how to set pixels on a display


Creating Abstraction
--------------------

* Without being able to organize things into *levels of abstraction*, writing complex software would be prohibitively difficult

    * The same is true for your every day live --- learning to think of things in terms of levels of abstraction is very important
    * For example, when driving a car, do you think about the pistons firing?
    * Or, do you need to think about neurons firing and ion pumps to move your arm?

* You are already experts at this in real life
* Unfortunately, however, it is not simple to just start creating abstraction in your code
* Knowing how and where to create levels of abstraction requires a deep understanding of the problem you are trying to address



Back to concrete things...
==========================

* The general format for defining a function is::

	def function_name(p1, p2, p3, p4, ... ):
		statement 1
		statement 2
		...
		statement m
		
* ``function_name`` is... the name of the function. This can be almost whatever you want.
* ``p1, p2`` , etc. are called the *parameters*, you can have as many as you like and call them almost whatever you want. 
* You tell Python which statements make up the *body* of the function by using *indentation*.
    * This is a somewhat unique feature of Python. 
        * And somewhat hated by some people. 
    * Many other languages use pairs like ``begin, end`` , ``do, done`` or ``{, }`` to delimit the body of a function.

.. admonition:: Activity

    Write a function ``catstr`` which takes two strings as parameters and then prints out the concatenation of the strings. e.g., if I call ``catstr('Hello ','world!')`` it will print ``Hello world!``.

      .. raw:: html

		<iframe width="560" height="315" src="https://www.youtube.com/embed/cMTPTq7xpOA" frameborder="0" allowfullscreen></iframe>
   
   
.. admonition:: Activity

    **NOTE:** This one is tricky but super important to understand. If you're still stuck after class, be sure to take your time to figure this out. There's a YouTube video to help you out. 
   
    Now write a function ``crosscat`` that will take *four* strings and print out the concatenation of the first and third string, and then, on a new line, the concatenation of the second and fourth string. **BUT**: your function isn't allowed to use a ``print`` function! You can, however, use your ``catstr`` function.

      .. raw:: html

   		<iframe width="560" height="315" src="https://www.youtube.com/embed/DESQnHsGYss" frameborder="0" allowfullscreen></iframe> 
	
		
Execution Flow
==============

* Python executes one statement at a time
* To make sense of programs, we need to know *which* instruction gets executed *when*
* In a program, the statements get executed in the order in which they appear in the program, top to bottom of the file
    * Later, we'll learn how to jump around
* What happens when a function gets called? Let's trace through this program::

    def do_stuff(a, b):
        c = b * 2
        d = (a+4) * 2
        c = d + c
        return c
	
    x = 2
    y = 3
    z = do_stuff(x, y)
    print(z)
    print("where am I?")

* So what happens is:
    * Program starts at the top, and computer sees that a function is being *declared* (not called yet)
        * NOT RUN YET THOUGH!
    * Computer basically skips down to where the function ends
    * We assign some values to variables   
    * Python makes a note of where the function is being called from
    * The *flow of execution* passes to the function
    * Python executes each statement in the function, in order
    * At the end of the function, control returns to the point from which the function was called
	
	
Composition
===========

* Python functions can be *composed* just like mathematical functions.
* We've already seen ``print`` composed with ``do_stuff``
* We can nest functions, too:
    >>> do_stuff(do_stuff(2, 2), do_stuff(2, 2))
    72
* If you get confused tracing nested functions, just remember:
    * Functions get *evaluted* and turned into values
    * Find a function you can evaluate
    * Evaluate it
    * Cross out the function and replace it with the *value* it returns
    * Keep doing this until you're down to one value.

.. admonition:: Activity

    Figure out the value of ``do_stuff(do_stuff(2, 2), (do_stuff(2, 2) + do_stuff(4, 4)) )`` using only *pen and paper*. No computers!

.. admonition:: Activity

    Figure out the value of ``no_stuff(no_stuff(2, 2), (no_stuff(2, 2) + no_stuff(4, 4)) )`` using only *pen and paper*. No computers!
	
Variable scope
==============
* If you set a variable inside a function, it is *local* to that function.
* No other function can see a function's local variables. They are *local*. Consider this code::

    def do_more(a, b):
        c = 2*a + b
        return c


* What happens if I do this:
    >>> print do_more(4, 4)
    12

    >>> print(c)
    NameError: name 'c' is not defined
	
* Error! But ``c`` is defined in ``do_more``! Why did we get an error?
* Moral of the story: variables have *scope*. This can actually be a surprisingly delicate concept and we'll come back to it later.	
	

Import --- MORE
===============
* Can also import other people's functions
* 	>>> import math
* 	>>> import numpy	


COMMENTS!!!!!!!!!!!
===================

* You can add *comments* to your code in Python with ``#``::

    do_something()
    # We just did something
    # Now we'll do something else
    do_something_else() # doing something else
   
* As soon as Python sees ``#`` it ignores the rest of the current line
* Writing comments makes your code *easier to read*
* Especially 6 weeks later when you have to change it


* And *especially* when someone else has to make sense of your mess
* Comments shouldn't just repeat what's obvious from reading the code
* They should provide a *higher level* description of what's happening.
* Computer Scientists get real geeky about comments
* Physicists immediately go into shock and collapse if they write a single comment
* Find a healthy balance that works for you

Function headers
================

* Because so much of our programming consists of pasting together functions... it is of special
  importance to document what a function does.
* We do this with a *function header*::

    def set_up_cities(names):
        """
        Set up a collection of cities (world) for our simulator.
        Each city is a 3 element list, and our world will be a list of cities.
        
        :param names: A list with the names of the cities in the world.
        
        :return: a list of cities
        """

        print 1 + 2

* The stuff between the ``"""`` is the function header and should appear *immediately after* the ``def``.
* It should explain what the function is going to do, in plain English. If I have to read the function code to figure out what it does, your header description sucks.
* It should explain *every* parameter.
* If the function returns something, it should explain that too

This might all seem like a lot of extra work. And it is. But it's *less* work than trying to figure out how everything works after you've been away from the code for 2 months.

You don't believe me. You'll leave this course and go write code with no comments. Seriously, you will. You might *mean* to write comments, but you won't. You're just too *busy*.
 
Then, at some later point, you'll have to go back to your code. It won't have comments. You'll have no clue how anything works. It'll take you a day or two just to figure out what you'd done before.

After that happens enough times, you'll start writing comments.

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/eD1iff-zLLo" frameborder="0" allowfullscreen></iframe>

	
For next class
==============

* Read `chapter 5 of the text <http://openbookproject.net/thinkcs/python/english3e/conditionals.html>`_
