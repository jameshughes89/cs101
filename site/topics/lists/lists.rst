*****
Lists
*****

* We saw that strings were a little different when compared to the other types we've seen (``int``, ``float``, ``bool``)
* We can generalize the idea of strings to more types

    * A string is a collection of characters
    * We can use lists to have a collection of other types


.. admonition:: Activity
    :class: activity

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

* The ``list`` is your first real **data structure**
* As the name suggests, a data structure is some *structure* that holds *data*
* Lists, although simple, are exceptionally useful and important

  .. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/EcuTE0VEDl8" frameborder="0" allowfullscreen></iframe>


.. admonition:: Activity
    :class: activity

    Apply what you know about loops, strings, and lists to solve the following problems --- combining algorithms and
    data structures is a big part of programming. **Hint:** You will probably find the linear searches from the strings
    topic to be helpful.
   
    #. Write a function ``contains_while(needle, haystack) -> bool:`` that uses a ``while`` loop and returns ``True`` if needle is contained in the haystack and ``False`` otherwise.
    #. Write a function ``index_of_for(needle, haystack) -> int:`` that uses a ``for`` loop and returns the index of needle within the haystack or ``-1`` if it is not found.
    #. Write some ``assert`` tests for both functions to verify correctness.


List Operators and Methods
==========================

* Similar to strings, we can concatenate lists with the ``+`` operator

    .. code-block:: python
        :linenos:

        some_list = [5, 6, 7, 8, 9]
        some_other_list = ["this", "is", "a", "list"]
        bigger_list = some_list + some_other_list
        print(bigger_list)
        # Results in [5, 6, 7, 8, 9, 'this', 'is', 'a', 'list']


* We can concatenate a list with itself multiple times using the ``*`` operator

    .. code-block:: python
        :linenos:

        some_list = [5, 6, 7, 8, 9]
        triple_list = some_list * 3
        print(triple_list)
        # Results in [5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9]


.. admonition:: Activity
    :class: activity

    #. Create some list and assign it to a variable ``some_list``
    #. ``print`` out the list --- ``print(some_list)``
    #. After running the code, type ``some_list.`` and wait

        * Don't forget the dot ``.``

    #. Play around with some of the methods you see


Mutability 
==========

* Although lists and strings have some things in common, one thing they do not have in common is *mutability*

    * Remember, strings are *immutable*

* We can index strings and lists the same way to access individual elements
* But unlike strings, we can also change the elements at a specific index

.. code-block:: python
    :linenos:

    another_list = ["a", "b", "c", "d", "e"]
    another_list[2] = "X"
    print(another_list)
    # Results in ['a', 'b', 'X', 'd', 'e']


Lists & Loops
=============

* Similar to how ``for`` loops made it easy to iterate over each character in a string
* ``for`` loops can be used the same way on lists to iterate over each element in the list

    * ``for`` each *thing* in a collection of *things*

.. code-block:: python
    :linenos:

    collection_of_things = ["Hello", 10, True, 100.001]

    for thing in collection_of_things:
      print(thing)

    # Results in
    #   Hello
    #   10
    #   True
    #   100.001


* Iterating over a *collection of things* is very common
* Expect to start using ``for`` loops like this a lot
* In fact, this was used in assignment 1 multiple times

    * Iterating over the contents of the file being read
    * Iterating over the list of ``(latitude, longitude)`` pairs


Range
-----

* ``range`` is a very handy function that we often use with ``for`` loops
* It provides an easy way to loop over a specific range of numbers

.. code-block:: python
    :linenos:

    for i in range(5):
      print(i)

    # Results in
    #   0
    #   1
    #   2
    #   3
    #   4


* Notice that the integer ``5`` was specified in the ``range`` function, and the loop ran a total of ``5`` times

    * But because of ``0`` based indexing, the the number ``5`` is not actually included

* A big reason we like to use ``for`` loops this way is because the syntax is so simple and clean
* The above functionality can be achieved with a ``while`` loop, but the code needed is a little more cumbersome

.. code-block:: python
    :linenos:

    i = 0
    while i < 5:
      print(i)
      i += 1

    # Results in
    #   0
    #   1
    #   2
    #   3
    #   4


.. admonition:: Activity
    :class: activity

    Write a function ``beer_on_wall`` that prints out ``"n bottles of beer on the wall"`` for all ``n`` from ``99`` down
    to ``0``. This function must use a ``for`` loop with the ``range`` function.

    The difficulty here is the need to count backwards.

    `Perhaps a read of the documentation can help. <https://docs.python.org/3/library/stdtypes.html#typesseq-range>`_

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/0AuMKIMiPMo" frameborder="0" allowfullscreen></iframe>


Looping Over Indices and Enumerate
----------------------------------

* Sometimes it is important to know the indices of each element being printed out
* For example, if the goal is to do a linear search to find the index of a given element, the following would be problematic

.. code-block:: python
    :linenos:

    def index_of_uhoh(needle, haystack):
        for element in haystack:
            if element == needle:
                return ???? # How do I find the index?
        return -1


* Using the ``range`` function would help in this situation as we can use it to loop over each index in ``haystack``
* The only catch is that we need to actually index ``haystack``

.. code-block:: python
    :linenos:

    def index_of(needle, haystack):
        haystack_length = len(haystack)
        for i in range(haystack_length):
            if haystack[i] == needle:
                return i
        return -1


* To make what is going on a little clearer, consider the following example

.. code-block:: python
    :linenos:

    another_list = ["a", "b", "c", "d", "e"]
    for i in range(len(another_list)):
        print(i, another_list[i])

    # Results in
    #   0 a
    #   1 b
    #   2 c
    #   3 d
    #   4 e


* This loop prints out the index (``i``) along with the element at the given index (``another_list[i]``)
* This functionality is quite common and Python even provides a shorthand for achieving it --- ``enumerate``

.. code-block:: python
    :linenos:

    another_list = ["a", "b", "c", "d", "e"]
    for i, element in enumerate(another_list):
        print(i, element)

    # Results in
    #   0 a
    #   1 b
    #   2 c
    #   3 d
    #   4 e


* Here there is no need to actually index the list since the ``element`` variable already has the value ``another_list[i]``


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
    :class: activity

    Create a list named ``l``. Make an *alias* of the list named ``lalias``. Make a *copy* of the list named ``lcopy``. Prove to yourself that one is an alias and one is a copy.


Mind the rotating knives
========================

* Remember how assigning lists wasn't really *copying* them, but just creating a new name?
* I wonder what happens when you pass a list to a function as an argument?
    * Does the function get it's own copy?
    * ... or does the function just get an alias to the same list?
   
.. admonition:: Activity
    :class: activity

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
    :class: activity

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
    :class: activity

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


