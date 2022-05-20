******************************
Tuples, Dictionaries, and Sets
******************************

* In addition to lists, there are a few other noteworthy datastructures we will look at in this course
* Although they will not be used as much as lists, it's important to be aware of the tools you have at your disposal


Tuples
======

* A tuple looks and behaves similar to a list, but has slightly different syntax

    * Tuples use parentheses ``(``\, ``)``

    .. code-block:: python
        :linenos:

        some_tuple = (10, 11)
        print(some_tuple)   # Results in (10, 11)


* They are both ordered sequences of data
* They can be indexed like lists

    .. code-block:: python
        :linenos:

        some_tuple = (10, 11)
        print(some_tuple[0])   # Results in 10


* But unlike lists, tuples are immutable

    * Once they are created, we cannot change them

* They're ideal for when we need to pack some data together

    * For example, a tuple would be great for storing cartesian coordinate ``(x, y)``
    * Tuples were also used in the Starbucks assignment to store the latitude and longitude pairs

    .. code-block:: python
        :linenos:

        for row in starbucks_file_reader:
            location_tuple = (float(row[0]), float(row[1]))
            starbucks_locations.append(location_tuple)


Dictionaries
============

* Dictionaries are amazing data structures that are a little more complex than lists and tuples

    * Much of their complexity is hidden from us so we will not worry about it here

* Simply, they are like list that you could index with *strings*, or various other types, instead of just integers
* Consider the following example of storing grades for students

.. code-block:: python
    :linenos:

    # Create a new, empty dictionary
    some_dictionary = {}

    # Add a few things to the dictionary
    some_dictionary["Billy"] = 74
    some_dictionary["Sally"] = 88
    some_dictionary["Jimmy-Bob"] = 99

    # Print out the dictionary
    print(some_dictionary)      # Results in {'Billy': 74, 'Sally': 88, 'Jimmy-Bob': 99}


* In the example, a dictionary was created and three values were added to the dictionary
* But values are associated with unique *keys*

    * The keys must be unique, but the values do not need to be

* The keys in the example are ``"Billy"``, ``"Sally"``, and ``"Jimmy-Bob"``
* Each of the keys have an associated value --- ``74``, ``88``, and ``99`` respectively

* Accessing a value from a specific key from the dictionary is done with indexing

.. code-block:: python
    :linenos:

    print(some_dictionary["Jimmy-bob"])     # Results in 99
    print(some_dictionary["Sally"])         # Results in 88


* And updating a value associated with a key is done just like the original assignment

    * Keys are unique, so using an existing key would overwrite the value and not make a new entry

.. code-block:: python
    :linenos:

    some_dictionary["Sally"] = 90
    print(some_dictionary["Sally"])         # Results in 90



So Why Are They Great?
----------------------

* Imagine we have a 2D list like this:

.. code-block:: python
   :linenos:

    # Creates some lookup table list thing
    grades = [['James', 98], ['Bob', 86], ['Janice', 86], ['Greg', 59]]

* How would we get the grade for any given student?
    * Linear search, right!
    * So there is nothing *wrong* with this, but... there's a better way!

* With a dictionary, we can simply do this!

.. code-block:: python
   :linenos:

    # Creates some lookup table list thing
    grades = {'James':98, 'Bob':86, 'Janice':86, 'Greg':59}

* How would we get the grade for any given student?
    * Just index the dictionary!
    * Way better!

Are They Actually Better?
-------------------------

* Remember how the ``in`` keyword allowed us to do a linear search really easily. 
* It wasn't really *better* than coding a linear search yourself, but it did save some typing. 
* Is the dictionary not just doing the linear search work for us like how ``in`` was?
    * **NO** (asterisk) 
    * But I won't teach you this yet because it's well beyond the scope of this class. 
        * Sorry :(   
   
.. admonition:: `Activity++ <https://leetcode.com/problems/two-sum/description/>`_

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
   
    **EXAMPLE**

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,

    return [0, 1].

Sets
====

* A set is kinda' like a list, but it only holds *unique* things.
* Also, sets typically do not have any ordering to them.
    * Lists start at index 0, then go to 1, 2, ... 
    * Sets start... wherever
   
    >>> a = set([])	# `[]' not actually needed for empty one
    >>> print(a)
    set()
    
    >>> print(type(a))
    <class 'set'>
    
    >>> b = set([1, 2, 3, 4])
    >>>print(b)   
    {1, 2, 3, 4}

* Cool. But you said something about *uniqueness* and *orderdness*

    >>> c = set([3, 4, 2, 2, 1, 5, 5, 5, 5])
    >>> print(c)
    {1, 2, 3, 4, 5}
   
* Hmmm... Looks ordered to me
    * Not really though, there is no actual intrinsic ordering enforced here
* We can totally see the uniqueness though, so that's cool

* ``in`` totally works

    >>> print(3 in c)
    True
    
    >>> print('a' in c)
    False
   
* Iterating over a set

    >>> for thing in c:
    >>>   print(thing)
    1
    2
    3
    4
    5
   
* Add things to a set

    >>> c.add('hello')
    >>> print(c)
    {1, 2, 3, 4, 5, 'hello'}
    
    >>> c.add('hello')
    >>> print(c)
    {1, 2, 3, 4, 5, 'hello'}
   
* *discard* things
 
    >>> c.discard('hello')
    >>> print(c)
    {1, 2, 3, 4, 5}
    
    >>> c.discard('hello')
    >>> print(c)
    {1, 2, 3, 4, 5}
   
* *remove* things
    * Almost the same as discard, but will throw an *exception* if we try to remove something that's not there
   
    >>> print(c)
    {1, 2, 3, 4, 5}
    
    >>> c.remove(5)
    >>> print(c)
    {1, 2, 3, 4}
   
    >>> c.remove(5)
    KeyError              Traceback (most recent call last)
    <ipython-input-91-0733df1dbd33> in <module>()
    ----> 1 c.remove(5)
    KeyError: 5

* Clearing out a set

    >>> c.clear()
    >>> print(c)
    set()

* Check equality

    >>> c = set([1, 2, 3])
    >>> d = set([3, 2, 1])
    >>> print(c == d)
    True
   
What makes them special other than just uniqueness and orderdness?
------------------------------------------------------------------

* So far they might not seem that special when compared to lists
* But they are very very very special in many ways
* One of which is: ``in``. 
* Remember how when we used ``in`` for a list, but at the end of the day, the computer still have to do a linear search
    * Remember what a liner search is?
* Turns out, for a set, ``in`` can tell us if something is in the set **without** having to do a linear search!


.. admonition:: Activity
    :class: activity

    Load up this code into Python:
   
    .. code-block:: python
   
        set_a = set([0, 1])
        set_b = set([0, 1, 2])
        set_c = set([2, 3])

    * Figure out if there is an easy way to determine if set ``set_a`` ``isubset`` of ``set_b``
    * Figure out if thre is an easy way to get the ``union`` of two sets
    * Figure out if there is an easy way to get the ``intersection`` of two sets
    * Figure out if there is an easy way to get the ``difference`` between ``set_b`` and ``set_a`` 
    * Do the previous one again but try the ``difference`` between ``set_a`` and ``set_b``
   
    **HINT:** hit tab.

.. image:: sets.png
   
  
.. admonition:: Activity
    :class: activity

    1. Imagine I gave you the text from a book that you could load up into Python. What's the easiest way to count the number of unique words?
   
    2. What would you do if I gave you another book and asked you which words do they have in common?
   
    3. What if I wanted to know the number of unique words that exist between the two books?
   
    4. What If I wanted to know which words were in one book, but not the other?


The Bad News...
===============

* The above data structures are pretty awesome
* Unfortunately... they're not *free*
    * Although Python really makes it look like they are
* With dictionaries, sets, tuples, and even lists, someone actually had to write a lot of nifty algorithms to do all the amazing things they do
* I briefly discussed fixed length arrays before, and those, classically speaking, we get for free, in addition to the *primitive types*
* Most of the cool data structures we've seen so far are actually built on top of the fixed length arrays
* In the same way that we're not actually sure how ``print`` actually works, we don't know how these data structures really work under the hood. 


The Good News...
================

* This does not really matter for us right now. 
* As of now, we don't really need to know all this to get the computer to do fun things. 
* Just like how you don't really need to know all the ins and outs of an internal combustion engine in order to drive a car, we don't need to know all the ins and outs of the data structures to use them. 
* Buuuuutttttttttttt... at the same time, if I was a race car driver, maybe knowing how things work under the hood could help me tweak and tune the car for the best performance. 

The Good/Bad News...
====================

* The under the hood stuff here is outside the scope of this course. 
* If you're thinking **Thank F@-%!#& GAWD**, lucky you
* If you're thinking *awhhhhhhhhhhhhhhhh, I wanna' know*, sorry

* Either way, we will look at *some* of these data structures in CSCI 162!
    * Trust me, it's actually a lot of fun!!




 
   
For next class
==============
* `Get PyCharm installed! <https://www.jetbrains.com/pycharm/download>`_

* Read `appendix A of the text <http://openbookproject.net/thinkcs/python/english3e/app_a.html>`_   
