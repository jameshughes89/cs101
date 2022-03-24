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


For Next Class
==============

* If you have not yet, read the rest of `Chapter 2 of the text <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html>`_
