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

    b = [5, 6, 7]   # Change what b references
    print(a, b)     # Results in [0, 1, 2] [5, 6, 7] --- a is left unchanged


* **However**, the following may throw you off

.. code-block:: python
    :linenos:

    a = [0, 1, 2]
    b = a           # b is an "alias" for a
    print(a, b)     # Results in [0, 1, 2] [0, 1, 2]

    b[1] = 99       # Change index 1 of the list b references
    print(a, b)     # Results in [0, 99, 2] [0, 99, 2]


* Remember, ``a`` and ``b`` are both referencing **the same list**

    * They are aliases
    * There is only one list, but we have two references to that one list

* Regardless of the variable used to modify the single list, it's the list that is being altered
* If you expected the line ``b = a`` to make a full copy of the list referenced by ``a``, then this will seem strange
* But the line ``b = a`` does **not** make a copy of the list --- it makes a copy of the reference to the list

.. warning::

    This idea of references and aliases goes well beyond lists and will come up more as we progress through the course.
    It is something you will get used to with practice, but be aware that mixing up references is a very common error
    even experienced programmers run into.


* If you do actually want to make a copy of a list, there are a few ways to do it

    * Lists have a copy method that returns a copy ``new_list = some_list.copy()``
    * It is also possible to slice the list to produce a copy ``new_list = some_list[:]``

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/2F_qnTYA6g4" frameborder="0" allowfullscreen></iframe>


.. admonition:: Activity
    :class: activity

    #. Create a list ``l`` with arbitrary contents.
    #. Create an alias of ``l`` called ``l_alias``\.
    #. Create a copy of ``l`` called ``l_copy``\.

    Convince yourself that you did in fact make an alias with ``l_alias`` and a copy with ``l_copy``\,


Functions and Aliasing
======================

* When a list is given to a function, the parameter will get a reference to the list and not a copy of the list

    * The parameter within the function will be an alias

.. code-block:: python
    :linenos:

    def add_to_list(some_list, value):
        some_list.append(value)

    a_list = ['a', 'b', 'c']
    add_to_list(a_list, 99)
    print(a_list)   # Results in ['a', 'b', 'c', 99]


* In the above example, although never access through ``a_list``, the list ``a_list`` references is altered through the alias ``some_list`` within the function ``add_to_list``


Side Effects & Pure Functions
-----------------------------

* ``add_to_list`` is an example of a function that has a *side effect*

    * The function modified the list that was passed by reference
    * The term *side effect* comes from our mathematical expectation of a *function*

        * A function maps some parameters on to a value
        * If I give you the function :math:`f(x, y, z)= x + y - z` and ask you to evaluate :math:`f(1, 2, 3)`, you don't expect the values of :math:`x`, :math:`y`, and :math:`z` to change

* We can write a different version of the function that has no side effect

    * Functions without side effects are called *pure* functions

.. code-block:: python
    :linenos:

    def add_to_list_pure(some_list, value):
        new_list = some_list.copy()
        new_list.append(value)
        return new_list

    a_list = ['a', 'b', 'c']
    other_list = add_to_list_pure(a_list, 99)
    print(a_list)           # Results in ['a', 'b', 'c']
    print(other_list)       # Results in ['a', 'b', 'c', 99]


* In the new function ``add_to_list_pure``, the function makes a copy of the list passed by reference and made changes to the copy
* The new list was returned

    * In the end, the original list's data was left alone

* There are nice theoretical and practical benefits to keeping functions pure
* But that does not mean that non-pure functions are intrinsically bad

    * Sometimes it's just a lot easier to achieve something with side effects


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

