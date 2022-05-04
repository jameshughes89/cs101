*****************
Strings & Objects
*****************

* Strings are a little different when compared to the other types we have seen (``int``, ``float``, ``bool``)
* Classically speaking, a string is a collection of individual characters
* In fact, we can *index* the string to access individual characters from it

.. code-block:: python
    :linenos:

    some_string = "Hello, world!"
    print(some_string[0])   # prints out 'H'
    print(some_string[4])   # prints out 'o'


.. note::

    In Python, and many other programming languages, the index for the beginning is actually ``0``, not ``1``. There are
    some historical and engineering reasons for this, and there are plenty of programming languages that start at ``1``
    too. This can feel tedious for new programmers, but it will become natural to you.


.. admonition:: Activity
    :class: activity

    #. Write a single line command to print the first 4 characters of some string.
    #. How about the 2nd to 7th characters?
    #. Get the last three characters? **Hint:** what does a *negative* index do?
    #. `Get the length of a string. <https://www.google.com/search?q=get+the+length+of+a+string+python>`_
    #. What does ``print(a[0:4])`` do?

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/cxppFPrjcow" frameborder="0" allowfullscreen></iframe>


For loops
=========

* We can find the length of a given string with ``len(some_string)``
* And we know we can index individual characters from a string
* Let's write a function ``vertical_print_while`` that prints a string vertically (one character per line)

.. code-block:: python
    :linenos:

    def vertical_print_while(a_string: str):
        """
        Print out a string vertically. In other words, print out a single character on each line.

        :param a_string: Some string to print out
        :type a_string String
        """
        character_index = 0
        while character_index < len(a_string):
            print(a_string[character_index])
            character_index += 1


.. admonition:: Activity
    :class: activity

    Write the ``vertical_print_while`` function yourself. Try not to just copy/paste the provided solution. Call the
    function on a few different strings to see if it behaves the way you expect.

     .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/YS2TVVTIaPQ" frameborder="0" allowfullscreen></iframe>


* The ``while`` loop worked perfectly fine
* But there is another type of loop called a ``for`` loop that may feel a little nicer to use in this scenario
* These ``for`` loops are great for when we have a collection of *things* and we want to do something for each of those *things*

.. code-block:: python
    :linenos:

    def vertical_print_for(a_string: str):
        """
        Print out a string vertically. In other words, print out a single character on each line.

        :param a_string: Some string to print out
        :type a_string String
        """
        for char in a_string:
            print(char)


* The ``while`` loop will continue to run ``while`` the condition is ``True``
* The ``for`` loop will run for each *thing*
* In this example, the ``for`` loop will run for each character in the string

* If we were to call ``vertical_print_for("Hello")``

    * The first time through the loop ``char`` would have the value ``"H"``
    * The second time ``char`` would have the value ``"e"``
    * The third time ``char`` would be ``"l"``
    * Fourth time ``char`` is ``"l"`` again
    * The fifth time ``char`` is ``"o"``
    * The loop ends as there are no more characters in the string


* Both the``while`` and ``for`` loops are perfectly fine for this situation

    * But you may find the ``for`` loop has a little nicer syntax

.. note::

    In the ``vertical_print_for`` example, the use of the variable name ``char`` in the ``for`` loop is arbitrary. It is
    just a variable name and is not required to be ``char`` because the things in the string are characters. I chose
    ``char`` since it is an appropriate name for the variable. For example, the following code would work:

    .. code-block:: python
        :linenos:

        for terrible_variable_name in a_string:
            print(terrible_variable_name)


Immutability
============

* Although we can access individual characters at a specified index

    * ``some_string[an_index]``

* We cannot *change* the value at a specified index

    * ``some_string[an_index] = "X"``
    * If you try this, you will get ``TypeError: 'str' object does not support item assignment``

* This is because strings are **not** mutable

    * They're immutable
    * Fancy way of saying, once they exist you cannot change them

* However, there is nothing stopping us from making a new string based on the old

.. code-block:: python
    :linenos:

    a_string = "Hello, world!"
    b_string = a_string[:5] + "!" + a_string[6:]


in
==

.. admonition:: Activity
    :class: activity

    Write a function ``char_is_in(char,string)`` that returns ``True`` if the character ``char`` appears in the string ``string``.
    
    * HINT: what does the ``in`` operator do in Python?

     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/sokPQLkrXjw" frameborder="0" allowfullscreen></iframe>
   

* You can do the above exercise the hard way, with loops, or you can look up ``in``.

.. admonition:: Tricky Activity

    What's wrong with this?::
   
        def char_is_in(char, string):
            count = 0
            while count < len(string):
                if string[count] == char:
                    return True
                else:
                    return False
                count = count + 1

    * Try: `char_is_in('t', 'test')`
    * Try: `char_is_in('z', 'test')`
    * Try: `char_is_in('e', 'test')`

.. admonition:: Activity
    :class: activity

    Write a function ``where_is(char,string)`` that returns the *index* of the first occurrence of ``char`` in ``string``.

String Trivia
=============
* ``''`` or ``""`` will work for the quotes needed for strings
    * But you can put ``''`` inside ``""`` s
   
    >>> a = "Hello, 'world'"
    >>> print(a)
    Hello, 'world'
   

* We can concatenate strings
    >>> a = 'FuN' + ' ' + 'tImEs'
    >>> print(a)
    FuN tImEs
   
* We can make a string repeat
    >>> a = 'FuN' * 3
    >>> print(a)
    FuNFuNFuN
   
* We can convert an ``int`` to a ``str``  
    >>> print(type(1))
    <class 'int'>
  
    >>> print(type(str(1)))
    <class 'str'>

* The string ``''`` is a string, but it's *empty*
    * This is a weirdly important detail actually

    >>> a = ''
    >>> print(len(a))
    0
   
    >>> print(type(a))
    <class 'str'>

* We have some special *characters* that we have no buttons for.
    * '\\\n'
    * '\\\t'
    * '\\\\'
    * There are a bunch 
    
    >>> a = 'hello\nWorld\tFUN\\!'
    >>> print(a)
    hello
    World   FUN\!	# A weird string
      
* ASCII Table
    * Every *character* is a *number*

    .. image:: ascii.gif
   
    >>> wut = ord('a')	# get the num of 'a'
    >>> print(wut)
    97
   
    >>> wut = chr(65)	# convert num to char
    >>> print(wut)
    A
   
Formatting output (the ol' trusty way)
======================================

**%.2f** (percent dot two eff)

* f is for float
* Right side of **.** is for decimal places

    >>> a = 1.235
    >>> print('Format to 2 decimal places: %.2f' %a) # it will round too!
    Format to 2 decimal places: 1.24		
  
    >>> b = 4.39999
    >>> print('a: %.2f b: %.4f' %(a, b))	# need parentheses if more than one value to be inserted
    a: 1.24 b: 4.4000
   
* Left side of **.** is for specifying total string length
   
    >>> a = 1.311
    >>> print('3 of the 5 chars: %5.1f' %(a))
    3 of the 5 chars:   1.3	# len('1.3') = 3
    
    >>> print('4 of the 5 chars: %5.2f' %(a))
    4 of the 5 chars:  1.31
   
    >>> print('5 of the 5 chars: %5.3f' %(a))
    5 of the 5 chars: 1.311

* Left justify 

    >>> a = 1.311
    >>> print('%-10.2f neato' % a)
    1.31       neato
    
    >>> print("%-10s%10.2f" %('Total:', a))
    Total:          1.31

* Many old programming languages do it this way
    * And there are a billion other options too
* `There are new ways to format your strings in Python though <https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python>`_
    * .format()
        * Probably the best way to do it in Python these days
    * f-strings
    * Check them out if you care

   
Objects
=======

.. warning::
   
    Some of the following is not actually true for Python, but will be the case for many of the commonly used programming languages. 
   
    Also, we will be going into more detail on Objects later in the class.

* We have seen *primitive* types
    * Int
    * Float
    * Booleans
   
* There are other *types*:
    * Strings (actually kinda' a primitive type in Python, but let's ignore this ...)
    * Numpy things 

* These are objects!
* We can even make our own *objects* 
    * stay tuned
* These objects act a little differently inside the computer 
    * For good reason too, but stay tuned. 


Methods
=======
* We've seen built in functions 
    * ``print('this is a function')``
* We've written our own functions
    * ``char_is_in('a','bleh')``

.. admonition:: Activity
    :class: activity

    In Colab (or whatever IDE):
        1. Make a string
        2. Assign it to a variable (if using Colab, hit run too)
        3. Type the name of the variable
        4. Press dot (period)
        5. Wait... (or space or press ctrl-space (depends on IDE))

    .. image:: methods2.png
    .. image:: methods.png

.. admonition:: Activity
    :class: activity

    1. Try writing ``a_string.upper()`` and printing it out. 
    2. Try some other *methods*
   
* *Methods* are very very similar to *functions*
* But we're telling a specific *object* to do something
* Long story short:
    * Sometimes we do things with functions
    * Sometimes we do things with methods

BUT WAIT...
-----------

* Why do we have to do it like this ``a_string.upper()``
* As opposed to like this: ``upper(a_string)``

Answer
------

1. Because... 

2. ``upper(a_string)`` is not actually defined 

    * unless we define it ourselves

3. These methods were written by someone, and they wrote them to work a certain way

    * Not necessarily the best way, or a way you like

4. There's also a good bookkeeping argument too

    * Put all the string methods with the strings

5. But really... because
   

How are you supposed to keep track of what's what?
--------------------------------------------------

* Don't worry, you'll get it with practice
* Do note though, **the key is practice** 

Heavy lifting with strings
==========================
* If the program you are writing needs to do a lot of string manipulation, you probably want to
    >>> import string
* ... and `read about all the nifty stuff it does <http://docs.python.org/library/string.html>`_ 

For next class
==============

* Read `chapter 11 of the text <http://openbookproject.net/thinkcs/python/english3e/lists.html>`_

