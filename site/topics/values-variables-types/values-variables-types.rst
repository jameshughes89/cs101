**************************************
Values, Types, Variables, Print, Input
**************************************

Welcome back
============

Let's get started right away...

.. admonition:: Quick Activity

    Did you try anything interesting with Python yet?
   
   
**Heads up:** Before we get to the "super awesome fun stuff", we've got to cover the basics. I understand that the basics aren't super awesome. Don't worry, we'll get there. But we can't get there without the basics.


.. admonition:: Activity

    What is *computation?* What is a *computer?* What is *programming?*


.. admonition:: Activity

    Who can name different kinds of *computers* `? <https://en.wikipedia.org/wiki/Computer#Unconventional_computers>`_
	  
	  
	     
What's a program?
=================

* The stuff in the computers
* A thing that does stuff
* A recipe
* A sequence of instructions that specifies *exactly* how to perform a computation?

.. admonition:: Activity

    Explain to a partner how you would go about making breakfast in the morning.
   
   
* There, that's basically a program.
* What kind of computer was executing this program?   


What's debugging?
=================

* Mystery novel
* A logic puzzle
* How you fix your mistakes
* What most programming is

.. admonition:: Quick Activity

    Have you seen any Python errors yet? 

    What were they? 

    Did you understand them?
   
   
Languages
=========

* What's the difference between a formal, and a natural, language?
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
* IO 
* Processors
* Hard Drive
* RAM
* Binary
* Compiling
* Interpreter vs IDE
   
   
Okay, we're done with the background, let's get on with the real stuff
======================================================================

.. admonition:: Activity

    Write a (single-line) Python program that prints a witty message, of your choice.   
   

print
=====

* Print is a *function* that allows us to print out information to the screen
* Print might end up being your best friend
* Get used to writing it
   
   
Values 
======

* Values are things that a program manipulates
    * *Strings*: "abcdef"
    * *Integers*: 7, 42, 97
    * *Floating-point numbers*: 3.792, 0.000000000005
* These values are called **literals**
    * like, 1 is *literally* 1  
* Notice how I described the **type** of each value along with the value itself
    * Strings
    * Integers
    * Float
   
* Computers are exceptionally stupid. You must be completely explicit about everything

* To a computer, the integer 1 is not necessarily the same thing as the floating point number 1.0... because they have different *types*
    * They actually have different meaning
    * They even technically have different physical representations inside the computer too, which is neato  
* Many of the errors you will make in programming result from mixing types inappropriately
* Some languages (e.g., C, Fortran, Java) are very militant about types. You have to be totally explicit about them
* Python is a little more relaxed. You *can* be explicit, but you don't have to be. Python will guess if you don't tell it
* Upside: less to worry about and less clutter in your code


* Can I ask Python to tell me its guess for the type of a value?
    >>> print(type(12))
    <class 'int'>
    
    >>> print(type('Witty remark'))
    <class 'str'>
	
    >>> print(type(3.75))
    <class 'float'>
	
    >>> print(type(type(1.1)))
    <class 'type'>


* It's kinda' easy to tell the type of a value isn't it?
    * Most of the time... but this will bite you... trust me!


.. admonition:: Activity

    Write a single line program to print out the *integer* 1. Now write a single line program to print out the *string* 1. Can you tell the difference by looking at the output?   

   
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
   

Choosing variable names
=======================

* You can use whatever you want, within a few restrictions set by the language.
    * Python wants variable names that begin with a letter of the alphabet and limits what non-alphanumeric characters you can use
* A good choice is a variable name that is descriptive of what the variable is meant to contain. 
    * good: ``density``
    * less good: ``d``
    * bad: ``definitely_not_density``

.. admonition:: Activity

   Suppose you're a big fan of '80s Arena Rock. Create two variables, named ``def`` and ``leppard``, set them to ``19`` and ``87`` respectively, then add them.

* What happened? (To your code, not the band!)   

Constants
=========

* They're just variables, but WE, as the programmers use them a special way
* Imagine you are writing a program where you're doing a lot of calculations with sales tax

    >>> some_bill = 10.45 * 1.15
    12.0175
    
    >>> another_bill = 4.99 * 1.15
    5.7385
    ...
	
* This is clearly correct, butttt:
    * What if one of your friends looks at this code and wonders "wtf is 1.15?"
    * What if the gov changes the sales tax in the future?

* Isn't that a little clearer?
 
	
	>>> SALES_TAX = 1.15
	>>> some_bill = 10.45 * SALES_TAX
	12.0175
	>>> another_bill = 4.99 * SALES_TAX
	5.7385
	...
	
* Convention is all uppercase and underscores   
	
   
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