**********
References
**********

* It is important for us to have an idea of what exactly is stored in our variables

.. warning::

    The ideas below are presented at a very high level and are not quite entirely correct for Python and other similar
    programming languages. The differences come up in the nuances, but the following is sufficient to cover the
    important ideas that you need to know. In fact, where there are differences between the following and how Python
    actually works is not overly important for us, especially in introductory computer science.


.. note::

    We typically use *hexadecimal* (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F) when referring to memory addresses,
    but for simplicity, we will use decimal numbers throughout this topic.


* Here is an idealized view of memory inside a computer

.. image:: RAM.png


Primitive Types in Memory
=========================

* Let's say we have a single integer called ``x``
* An integer is a primitive type
* In many programming languages integers take up **32 bits** worth of memory

    * That means 32 0s and 1s
    * E.g. ``00101010010010110101110100010100``, which is the number ``709582100``

* Since we know how much memory an integer takes up, we can easily put integers into nicely divvied up chunks of memory

* If we divided memory into blocks of 32 bits
* And we create an integer variable ``x = 17``
* Something like this will happen

    * The value ``17`` gets assigned to one of the 32 bit sections of memory
    * A label ``x`` is created for that location

.. image:: int_in_RAM.png


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

Idealized View of a List
========================

.. image:: array_1.png

* Above is an array with length ``8``
* The contents are labeled ``a`` -- ``h``, but these are arbitrary labels and we can think of them as integers




References
----------

* Let's see what happens when we say this (people always say how complicated this is, but it's really not when you understand the intuition): 

>>> z = [a, b, c, d, e, f, g, h]

.. image:: array_pointer.png

* ``z`` gets us to a memory location whose contents is another memory address
    * It effectively *points* to another chunk of RAM

.. admonition:: Activity
    :class: activity

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
   
* How many references do I now have that get me to the same memory location?

* Now let's look at what happens if I do this

>>> w[4] = P

.. image:: array_pointer_copy_change.png

* Did I change the contents at the memory location ``w``?
   * No, I changed something that the reference in the memory location ``w`` was pointing to!!

* Memory (typically) works like this for non-primitive types (objects)
   * Arrays
   * Lists
   * etc. 

	  	  
For Next Class
==============

* If you have not already, read `Chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
* If you have not already, read `Chapter 15 of the text (only lightly though) <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_


