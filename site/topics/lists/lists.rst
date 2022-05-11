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


For Next Class
==============
* Read `Chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
* Read `Chapter 15 of the text (only lightly though) <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_


