*********************
Aliases & List Trivia
*********************

.. _label-topic8-aliasing:

* The following code should be simple to understand at this stage

.. code-block:: python
    :linenos:

    a = 5
    b = a
    print(a, b)     # Results in 5 5

    b = 7
    print(a, b)     # Results in 5 7 --- a is left unchanged



* And similarly, the below example should not surprise you

.. code-block:: python
    :linenos:

    a = [0, 1, 2]
    b = a           # b is an "alias" for a
    print(a, b)     # Results in [0, 1, 2] [0, 1, 2]

    b = [5, 6, 7]
    print(a, b)     # Results in [0, 1, 2] [5, 6, 7] --- a is left unchanged



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




Nested lists
============

* If you can nest loops... can you nest lists?

.. admonition:: Activity
    :class: activity

    Figure out if Python supports nested lists. If it does: build a few. If it doesn't: how might you implement them yourself?
 
.. admonition:: Activity
    :class: activity

    Hack around with Python to find answers to these questions:
        1. Can you have a list in a list?
        2. What about a list in a list in a list?
        3. How about a list in a list in a list in a list in a list in a list?
        4. Are there *methods* for the lists?

List Trivia
===========
let's assume we have ``a = [1,4,6,2,4,6]``

* An empty list is a list!!!!

>>> b = []
>>> print(b)
[]

>>> print(type(b))
<class 'list'>

>>> print(len(b))
0

* Like strings, we can use ``in``

>>> print(4 in a)
True

>>> print('x' in a)
False

* We can get the length of a list with ``len(the_list)``

>>> print(len(a))
6

* We can print out a whole list with ``print(the_list)``

>>> print(a)
[1, 4, 6, 2, 4, 6]

* We can concatenate a list with ``+``
    * but ``a`` is unchanged here; we create a new list

>>> print(a + [9, 9, 9, 9, 9])
[1, 4, 6, 2, 4, 6, 9, 9, 9, 9, 9]

* We can ``append``
    * but ``c`` is changed here

>>> c = [1]
>>> c.append(4)
>>> print(c)
[1, 4]

>>> c.append([9,9,9,9,9])
>>> print(c)
[1, 4, [9, 9, 9, 9, 9]]

* We can multiply the list

>>> print(a*3)
[1, 4, 6, 2, 4, 6, 1, 4, 6, 2, 4, 6, 1, 4, 6, 2, 4, 6]

* We can check equality

>>> print([1,2,3] == [1,2,3])
True

>>> print([1,2,3] == [3,2,1])
False

* We can find the ``max`` of the list

>>> print(max(a))
6


* We can find the ``min`` of a list

>>> print(min(a))
1

* We can ``sum`` up the contents

>>> print(sum(a))
23

* We can sort the list

>>> a.sort()
>>> print(a)	# WARNIG, WE CHANGED a NOW!
[1, 2, 4, 4, 6, 6]


**REMEMBER, IF YOU DON'T REMEMBER WHAT YOU CAN/CAN'T DO WITH THEM, JUST TRY TO DO THINGS WITH THEM!** If it works, cool, if not, whatever, no harm done. 


.. admonition:: Activity
    :class: activity

    Let's take a step back for a sec and think about the algorithms for a sec. 
   
    1. If I asked you to tell me the ``sum`` of the contents of the list, what would you do?
    2. Did you have to write that function?
    3. Do you think Python magically *knew* what the sum was?
    4. How do you think Python got you the answer?
    5. Do you have enough tools in your tool-belt to write this function?
    6. Write a function called ``my_sum`` that will sum up the contents of the list, but you're not allowed to use the internal ``sum`` function. 
   
.. admonition:: Activity
    :class: activity

    How long does it take for ``my_sum`` to run? 
   
    Hint: how long would it take if the list had a length 10 versus 10,000?
   
   

	  
	  	  
For next class
==============
* Read `chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
* Read `chapter 15 of the text (only lightly though) <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_
* Read `chapter 9 of the text <http://openbookproject.net/thinkcs/python/english3e/tuples.html>`_
* Read `chapter 20 of the text <http://openbookproject.net/thinkcs/python/english3e/dictionaries.html>`_

