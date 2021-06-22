Topic #8b -- List & Pointer Trivia
==================================


Nested lists
^^^^^^^^^^^^^

* If you can nest loops... can you nest lists?

.. admonition:: Activity

    Figure out if Python supports nested lists. If it does: build a few. If it doesn't: how might you implement them yourself?
 
.. admonition:: Activity

    Hack around with Python to find answers to these questions:
        1. Can you have a list in a list?
        2. What about a list in a list in a list?
        3. How about a list in a list in a list in a list in a list in a list?
        4. Are there *methods* for the lists?

List Trivia
^^^^^^^^^^^
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

    Let's take a step back for a sec and think about the algorithms for a sec. 
   
    1. If I asked you to tell me the ``sum`` of the contents of the list, what would you do?
    2. Did you have to write that function?
    3. Do you think Python magically *knew* what the sum was?
    4. How do you think Python got you the answer?
    5. Do you have enough tools in your tool-belt to write this function?
    6. Write a function called ``my_sum`` that will sum up the contents of the list, but you're not allowed to use the internal ``sum`` function. 
   
.. admonition:: Activity

    How long does it take for ``my_sum`` to run? 
   
    Hint: how long would it take if the list had a length 10 versus 10,000?
   
   

	  
	  	  
For next class
^^^^^^^^^^^^^^
* Read `chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_
* Read `chapter 15 of the text (only lightly though) <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_


