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
    ``return``\ing the final value, it just ``prints`` the value out within the function (just replace the final line
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



Execution Flow
==============

* Python executes one statement at a time
* In a program, the statements get executed in the order in which they appear, top to bottom
* However, statements within a function only get executed when that function is called

.. code-block:: python
    :linenos:

    def celsius_to_fahrenheit(temp_in_celsius):
        partial_conversion = temp_in_celsius * 9/5
        temp_in_fahrenheit = partial_conversion + 32
        return temp_in_fahrenheit

    celsius = 24
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(fahrenheit)

    celsius = 32
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(fahrenheit)


* In the above example, the program starts running at line 1, however Python notes that this is a function definition

    * It is not *called* yet --- it does not run yet

* Python takes note of the function and knows that it exists
* The first line to get executed in this program is line 6 where the value of ``24`` is assigned to ``celsius``
* Line 7 makes a call to the function ``celsius_to_fahrenheit``, and so the execution jumps to line 1
* The program will run the whole function (lines 1 -- 4) and return the value to where it was called (line 7) and the value is stored in the variable ``fahrenheit``

    * Functions end when there are no more lines to execute, or a ``return`` statement is hit

* Like 8 prints out the value of ``fahrenheit``
* Line 10 assigns a value to a variable
* Like 11 calls the function ``celsius_to_fahrenheit`` again, which means our execution jumps to line 1 again
* Once the function is complete (lines 1 -- 4), the value is returned to like 11 and the returned value is assigned to ``fahrenheit``
* Line 12 prints out the value of ``fahrenheit``
* The program is now complete


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
* You have been making use of the ``print`` function every time you needed to display something
* Fortunately, you did not need to worry about setting individual pixels on your display to show the characters
* ``print`` has collected all the complex information and instructions needed to print
* Because of this, we can think about ``print`` every time we need to print instead of worrying about the underlying workings of how to set pixels on a display

* Without being able to organize things into *levels of abstraction*, writing complex software would be prohibitively difficult

    * The same is true for your every day live --- learning to think of things in terms of levels of abstraction is very important
    * For example, when driving a car, do you think about the pistons firing?


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


Comments
========

* You can add *comments* to your code in Python with ``#``
* As soon as Python sees ``#`` it ignores the rest of the current line

.. code-block:: python
    :linenos:

    # Calculate the Euclidean distance between two points
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

* We want our code to be written in such a way that it is correct, but also understandable
* However, sometimes we may have some code that is rather complex and not immediately clear

    * This becomes particularly important if you are working with others that need to look at your code

* When situations like these arise, we add comments to our code to explain what's going on
* It's not about explaining everything, but explaining what is likely to be unclear



Docstring
---------

* We will find that, as we write bigger and bigger programs, we will be making use of functions a lot

    * Not only those that already exist like ``print``, but functions we write

* Since functions tend to be some coherent set of statements that serve a purpose, we write *docstrings* to describe what the function does


.. code-block:: python
    :linenos:

    def celsius_to_fahrenheit(temp_in_celsius):
        """
        Convert a temperature from Celsius units to Fahrenheit units.

        :param temp_in_celsius: The temperature in Celsius to be converted.
        :return: The temperature in Fahrenheit.
        """
        partial_conversion = temp_in_celsius * 9/5
        temp_in_fahrenheit = partial_conversion + 32
        return temp_in_fahrenheit


* The stuff between the ``"""`` is the docstring and should appear immediately after the ``def`` line
* It explains what the function does in plane English
* It explains what each parameter is
* If the function ``return``\s something, then explain that too

* This may feel like a lot of work, especially with such a simple function in the above example
* But having these describing the functions makes it easier for anyone looking at your code

    * `This includes yourself one weeks from now <https://i.redd.it/p172loj7q7j31.jpg>`_

* Trust me when I say, there will be a time in your life where you regret not writing comments/docstrings

    * `And when that time comes, I want you to remember that I warned you <https://i.redd.it/b9e4xbeg40151.jpg>`_


  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/eD1iff-zLLo" frameborder="0" allowfullscreen></iframe>

	
For Next Class
==============

* Read `Chapter 5 of the text <http://openbookproject.net/thinkcs/python/english3e/conditionals.html>`_
