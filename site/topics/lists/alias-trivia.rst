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


List Trivia
===========

* We can find the length of a list

.. code-block:: python
    :linenos:

    some_list = [10, 11, 12]
    print(len(some_list))       # Results in 3


* We can have empty lists

.. code-block:: python
    :linenos:

    empty_list = []
    print(empty_list)           # Results in []
    print(type(empty_list))     # Results in <class 'list'>
    print(len(empty_list))      # Results in 0


* We can have lists of lists

.. code-block:: python
    :linenos:

    some_nested_lists = [[0, 1, 2], ['a', 'b', 'c']]
    print(some_nested_lists[1])     # Results in ['a', 'b', 'c']
    print(some_nested_lists[1][0])  # Results in 'a'


* We can append to a list

.. code-block:: python
    :linenos:

    some_list = [10, 11, 12]
    some_list.append(99)
    print(some_list)       # Results in [10, 11, 12, 99]


* We can concatenate lists with ``+`` to create a new list

    * The original lists are left unchanged

.. code-block:: python
    :linenos:

    list_a = [0, 1, 2]
    list_b = ['a', 'b', 'c']
    list_c = list_a + list_b
    print(list_a)               # Results in [0, 1, 2]
    print(list_b)               # Results in ['a', 'b', 'c']
    print(list_c)               # Results in [0, 1, 2, 'a', 'b', 'c']


* We can repeat a list with ``*``

.. code-block:: python
    :linenos:

    some_list = [10, 11, 12]
    print(some_list * 3)       # Results in [10, 11, 12, 10, 11, 12, 10, 11, 12]


.. admonition:: Activity
    :class: activity

    Python has some built in functions that we can use on lists:

        * ``min``
        * ``max``
        * ``sum``

    However, just because Python provides these functions, someone still had to write these functions.

    #. Without using the built in ``sum``, write your own function ``my_sum`` to add up the contents of a list.
    #. How different do you think your algorithm is compared to the one Python gave you?
    #. If you had a list of length :math:`10`, how many things does your function need to add together?
    #. What if your list was length :math:`10,000`?

	  	  
For Next Class
==============
* Read `Chapter 9 of the text <http://openbookproject.net/thinkcs/python/english3e/tuples.html>`_
* Read `Chapter 20 of the text <http://openbookproject.net/thinkcs/python/english3e/dictionaries.html>`_

