**********
References
**********

* It is important for us to have an idea of what exactly is stored in our variables

.. warning::

    The ideas below are presented at a high level and are a simplification of how Python actually works. The
    simplification is sufficient for what we need to understand, and the details that differ are not important at
    this stage.


* Here is an idealized view of memory inside a computer

.. image:: ram_overview.png


Primitive Types in Memory
=========================

* Let's say we have a single integer called ``x``
* An integer is a primitive type
* In many programming languages integers take up **32 bits** worth of memory

    * That means 32 ``0``\s and ``1``\s
    * E.g. ``00101010010010110101110100010100``, which is the number ``709582100``

* Since we know how much memory an integer takes up, we can easily put integers into nicely divvied up chunks of memory

* If we divided memory into blocks of 32 bits
* And we create an integer variable ``x = 17``
* Something like this will happen

    * The value ``17`` gets assigned to one of the 32 bit sections of memory
    * A label ``x`` is created for that location

.. image:: int_in_memory.png

* If we wanted to copy the value of ``x`` into another variable, I could write something like ``y = x``
* When this happens

    * Copy the contents from the location with the label ``x``
    * Place the copied value into another 32 bit section of memory
    * Create a label ``y`` for the copied value's location

* **The contents of** ``x`` **are copied to** ``y``

.. image:: copied_int_in_memory.png

* This strategy works great for types that have a nicely defined sizes
* But what happens when we do not know beforehand how much memory something needs in order to store it?


Lists in Memory
===============

.. image:: list_elements_overview.png

* Above is a list with length ``8``
* The contents are labeled ``a`` -- ``h``, but these are arbitrary labels and we can think of them as integers

* In the examples so far, memory was divided into chunks of 32 bits which is perfect for integers
* Unfortunately, we need to store a whole list that contains 8 integers

    * This needs 256 bits

* Fortunately we have a solution
* Store each of the elements within the list in their own memory location

    * Similar to how the integer ``17`` was stored above

* Section off a large block of memory for the list to hold *references* to each of the elements of the list
* For example, the following image shows how we can think of storing the list ``[a, b, c, d, e, f, g, h]``

.. image:: list_contents_in_memory.png

* Just put each integer into its own memory location
* Keep track of the fact that our list starts at memory address 677 and goes to 684
* The trick is in how this is managed


References
----------

.. code-block:: python
    :linenos:

    z = [a, b, c, d, e, f, g, h]


* Given the above list creation, the computer finds a contiguous block of memory to store the contents of the list

    * Each element in the list fits nicely into the divvied up sections

* Then, the information needed to find and access the list contents is stored in a piece of memory labelled with the variable ``z``

    * The list is **not** stored in ``z``\; the *location* of the list in memory is stored in ``z``

.. image:: list_reference_in_memory.png


.. admonition:: Activity
    :class: activity

    Take a moment to look at this image and see if you can explain why we start counting at 0 when indexing lists.


* If we wanted to make a copy of ``z`` like we did with the integers ``x`` and ``y``\, we could write something like ``w = z``
* And just like with the integers, this copies the contents of the memory location of ``z`` and puts it into a new location labelled with a ``w``
* However, the catch is that the contents of ``z`` is the memory address of the list
* After making the copy into ``w``, how many references are there to the memory location of the list?

.. image:: copied_list_reference_in_memory.png

* If I want to make a change to ``w`` and I write something like ``w[4] = P``, the computer goes to the list referenced by ``w`` and alters the value at index ``4``

.. image:: aliased_list_after_update.png

* This does not alter the contents of the memory location of ``w``\; this alters the data at the memory location referenced by ``w``
* In fact, this also alters the data at the memory location referenced by ``z``

    * What would happen if I wrote ``print(z[4])``\?

* When we have two or more references referring to the same *thing* in memory, we call these aliases

    * ``w`` is an alias for ``z``
    * This is discussed further in the following topic


.. note::

    In reality, Python stores each list element in its own memory location and the list holds references to them.

    .. image:: multiple_list_references.png


For Next Topic
==============

* Read `Chapter 14 of the text <https://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
* Read `Chapter 15 of the text (only lightly though) <https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_

