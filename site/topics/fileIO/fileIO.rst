*******
File IO
*******

Getting data into Python
========================

* You now know a lot about how to *manipulate* data.
* But you probably want to manipulate *specific* data. *Your* data. Not toy examples.
* We need to learn about **File I/O**.
* I wont lie to you: file I/O is boring, painful, detail-oriented work.
* Fortunately, Python makes it less painful than just about any other language I've ever used.

Read/Write to a text file
=========================

* There are a bunch of ways to do it, but here's one.

>>> my_file = open('aFileName.txt', 'r')

* Done (many programming languages do NOT make it this easy)
* This assumes the file is in the working directory
* Take a wild guess what 'r' means

.. admonition:: Activity
    :class: activity

    1. Create a text in the working directory. If using Colab, you'll have to get one there. 
    2. Open it like the above
    3. Try using the methods ``.readline()`` and ``.read()``
   
* There are a lot of methods, these are just two.

* How about writing to a file? 

>>> my_other_file = open('anotherFileName.txt', 'w')

.. admonition:: Activity
    :class: activity

    Try to figure out how to ``write`` to this file. 


* When done with files...
* Listen up, this is a very very important thing
* Pay attention
* **We must close them!**
* Failing to do this can cause serious issues!!
    * Seriously, I've spent longer than I would like to admit in my life looking for bugs that were just a result of me not closing my files. 
   
* Fortunately it's easy to close them

>>> my_other_file.close()


Loading a CSV file
==================

* Regular text files are cool, but CSVs are a great way to format data. 

* CSV stands for "Comma Separated Values".
* The file is stored in plain text (you can read it with a text editor)
* Delivers what it promises.
* Each line of the file is one item.
* Within the line, each value associated with that item is in a comma-delimited field.
    * Some people will use tabs or other things, but commas are best. 
* For example, suppose I have recorded height, weight and IQ for 3 subjects::

    name, height, weight, IQ
    Subject 1, 170, 68, 100
    Subject 2, 182, 80, 110
    Subject 3, 155, 54, 105
   
* The first line is a *header*, explaining the values in each field. 
* Headers are *not* mandatory. Some CSVs have 'em, some don't.
* Good news: Python has a built-in library to read CSV files for you!
* In fact, we've seen this before::

    def load_asn1_data():
        """
        This function loads the file `starbucks.csv` and returns a LIST of
        latitudes and longitudes for North American Starbucks'.
        We'll talk about lists formally in class in a few lectures, but maybe
        you can start guessing how they work based on what you see here...
        """
	
        import csv
	
        reader = csv.reader(open('starbucks.csv', 'r'))
        locations = []
	
        for r in reader:
            locations.append( (r[0],r[1]))
		
        return locations

* How does the ``csv.reader`` work?

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/HUHqBtNWJo8" frameborder="0" allowfullscreen></iframe>
	
.. admonition:: Activity+
    :class: activity
	
    Figure out how it works. Download :download:`this csv file <airports.csv>` to your computer. **NOTE:** If using Colab, you'll have to upload it.
   
    Now write a function called ``load_airports()`` that loads this CSV file into a list. 

    Play with this list a bit and get a feel for how the data is organized.

.. admonition:: Activity+++
    :class: activity

    Now write a function ``get_name_from_code(airport_code, airport_list)`` that will return a string containing the full name of the airport with the code ``airport_code``. 

    The parameter ``airport_list`` should be the list you loaded using ``load_airports()``.


      .. raw:: html
	
		<iframe width="560" height="315" src="https://www.youtube.com/embed/9wunG22ivJ0" frameborder="0" allowfullscreen></iframe>
   
* Suppose you have some tabular data in Python that you want to save back in to a CSV

    >>> csv_out = csv.writer(open('yourFileName', 'w'))
    >>> csv_out.writerow(['First cell','Second cell', 'Third cell'])
    write as many rows as you need to... maybe in a loop?
   

* CSV files are popular because they're simple.
* You can, e.g., export any Excel spreadsheet as a CSV.
* If you have tabular data, this is a decent choice of format.
* If you don't have tabular data... this is an awful choice.

   
Exceptions
==========

* I'm not gonna' go into too much detail on *exceptions*, but I want you to be aware of them and what they are
* You've all seen these

>>> int('hello')
ValueError: invalid literal for int() with base 10: 'hello'

>>> a = ['a', 'e', 'i', 'o', 'u']
>>> print(a[11])
IndexError: list index out of range

* ``ValueError`` and ``indexError`` are exceptions. 
    * There are a bajillion more

* When we tried to convert the string 'hello' to an integer, the code *raised* an exception
* When we tried to access the 11th thing from the list of only 5 things, the code *raised* an exception
* Why?
* Well, whoever wrote the code you're trying to use for converting strings to ints and accessing lists had to have a way to deal with *exceptional* situations. 
* It's kinda' like the programmer of the code you're trying to use is saying:
    * You're trying to ask me to convert 'hello' to an int? Nope... Can't do it... But that's not *my* problem, that's **your** problem
* So they told their code to ``raise`` an exception. 
* When this exception is raised, it's now **YOUR** problem!


* Here is a super contrived example of writing our own code to ``raise`` an exception...
    * A lot of other programming languages call this ``throw``

.. code-block:: python

    def do_not_give_me_five(n):
        if n == 5:
            raise ValueError('I TOLD YOU NOT TO GIVE ME 5!!!')
        else:
            print(n)
   
>>> do_not_give_me_five(4)
4

>>> do_not_give_me_five(5)
ValueError: I TOLD YOU NOT TO GIVE ME 5!!!

* You may be wondering what the point is then
* Well, here is perhaps a better example

.. code-block:: python

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError('Nooooo!')
        else:
            return a/b

* This function I just wrote will first check if ``b`` is ``0``. If it is, it will ``raise`` an exception.

Catching Exceptions
===================

* Exceptions are not necessarily errors. They are *exceptional situations*.
* Let's consider ``divide`` above
    * Although you could think about any other thing you've tried to do before that returned an exception, like converting 'hello' to an int, or indexing something that does not exist.

* Pretend I wrote this divide function in 1999 and now everyone today is using my super awesome function. 
* You come along today and call ``divide(9,0)``

1. I can't divide 9 by 0. That's a no-no.
2. What should *I* do about it in 1999?
3. Well... you're writing a program right now trying to use this function to do something
4. How could I know how to handle this situation in YOUR program?
5. How about this... How about I write some code in my 1999 code that says "SOMETHING EXCEPTIONAL HAPPENED" that lets YOU know that something is off.
6. Then YOU can handle these exceptional situations however YOU want. 

    * Crash?
    * Carry on?
    * Try again?
    * Call the user a moron?
   
So here's the rule, let's say I'm going to use a function that might throw an exception.

1. I will ``try`` to run the code that may or may not ``raise`` an exception
2. The code will run normally ``except`` if the exception is raised. 

.. code-block:: python

    def my_code():
        try: 
            function_that_can_raise_exception()
        except SomeError:
            code
            that
            will
            handle 
            situation
        code
        that
        runs
        regardless
	  
* The code in the ``except`` area only runs if an exception happens
* If no exception happens, then the code is skipped
* It's kinda' like ``if`` statements, but for exceptions

Divide Example
--------------

* Let's look at a couple of examples of people using ``divide``
   
Jane example

* Jane wants us to set the result to NaN (not a number) if we try to divide by zero.

.. code-block:: python

    def jane_code(a,b):
        try: 
            rez = divide(a,b)
        except ZeroDivisionError:
            rez = float('NaN')
        print(rez)

* What's happening?
    * If we call ``divide`` and nothing funny happens ``rez`` becomes the result
    * If an exception is thrown, ``divide`` never finishes doing its thing and we set ``rez`` to ``NaN``. 
    * Then, either way, we print out ``rez``

   
Bob example

* Bob just wants to have his program keep asking the user for input until it can divide the numbers

.. code-block:: python

    def bob_code():
        while True:
            data = input().split()
            a = int(data[0])
            b = int(data[1])
            try: 
                rez = divide(a,b)
                break
            except ZeroDivisionError:
                print('Bad input for divide (divided by 0), try again')
			
        print('Im outside the loop')
	  
	  
	  
Tim example

* `Tim is programming a piece of medical equipment that gives radiation therapy to people, and if the calculation goes wrong, we need the equipment to stop immediately otherwise we might give someone radiation poisoning <https://en.wikipedia.org/wiki/Therac-25>`_.

.. code-block:: python

    def tim_code(a,b):
        try: 
            rez = divide(a,b)
        except ZeroDivisionError:
            exit()	# Immediately stop!
        print('I am going to give you radiation therapy now.')


Sally example

* `Sally is writing code for a helicopter. If the calculation does not work, we still want the program to run and keep us in the air <https://en.wikipedia.org/wiki/1994_Scotland_RAF_Chinook_crash>`_.

.. code-block:: python

    def sally_code(a,b):
        try: 
            rez = divide(a,b)
        except ZeroDivisionError:
            print('Error in calc. I will stay in the air though. ')
        print('Keep Flying')


Exception Types
===============

* There are A LOT of types of exceptions/errors out there
* We can even make our own (outside the scope of this class though)
* There is even a hierarchy 
    * `I stole this pic from here <https://o7planning.org/en/11421/python-exception-handling-tutorial>`_ 

.. image:: exceptions.png


Exceptional vs Error
==================== 
	
* I'm not gonna' get too far into this, but long story short, there are some exceptions that are exceptional situations, and some that are just plane errors on the programmer's part. 
* Things like ``IndexError: list index out of range`` are probably errors you made
* Things like ``FileNotFoundError:`` are probably issues with the how the code was used (trying to open a file that does not exist), and not really an *error*


	
Why do we care about exceptions?
================================

* It allows programmers to pass info around and communicate through TiMe
* It allows us to deal with exceptional situations effectively
* It gives us a nice logical division between normal code and exceptional code



For next class
==============

* Read `chapter 15 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_  
* Read `chapter 16 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html>`_  

