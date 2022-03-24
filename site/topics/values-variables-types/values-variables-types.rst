**************************************
Values, Variables, Types, Print, Input
**************************************

.. admonition:: Activity

    What is *computation?* What is a *computer?* What is *programming?*


.. admonition:: Activity

    `Who can name different kinds of computers? <https://en.wikipedia.org/wiki/Computer#Unconventional_computers>`_


What Is A Program/Algorithm?
============================

.. admonition:: Activity

    Explain to a partner how you would go about making breakfast in the morning.


* There, that's an algorithm
    * It is a series of instructions that can be followed to achieve something

* What kind of computer was executing this program?


What Is debugging?
==================

* Most of the time your code will be wrong
    * This is true for both new and experienced programmers

* Debugging is the process of addressing the bugs in your code
* Realistically, expect to debug a lot

* Remember, you will be wrong every time you run your program before you get it right
    * The point is, you will be wrong a lot more than you will be right --- get used to this


.. admonition:: Quick Activity

    Have you seen any Python errors yet? 

    What were they? 

    Did you understand them?

   
Languages
=========

* What is a natural language?
* What is a formal language?
* Why is ambiguity so important to natural language?
* Why is ambiguity deadly for a formal language?

.. admonition:: Activity

    Do you think there is a limit to what I can describe with a formal language? 

    Can I describe *anything*? *Any* computation? 

    **HINT**: Is the following statement true or false: "This statement is false."
   
* The world is a screwed up, scary, place (for mathematicians, anyways). If you want to fall down this particular rabbit hole:
    * https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
	* http://en.wikipedia.org/wiki/Principia_Mathematica
	* http://en.wikipedia.org/wiki/Computability   
   

Terminology
===========

* Hardware/Software
* Input/Output (I/O)
* Processors
* Hard Drive
* Memory and Random Access Memory (RAM)
* Binary
* Compiling
* Interpreter vs Integrated Development Environment (IDE)
   

Print
=====

.. admonition:: Activity

    Write a (single-line) Python program that prints a witty message of your choice.


* Print is a *function* that allows us to print out information to the screen
* Print might end up being your best friend
* Get used to writing it


Values And Types
================

* Values are things that a program manipulates
    * *Strings*: ``"abcdefg"``, ``"Hello World"``
    * *Integers*: ``7``, ``42``, ``97``
    * *Floating-point numbers*: ``3.792``, ``0.000000000005``

* These values are called **literals**
    * Like, ``1`` is *literally* ``1``

* Notice how I described the **type** of each value along with the value itself
    * Strings
    * Integers
    * Float
   
* To a computer, the integer ``1`` is not necessarily the same thing as the floating point number ``1.0`` or the string ``"1"``

* Some of the errors you will make will be a result from mixing types incorrectly
* Some languages (e.g., C, Java) are strict about types
    * You have to be totally explicit about them

* Python is a little more relaxed
    * Python will guess what the type is
    * Upside: less to worry about and less clutter in your code
    * Downside: more likely to introduce errors caused by mixing types

* You can check the type of something in Python by using the ``type`` function
    * ``print(type(12))`` would print out ``<class 'int'>``
    * ``print(type("Hello, World"))`` would print out ``<class 'str'>``
    * ``print(type(3.75))`` would print out ``<class 'float'>``
    * ``print(type(type(1.1)))`` would print out ``<class 'type'>``

* Notice that we are using two functions in the above examples
    * ``print``
    * ``type``

.. admonition:: Activity

    #. Write a single line program to print out the *integer* ``1``.
    #. Now write a single line program to print out the *string* ``"1"``.
    #. Can you tell the difference by looking at the output?


Variables
=========

* Variables let you store values in a labeled (named) location
* You store *values* into *variables* by using the assignment operator --- ``=``

.. code-block:: python
    :linenos:

    a = 5
    m = "Some String"


* In the above example, the variable ``a`` now has the value ``5``
* Both the *variable* ``a`` and the literal ``5`` both have the same value
    * If I say ``print(5)``, Python will print out the literal ``5``
    * If I say ``print(a)``, Python will print out the value stored in the variable ``a``, which is ``5``

.. warning::

    The ``=`` in Python has a very different meaning from what you are familiar with in math. In math, when one writes
    :math:`a = 5`, it means that :math:`a` and :math:`5` are equivalent as they exist --- it is stating a fact.

    In Python, and many other programming languages, it is not a statement about equality, but an assignment. In Python,
    if one writes ``a = 5``, it means that the variable ``a`` is now storing the value ``5`` within it.


Using Variables
---------------

* You can use variables in the same way you use literals

.. code-block:: python
    :linenos:

    print(5 + 6)

    a = 5
    b = 6
    print(a + b)

* Both ``print``s will print out ``11``
    * The first one adds the literals ``5`` and ``6``
    * The second one adds the variables ``a`` and ``b``

   
.. admonition:: Activity

    #. Assign various values of types string, integer and float to variables.
    #. Try adding variables of the same type. What happens?
    #. Try adding variables of different types. What happens?
    #. Try the assignment ``5 = a``. What happens?
    #. Figure out how to display the current contents of a variable.
   

Naming Variables
----------------

* You can use whatever you want within a few restrictions set by the language
    * Python wants variable names that begin with a letter of the alphabet and limits what non-alphanumeric characters you can use

* A good choice is a variable name that is descriptive of what the variable is meant to contain
    * good: ``density``
    * less good: ``d``
    * bad: ``definitely_not_density``

* There are a few other important restrictions that you may come across
    * For example, you cannot use reserved words (words that already have a specific meaning in Python)
        * ``def = 55`` will not work since ``def`` is a reserved word

* Two important conventions we will follow
    * Use lowercase letters
    * Separate words in the variable name with underscores (snake case)
        * ``some_bill``


Constants
---------

* In Python, constants are just variables that we as programmers use in a special way
* Imagine you are writing a program where you're doing a lot of calculations with sales tax

.. code-block:: python
    :linenos:

    some_bill = 10.45 * 1.15
    another_bill = 4.99 * 1.15


* This is clearly correct, however
    * What if someone else looks at this code and wonders what 1.15 is?
    * What if the gov changes the sales tax in the future?

* Although there is nothing wrong with the above code, one could do the following instead

.. code-block:: python
    :linenos:

    SALES_TAX = 1.15
    some_bill = 10.45 * SALES_TAX
    another_bill = 4.99 * SALES_TAX


* Now, just by looking at those lines of code, I know exactly what we are multiplying the numbers with
* If the sales tax rate is ever lowered, all I need to do is change the one line of code (``SALES_TAX = 1.15``)

* The naming convention for constants is all uppercase letters separate with underscores

* The idea behind the constants are that once the value is set by you, they are not to change
    * You can change them in the code, but the code should not alter the value of ``SALES_TAX``

* In Python, there is nothing stopping you from changing the value other than the convention
    * In some languages, the language actually prevents the program from altering the value of a constant


input
=====

* So we saw how to out print **out** the contents of a variable
* Is there a way to read **in** a value and put it into a variable?
* **YES!**

* Let's type this
	>>> my_value = input('give me a value: ')

* The string between the parentheses is what will be displayed to the user 
    * We can leave it blank too, but nothing will be printed out (this is important for Kattis)
        >>> my_value = input()
        
* The program will wait for the user to enter a value
* After a value is entered, it will be stored in the variable ``myValue`` 

.. admonition:: Activity

    * Read in some value into the computer. 
    * Print out the value you inputted.
    * What is the type of the value? How can I test this?
   
* What if we want it to be an int?

    >>> my_value = input('give me a value: ')
    >>> my_value = int(my_value)

or	
	
    >>> my_value = int(input('give me a value: '))
		
	
* We can actually use this idea to convert types.
   * int will convert something to an int
   * str will convert something to a string
   * float will convert something to a float
   
but...

    >>> int('hi')
    ValueError: invalid literal for int() with base 10: 'hi'
	
So it will only work if it's a valid thing to ask


Statements
==========

* A **statement** is an order to Python: "*do something*"
* An *instruction* that can be *executed* by Python
* You type in the statement into the interpreter, press Enter, and Python does what you asked (or at least tries to)
* If you type a series of statements into Colab and press run, Python does what you asked (or, again, at least tries to)
* Some statements produce immediate output, some just change things 'behind the scenes'
* We've already been using assignment statements (``=``), prints, inputs, and there are A LOT more

Expressions
===========

* An **expression** is, roughly, a thing that can be crunched down to a **value**.
* More precisely, an expression is a combination of:
   * literal values (e.g., ``5``)
   * variables (e.g., ``leppard``)
   * operators (e.g., ``+``)
	>>> leppard = 87
	>>> print(leppard * 2 + 7)
	181   
   
   
Operators
=========

* **Operators** are symbols that tell Python to perform computations on expressions.
   * e.g., +, -, \*, / 

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/8M0uZ5gclOQ" frameborder="0" allowfullscreen></iframe><br><br>   
   
   
.. admonition:: Activity

   Generate expressions to: 

   * 1) Add two variables 
   * 2) Multiply two variables 
   * 4) Divide result of step 3 by the result of step 1
   * 3) Add a third variable to the result of step 2

   ARE YOU READY FOR THIS?

   * Convert a temperature in Celsius to Fahrenheit.  
      * `But I don't know how to convert Celsius to Fahrenheit!!!! <https://www.google.com/search?sxsrf=ACYBGNR8TzZ_PzGMU9aXJ2I1VNjrV2XESg%3A1566411780922&source=hp&ei=BIxdXfP-NZLr-gTIp7v4CQ&q=how+to+convert+c+to+f>`_   
      .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/R1ScWDNUEnM" frameborder="0" allowfullscreen></iframe><br><br>   
   
   
Are operators just for numbers?
===============================

* Nope! Values of all sorts have operators that work on 'em.

.. admonition:: Activity
   
   * Experiment with the operators you know on *strings* (instead of just integers). 
   * Which ones work? What do they do? 
   * Try mixing strings and integers with various operators. What happens there?

   
Doing sequences of things
=========================

* So far we've just been entering one line at a time into the Python.
* That's not going to scale very well for most of the stuff we want to do...
* You can store an (arbitrarily long) series of statements in Colab (or in a file), and then ask Python to run that file for you.
* Python will execute each line of the file, in order, as if you'd typed them in.
* There are lots of ways to run scripts. Suppose you put a series of statements into a file called ``my_program.py``
    * from Colab: hit the run button or press Ctrl-Enter
    * from your IDE: hit the run button or figure out the hotkey
    * from the shell: ``$ python my_program.py`` or ``ipython my_program.py``
    * from the interpreter: ``>>> execfile('my_program.py')``
    * if you're using Ipython: ``%run my_program``
* To edit the script, you can use any text editor that you want. You'll have an easier time with one that is "Python aware", though.
   * Wut?
   * Colab
   * Notepad++ (Windows)
   * Sublime (Windows and Mac)
   * Integrated Development Environment
   * VS Code (Windows, Linux, and Mac)
   * PyCharm!
   

.. admonition:: Activity

    Consider the sentence ``Def Leppard is a poor substitute for Van Halen``. Write a program that stores *each word* of that sentence in it's own variable, and then prints the whole sentence to the screen, *using only a single print statement*.

      .. raw:: html

		<iframe width="560" height="315" src="https://www.youtube.com/embed/u-d3chSpFO4" frameborder="0" allowfullscreen></iframe><br><br>
   
For next class
==============

* Read the rest of `chapter 2 of the text <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html>`_
* Read `chapter 4 of the text <http://openbookproject.net/thinkcs/python/english3e/functions.html>`_
