**************************
Statements and Expressions
**************************

* Programs we write will be made up of multiple lines of code
* Each line will be doing some sort of work/computation


Statements
==========

* A **statement** is an instruction for Python to *do something*
* If you type a series of statements and press run, Python does what you asked (or at least tries to)
* Some statements result in some immediate output
    * ``print("Hello world")``
* Others will do some work behind the scenes
    * ``some_variable = 5``


Expressions
===========

* An **expression** is, roughly, a statement that can be crunched down to a **value**
* More precisely, an expression is a combination of:
    * literal values (e.g., ``5``, ``"Hello world"``)
    * variables (e.g., ``some_variable``)
    * operators (e.g., ``+``, ``*``)

* ``some_other_variable = (some_variable + 1) * 2`` is an example of an expression (and statement)


Operators
=========

* We have been using these in our code already
* **Operators** are symbols that tell Python to perform computations on expressions
    * example arithmetic operators --- ``+``, ``-``, ``*``, ``/``


.. admonition:: Activity

    Generate expressions to:

    #. Add two variables together (use whichever values you want) and save the result to some variable.
    #. Multiply two variables together and save the result to some other variable.
    #. Divide result of step 2 by the result of step 1.
    #. Add a third variable to the result of step 3.


.. admonition:: Activity

    Now for a tougher one. Convert a temperature from Celsius to Fahrenheit.
        * `But I don't know how to convert Celsius to Fahrenheit!!!! <https://www.google.com/search?q=how+to+convert+celsius+to+fahrenheit>`_

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/R1ScWDNUEnM" frameborder="0" allowfullscreen></iframe><br><br>

   
Operators On Other Types
========================

* There are operators for values other than just numbers
* We will see many of these as we move through the course

.. admonition:: Activity
   
    #. Experiment with the operators you know on *strings* (instead of just integers).
    #. Which ones work? What do they do?
    $. Try mixing strings and integers with various operators. What happens there?

   
Large Series of Statements
==========================

* So far we have been writing programs that are about one line long
* There is nothing stopping us from writing large programs with many lines of code
    * Saved in Colab or some other file
* We often call these Python programs **scripts**
* Python will run each line of the program, one line at a time, in the order that they exist

* Technically you can write your script in any text editor, but there are editors/environments designed for programming languages
    * Colab (use through the internet)
    * Notepad++ (Windows)
    * Sublime (Windows and Mac)
    * PyCharm (Windows, Linux, and Mac)
    * VS Code (Windows, Linux, and Mac)


.. admonition:: Activity

    Consider the sentence "I am taking CSCI 161". Write a program that stores each word of that sentence in it's own
    variable, and then prints the whole sentence to the screen, using only a single ``print``.

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/u-d3chSpFO4" frameborder="0" allowfullscreen></iframe><br><br>


For Next Class
==============

* If you have not yet, read the rest of `Chapter 2 of the text <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html>`_
