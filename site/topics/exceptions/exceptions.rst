**********
Exceptions
**********

* You have all seen various exceptions in Python

.. code-block:: python

    int('hello')
    ValueError: invalid literal for int() with base 10: 'hello'


* In the above example, when we tried to convert the string ``hello"`` to an integer, Python *raised* an exception

.. code-block:: python

    a = ['a', 'e', 'i', 'o', 'u']
    print(a[11])
    IndexError: list index out of range

* In the above example, when we tried to access the 11th thing in the list containing only 5 things, Python *raised* an exception

* Both ``ValueError`` and ``indexError`` are exceptions, but there are many more kinds of exceptions

* Consider how, like the ``print`` function, someone had to write the code for converting strings to integers and indexing elements form a list
* If I am the one writing the code for converting strings to integers, what should I make my code do if someone asks my code to convert the string ``"hello"`` to an integer?

    * Obviously there is no single obvious and natural way to convert the string ``"hello"`` to an integer
    * Should my code simply ignore the request and carry on like nothing ever happened?
    * Should my code crash the whole program?
    * Maybe some user entered some input wrong?
    * Maybe the issue is with some text file that was read?
    * ...

* The trouble is, if I am writing the code for converting strings to integers, I cannot possibly know what you --- the individual trying to use my code at some point in the future --- want to do in these exceptional situations
* What I can do however is *raise* an exception, which then communicates to the programmer using my code that *they* have to specify what *they* want to do when the exceptional situation arises

* Consider the example below on dividing by zero

.. code-block:: python
    :linenos:

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("Wait, that's illegal")
        else:
            return a/b


* Obviously we're going to have an issue if we try to divide a number by zero
* But what should happen if someone tries to?
* That's entirely up to the programmer making use of the ``divide`` function
* All I need to do is communicate to them that something exceptional happened by ``rais``\int an exception

    * The function first checks if ``b`` is ``0``
    * If ``b`` is ``0``, then the exception is ``raise``\ed
    * If it is not, then the function carries on as it should


Catching Exceptions
===================

* Pretend the above function ``divide`` was written in 1991 and you want to use it today
* When you are using it today, you end up calling ``divide(9,0)``, which is problematic

    * One cannot divide 9 by 0
    * What should the original programmer in 1991 do about it?
    * Well... not much considering you are the one trying to use the function today
    * How could the programmer know what to do to handle your specific situation today?

* What the original programmer can do, however, is to add some special code that says *something exceptional happened* that lets you know that something is off
* This then allows you, the individual trying to use ``divide`` today, to deal with the situation the way you need

    * Crash?
    * Read input again?
    * Carry on as if nothing happened?


* If you are using a function that may result in an exception, you can write your code such that

    * You ``try`` to run the code that may or may not ``raise`` an exception
    * The code will run normally ``except`` when the exceptional situation arises
    * If the exceptional situation arises, special instructions will be specified

* Below is a generalized idea of how one can do this

.. code-block:: python

    def my_code():
        try:
            might
            cause
            exception
        except SomeError:
            will
            handle
            exception
        runs
        regardless


* In the above example, the code in the ``try`` would be something that may cause an exception we want to deal with
* If it turns out that the code does ``raise`` an exception, the code within the ``except`` block runs
* If no exception arises, then the ``except`` block is skipped



Example 1
---------

* There exists a special value for floating point numbers in Python called ``NaN``, which means *not a number*
* A reasonable way to manage a ``ZeroDivisionError`` is to use a ``NaN`` value

.. code-block:: python
    :linenos:

    def not_a_number_example(a: float, b: float) -> float:
        try:
            quotient = divide(a, b)
        except ZeroDivisionError:
            quotient = float("NaN")
        return quotient


* If ``divide`` is called and there is no ``ZeroDivisionError``, then the division occurs and the ``quotient`` is returned
* On the other hand, if a ``ZeroDivisionError`` happens, we assign ``NaN`` to ``quotient`` and return it
* Either way, the ``quotient`` is returned


Example 2
---------


* Consider a program requiring a user to input some values
* If this is the case, it may be ideal to have the program ask for input again if the input was inadmissible

.. code-block:: python
    :linenos:

    def continue_asking_for_input() -> float:
        while True:
            data = input("Provide operands for division: ").split()
            a = float(data[0])
            b = float(data[1])
            try:
                quotient = divide(a, b)
                break
            except ZeroDivisionError:
                print("Cannot Divide By Zero --- Try Again")

        return quotient


	  
	  
	  
Example 3
---------

* It may be the case that if the function causes an exception, our program should stop running immediately
* If this is the case, we can make use of the ``exit()`` function to halt the program

.. code-block:: python
    :linenos:

    def stop_running_immediately(a,b) -> float:
        try:
            quotient = divide(a,b)
        except ZeroDivisionError:
            exit()	# Immediately stop!
        return quotient


* Alternatively, a simpler and better implementation would be to just let the exception propagate up and have the program eventually stop as a result

.. code-block:: python
    :linenos:

    def stop_running_immediately(a,b) -> float:
        quotient = divide(a,b)
        return quotient


* In the above example, if ``divide`` causes an exception, the exception would keep being handed to the calling function until it is dealt with or ultimately crashes the program


Sally example

* `Sally is writing code for a helicopter. If the calculation does not work, we still want the program to run and keep us in the air <https://en.wikipedia.org/wiki/1994_Scotland_RAF_Chinook_crash>`_.

.. code-block:: python

    def sally_code(a,b):
        try: 
            rez = divide(a,b)
        except ZeroDivisionError:
            print('Error in calc. I will stay in the air though. ')
        print('Keep Flying')



Why Care?
=========

* Which of the above examples is the *correct* one?
* The trouble is, that depends on your situation
* The point is, how can the programmer in 1991 know what you want to do with your situation today?

# Exceptions are fantastic because

    * They allow programmers to pass info around and communicate through Time
    * They allow us to deal with exceptional situations effectively
    * They provide a nice logical division between normal code and exceptional code


For Next Class
==============

* Read `Chapter 15 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_


