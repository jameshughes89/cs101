*****
Lists
*****

* Feel free to use your laptop if you have it
* Ensure I have recorded your completion --- failure to do so will result in a grade of 0
* I strongly encourage you to work with others in the lab

    * When you get stuck, do me a favour and ask those sitting around you for help
    * I want people to get used to working together in the labs
    * Peer teaching and peer learning is super effective

.. note::

    To obtain full marks for the lab, you must:

        #. Have completed the pre-lab exercises
        #. Have been working on the lab content
        #. Demonstrate competency in the topics


Pre Lab Exercises
=================

.. warning::

    You must have completed the specified exercises prior to the start of the lab. If you have not come to lab prepared,
    you will be asked to leave and you will obtain a grade of 0 for the lab.


* For all exercises

    * Do **not** make a ``vector.py`` file, just use Colab like you have been
    * Use ``assert`` to test instead of their ``test`` function

#. `Chapter 11 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/lists.html#exercises>`_

    * 5
    * 6

#. Write assertion tests for each of your functions above


Before Kattis
=============

#. Write a function ``linear_search(needle, haystack) -> bool:``

    * The function will ``return`` ``True`` if ``needle`` exists within the list ``haystack`` and ``False`` otherwise
    * This can use either a ``for`` loop or a ``while`` loop
    * Write ``assert`` tests to verify correctness

#. Write a function ``index_of(needle, haystack) -> int:``

    * The function will ``return`` the index of the first occurrence of ``needle`` within the list ``haystack`` and ``-1`` if it is not found
    * This can use either a ``for`` loop or a ``while`` loop
    * Write ``assert`` tests to verify correctness

#. Write a function ``replace_all(the_list, find, replace):``

    * This function will replace all occurrences of ``find`` within ``the_list`` and replace them with ``replace``
    * This function must ``return`` the modified list
    * For example, ``replace_all([1, 2, 2, 3], 2, 9)`` -> ``[1, 9, 9, 3]``
    * Write ``assert`` tests to verify correctness

#. Use the ``replace_all`` function to change the list ``[1, 2, 2, 1]`` -> ``[2, 1, 1, 2]``

    * You will need to use ``replace_all`` multiple times


Kattis Problems
===============

* You should be using a scrap piece of paper to work out the ideas for the following problems

    * The problems you are to solve are getting too complex to try to solve by just coding
    * Trying to solve problems by just typing away will not yield success

#. https://open.kattis.com/problems/bijele
#. https://open.kattis.com/problems/cold
#. https://open.kattis.com/problems/nastyhacks
#. https://open.kattis.com/problems/grassseed
#. https://open.kattis.com/problems/pet
#. https://open.kattis.com/problems/batterup
#. https://open.kattis.com/problems/aboveaverage
#. https://open.kattis.com/problems/icpcawards
#. https://open.kattis.com/problems/quickbrownfox
#. https://open.kattis.com/problems/nodup
#. https://open.kattis.com/problems/conundrum
#. https://open.kattis.com/problems/bela
#. https://open.kattis.com/problems/kornislav

.. warning::

    Ensure that your your completion has been recorded. Failure to do so may result in a grade of 0.
