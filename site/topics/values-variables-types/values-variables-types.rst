*******************************
Print, Values, Variables, Types
*******************************

.. admonition:: Activity
    :class: activity

    What is *computation?* What is a *computer?* What is *programming?*


.. admonition:: Activity
    :class: activity

    `Who can name different kinds of computers? <https://en.wikipedia.org/wiki/Computer#Unconventional_computers>`_


What Is A Program/Algorithm?
============================

.. admonition:: Activity
    :class: activity

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
    :class: activity

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
    :class: activity

    Do you think there is a limit to what I can describe with a formal language? 

    Can I describe *anything*? *Any* computation? 

    **HINT**: Is the following statement true or false: "This statement is false."


Terminology
===========

* Hardware/Software
* Input/Output (I/O)
* Processors
* Storage --- Hard Disk Drive/Solid State Drive
* Memory and Random Access Memory (RAM)
* Binary
* Compiling
* Interpreter vs Integrated Development Environment (IDE)
   

Print
=====

* We already made use of ``print`` in the previous topic

.. admonition:: Activity
    :class: activity

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
    :class: activity

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
    :class: activity

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


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/8M0uZ5gclOQ" frameborder="0" allowfullscreen></iframe><br><br>


For Next Class
==============

* Read the rest of `Chapter 2 of the text <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html>`_
