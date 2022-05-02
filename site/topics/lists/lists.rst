******************
Lists & References
******************

* We saw that strings were a little different when compared to the other types we've seen (``int``, ``float``, ``bool``)
* We can generalize the idea of strings to more types

    * A string is a collection of characters
    * We can use lists to have a collection of other types


.. admonition:: Activity

    Run the following code:

    .. code-block:: python
        :linenos:

        some_list = [5, 7, 9, 10]
        print(some_list)
        print(some_list[0])
        print(some_list[1:3])
        print(type(some_list))

    #. Determine what types can be in a list.
    #. Can a list contain things od different types at the same time?
    #. How can you access the last element in a list?
    #. Can we find the length of a list?
    #. Is it possible to have a list of length 0? This would be an empty list, or a list with nothing in it.


Data Structures
===============

* The ``list`` is your first real **data structure**.
* The name "data *structure*" pretty much tells you everything you need to know.
    * A data structure is a formal way to *structure* data.
* Lists, although simple, are one of the most useful and powerful of all data structures.
    * Sometimes they are a bit slower than more specialized alternatives.
        * This isn't a big deal for us though.

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/EcuTE0VEDl8" frameborder="0" allowfullscreen></iframe>



.. admonition:: Activity

    Let's apply what we've learned about loops to our newfound ``list`` data structure. Combining algorithms and data structures is what programming is all about!
   
        1. Figure out how to find the number of elements in a list.
        2. Write a function ``print_list(l)`` that takes a list ``l`` as its argument and prints out the elements of the list
        3. Write a function ``even_print(l)`` that takes a list ``l`` as its argument and prints out only the even elements of the list.
        4. Write a *single line* of Python code to test if a particular value appears in a list (e.g. test if ``5`` appears *in* ``[1,7,5,3]``.)

List operations
===============

* We can concatenate lists with the ``+`` operator:
    >>> a=[5,7,9,10]
    >>> b=['also','a','list']
    >>> a+b
    [5, 7, 9, 10, 'also', 'a', 'list']

* We can concatenate a list with itself, multiple times, using the ``*`` operator:
    >>> a*3
    [5, 7, 9, 10, 5, 7, 9, 10, 5, 7, 9, 10]
* Can we do this with Strings?
* As you've discovered for yourself, we can also *slice* lists (just like we did strings), find their size and check for membership.

Range
=====

* In real world programming applications, we very frequently need a list of integers.
    * For example: ``[1,2,3,4,5,...]`` so that we can count things.
* Python has a built in function ``range()`` that we can use to generate lists of integers for us:
	>>> list(range(1,5))
	[1, 2, 3, 4]
    
	>>> list(range(5,10))
	[5, 6, 7, 8, 9]
	
.. admonition:: Activity

    Generate the following lists, using ``range``:
        1. All integers from 0 to 17
        2. All integers from -10 to 0
        3. All integers from 10 to 0 (that is: counting *down* instead of up)
        4. All even integers from 0 to 20
	 
    If you're having trouble with the last two, look up the `docs for range <http://docs.python.org/library/functions.html#range>`_ .

    **WARNING** This is a tad different in Python 2, so be mindful of that when watching the video.
    
     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/izZEkV58Its" frameborder="0" allowfullscreen></iframe>


Mutability 
==========

* Strings do kinda look like "list of characters" and, in many ways, they are.
* *But not exactly*.
* Strings, remember, are *immutable*. What about lists? Let's try:
    >>> a=[5,7,9,10]
    >>> print(a)
    [5, 7, 9, 10]
    
    >>> a[2]='I changed!'
    >>> print(a)
    [5, 7, 'I changed!', 10]
* Unlike strings, lists are *mutable*.

.. admonition:: Activity

    Consider the list ``l=list(range(0,10))``. Find single-line commands to do the following:
        1. Change the 5th element of the list to ``'X'``.
        2. Replace the first two elements of the list with ``10`` and ``11``, respectively. Remember, single line only! (Hint: slicing)
        3. Delete the two elements you just changed. (Hint: what does assigning the empty list to a slice do?)

* A 'cleaner' way to delete an element from a list is with the ``del`` statement:
   
    >>> a=[5,7,9,10]
    >>> a
    [5, 7, 9, 10]
   
    >>> del a[2]
    >>> a
    [5, 7, 10]


.. _label-topic8-aliasing:

Aliasing 
========



* Pay attention here, because this is a *major* source of confusion for new programmers.
    * It's not actually that weird, but it does trip people up

* This code should look normal

    >>> a = 5
    >>> b = a
    >>> print(a, b)
    5 5
    
    >>> b = 7
    >>> print(a, b)	# a will be left unchanged
    5 7   	
   

* Suppose you have a **list**, ``big_list`` with 500 billion entries in it.
* That's a big list. Probably uses a lot of RAM.
    * A lot of space inside the computer.
* Now you type:
    >>> new_list = big_list
* What seems like a better idea:
    * Copy all 500 billion entries into ``new_list``, using twice as much RAM to store the same data.
    * Memorize the fact that ``new_list`` is just another name (*alias*) for ``big_list``. Copy nothing.
* Pretty obvious when you think about it that way, but less obvious when your lists only have 5 items in them.
* like this:
    >>> a=[1,2,3,4]
    >>> print(a)
    [1, 2, 3, 4]
    
	>>> b=a
	>>> b[2]='Z'
	>>> print(a)	# OMG, a was NOT left unchanged!!!!!!!!!
	[1, 2, 'Z', 4]
* You should probably pay attention to this
    * Probably one of the more annoying things new computer scientists have to deal with 
* If you expect ``b`` to be a *full copy* of ``a``, what just happened makes no sense.
* If you expect ``b`` just to be another name for ``a``, it makes perfect sense.

.. warning::

    In Python, when you "assign" a list, you **are not copying the list**. You are saying 'this is another name for the exact same list'. You are giving it an *alias*. 
   
* The reason this is so upsetting is that this behaviour is *different* from what happens with simple values like ``int``, ``float``, etc. You have to make an effort to remember that "=" means something different for lists than it does for other types. C'est la vie.
* Suppose you *really want* to **copy** your list instead of just giving it another name. You can do that easily enough using slicing: ``new_list = big_list[:]``. Slicing always creates a *new* list.
  
    >>> a=[1,2,3,4]
    >>> print(a)
    [1, 2, 3, 4]
    
	>>> b=a[:]
	>>> b[2]='Z'
	>>> print(a)
	[1, 2, 3, 4]


  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/2F_qnTYA6g4" frameborder="0" allowfullscreen></iframe>

* Spend some time getting used to this concept. I promise you, 100%, it will cause bugs in your code.
    * Happens to me all the time :(



.. admonition:: Activity

    Create a list named ``l``. Make an *alias* of the list named ``lalias``. Make a *copy* of the list named ``lcopy``. Prove to yourself that one is an alias and one is a copy.

Pointers (THIS IS ACTUALLY A BIG DEAL)
======================================

* Here is an idealized view of RAM inside a computer

.. image:: RAM.png

.. warning::

    We actually typically think of RAM addresses in *hexadecimal* (we use symbols 0-F). I'm just using decimal numbers here for simplicity. 
   
    Check this out though. We can sometimes see where things are stored in RAM. 
   
    Note that the ``0x`` means that the number is in hexadecimal

    .. image:: functionLocation.png

Fixed Size Arrays
-----------------
   
* Let's hit pause on lists for a sec and go back in time
* In many programming languages, lists aren't *free* like they are in Python
* Instead, we have *arrays*: Fixed size collections of data 
    * Like a list, but fixed size, and no fancy methods
        * BTW, the following is basically the same for lists too, but slightly easier to explain if we talk about arrays
 
.. image:: array_1.png
 
 
* Above is an array with length **8**
    * No making fun of my *Microsoft Paint* skills
* The contents are labeled *a -- h*, but let's pretend they're numbers


Primitive Types in Memory (RAM)
-------------------------------

* Let's say we have a single integer called ``x`` (so, not an array anymore)
    * I know it's an ``x``, but let's pretend it's some value of type *int*
* An integer is a primitive type

.. warning::

    Unlike many languages, ints are actually *objects* in Python, but we're still ignoring this for now to learn an important concept from the olden days that still applies to Python due to conventions 
   
* We know how big an integer can be inside the computer (how much RAM an int takes up)
    * And why do we know how big it is? 
        * Because some engineer said so
    * Let's say an int can be *32-bits*
    * That's 32 0s and 1s
    * Ex: 00101010010010110101110100010100
        * That's 709,582,100 if anyone cares

* If we know how much RAM an int takes up, I can easily shove ints into nicely divvied up chunks of RAM, assuming each spot has 32 bits. 

* Let's say I type

>>> x = 17

.. image:: Int_in_RAM.png

* Something like this will happen. 
    * The value 17 will go into one of the open divvied up chunks of RAM
    * We create a label for the value called ``x``
   
* If I say something like

>>> y = x

.. image:: copy_int_in_RAM.png

* Something like this will happen. 
    * Copy the contents in the location that the ``x`` refers to some other location
    * Create a label for the copied value called ``y``
   
* **I COPY OVER THE CONTENTS OF X AND PUT IT INTO Y**

* So far this is fine and dandy
* But, what happens if we try to shove an array into one of those nicely divvied up chunks of RAM?
    * The RAM is divvied up to accept single ints
    * But we have an array of 8 ints...
    * PROBLEM!

* Wait, there's actually a simple solution. What if we block off chunks of RAM to be the array?
* So if I have the array ``[a, b, c, d, e, f, g, h]``, we get this...

.. image:: array_in_RAM.png

* We're just putting each element into it's own RAM location
* We just need to know that our array starts at memory address 677 and goes to 684.

* ... but... how do we keep track of this?

Pointers
--------

* Let's see what happens when we say this (people always say how complicated this is, but it's really not when you understand the intuition): 

>>> z = [a, b, c, d, e, f, g, h]

.. image:: array_pointer.png

* ``z`` gets us to a memory location whose contents is another memory address (pointer)
    * It effectively *points* to another chunk of RAM

.. admonition:: Activity

    Take 1 min and look at this picture and see if you can explain why we start counting at 0 when indexing lists/arrays.
   

* Earlier we saw that lists work a little differently when saying something like

>>> my_list = [1,2,3]
>>> another_list = my_list
>>> another_list[1] = 99
>>> print(my_list)
[1, 99, 3]
 
* We called this aliasing and took note that it's weird
* However... actually... the way we copy over ``my_list`` to ``another_list`` works THE SAME WAY AS PRIMITIVE TYPES
    * But... You just said.. and you clearly showed us that it's totally different!!!!!!!!

* Strap yourselves in, because I'm about to blow your mind

* Let's say I write

>>> w = z

.. image:: array_pointer_copy.png


* Just follow the rules we followed for primitive types
   * Copy over the contents of z to an open memory location
   * Give it the label ``w``
   
* How many pointers do I now have that get me to the same memory location?

* Now let's look at what happens if I do this

>>> w[4] = P

.. image:: array_pointer_copy_change.png

* Did I change the contents at the memory location ``w``?
   * No, I changed something that the pointer in the memory location ``w`` was pointing to!!

* Memory (typically) works like this for non-primitive types (objects)
   * Arrays
   * Lists
   * etc. 
   
 
Lists and loops 
===============
* ``for`` loops can be used to execute a block of code for every element in a list::

    for element in some_list:
        do_something(element)

* Just like the loop we did with Strings last class!
* This is incredibly useful. In fact, you've already seen it in assignment 1. Let's try it::

    def like_food(food_list):
        for food in food_list:
            if food not in ['McDonalds','Burger King']:
                print('I like ' + food)
            else:
                print('I dont like ' + food + ' so much.')

* And now we'll run our function:

    >>> like_food(['curry','sushi','McDonalds','bison'])
    I like curry
    I like sushi
    I dont like McDonalds so much.
    I like bison


.. admonition:: Activity

    Write a function ``beer_on_wall`` that will print out "n bottles of beer on the wall" for all n from 99 down to 1.
   
    Remember: ``range`` returns a list (kinda)... and a ``for`` loop can *iterate* over every element of a list.

     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/0AuMKIMiPMo" frameborder="0" allowfullscreen></iframe>



* Suppose I want to print out a list of strings, in order, with each element preceded by number indicating it's position in the list::

    >>> list=['a','b','c','d']
   
    >>> for index in range(len(list)):
            print(index, list[index])
   
    0 a
    1 b
    2 c
    3 d

* What is going on in ``range(len(list))``? Break it down one step at a time.
* This pattern is so common that Python has given us a built in function ``enumerate`` to enumerate lists in a loop::

    for index, item in enumerate(list):
        print(index, item)
      
* Most of our ``for`` loops have only a single *loop variable*...
* ... but.. notice how instead of a single loop variable, we now have *two* (``index`` *and* ``item``). They iterate together in lockstep. 
  
    * ``index`` gets the index of the item in the list
    * ``item`` gets the actual item itself
	 
* This is a special feature of the ``enumerate`` function.

Mind the rotating knives
========================

* Remember how assigning lists wasn't really *copying* them, but just creating a new name?
* I wonder what happens when you pass a list to a function as an argument?
    * Does the function get it's own copy?
    * ... or does the function just get an alias to the same list?
   
.. admonition:: Activity

    Figure out the answer to this question empirically. Write a function that will prove to you which of the two options above is correct. 
  
Side effects
============


* Consider the code::

    def add_to_list(my_list):
        my_list.append('appended')

* Now consider the code::

    def add_to_list_2(my_list):
        return my_list + ['appended']
  
.. admonition:: Activity

    What happens when you do this?
      
        >>> a = [1,2,3,4]
        >>> add_to_list(a)
        >>> print(a)
      
   How about this:
   
        >>> a = [1,2,3,4]
        >>> add_to_list_2(a)
        >>> print(a)

   Finally, how about this:
   
        >>> a = [1,2,3,4]
        >>> b = add_to_list_2(a)
        >>> print(a)
        >>> print(b)

* The function ``add_to_list`` *modified* the parameter you passed in.
* The function ``add_to_list_2`` kept a respectful distance from your parameter and, instead, created a *new* list and *returned* that as the answer.
* If a function modifies a parameter it is said to have *side effects*.
    * The term "side effect" comes from our mathematical expectation of a "function". A function maps some parameters on to a value. If I give you the function `f(x,y,z)=x+y-z` and ask you to evaluate `f(1,2,3)`, you don't expect the values of `x`, `y` and `z` to change!

Pure functions
==============
* If a function has no side effects, we call it a *pure function*.
* Some programming languages allow *only* pure functions (e.g., `Haskell <http://www.haskell.org/haskellwiki/Haskell>`_).
    * There are some nice theoretical, and practical benefits to this.
* As you might guess from the ameliorative term "pure"... functions with side effects are considered... "not pure"... even downright dirty, by some folks.

.. admonition:: Activity

    Think of three potential advantages to pure functions over functions with side effects.
  

Who wants to be pure?
=====================
* Anything you can possibly do with a computer *can* be done with pure functions...
* ... but... some stuff is just plain easier to do with side effects. 
* This is a course for working scientists, so let's be pragmatic:
    * Write pure functions when practical to do so. The advantages make it worthwhile.
    * If it really is a lot easier to do the job with side effects... just do it and don't lose sleep over it.
   
  
	  
	  	  
For next class
==============
* Read `chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
* Read `chapter 15 of the text (only lightly though) <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_


