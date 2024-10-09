*********************
Loops & Linear Search
*********************

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

#. `Chapter 7 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/iteration.html#exercises>`_

    * 9 `What is a "triangle number"? <https://en.wikipedia.org/wiki/Triangular_number>`_ (no ``assert`` test for this)
    * 14 (use ``assert`` to test instead of their ``test`` function)
    * 15 (use ``assert`` to test instead of their ``test`` function) --- not required, but recommended


#. `Chapter 8 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/strings.html#exercises>`_

    * 3
    * 9 (use ``assert`` to test instead of their ``test`` function) --- not required, but recommended
    * 10 (use ``assert`` to test instead of their ``test`` function) --- not required, but recommended
    * 11 (use ``assert`` to test instead of their ``test`` function) --- not required, but recommended
    * 12 (use ``assert`` to test instead of their ``test`` function) --- not required, but recommended
    * 13 (use ``assert`` to test instead of their ``test`` function) --- not required, but recommended


#. Write assertion tests for each of your functions above, except for Chapter 7 exercise 9, as it requires ``print``



Before Kattis
=============

#. Write a function ``count_to_n_while(n: int):`` to print out each number from :math:`0` -- :math:`(n - 1)`

    * This function must use a ``while`` loop
    * This function will not return anything


#. Write a function ``count_to_n_for(n: int):`` to print out each number from :math:`0` -- :math:`(n - 1)`

    * This function must use a ``for`` loop
    * This function will not return anything


#. Write a function ``character_is_in_while(needle: str, haystack:str) -> bool:``

    * The function will ``return`` ``True`` if ``needle`` exists within ``haystack`` and ``False`` otherwise
    * This function must use a ``while`` loop


#. Write a function ``character_is_in_for(needle: str, haystack:str) -> bool:``

    * The function will ``return`` ``True`` if ``needle`` exists within ``haystack`` and ``False`` otherwise
    * This function must use a ``for`` loop


#. Write a function ``character_is_at_while(needle: str, haystack:str) -> int:``

    * The function will ``return`` the index of the first occurrence of ``needle`` within ``haystack`` and ``-1`` if it is not found
    * This function must use a ``while`` loop


#. Write a function ``character_is_at_for(needle: str, haystack:str) -> int:``

    * The function will ``return`` the index of the first occurrence of ``needle`` within ``haystack`` and ``-1`` if it is not found
    * This function must use a ``for`` loop



Kattis Problems
===============

* You should be using a scrap piece of paper to work out the ideas for the following problems

    * The problems you are to solve are getting too complex to try to solve by just coding
    * Trying to solve problems by just typing away will not yield success


#. https://open.kattis.com/problems/timeloop
#. https://open.kattis.com/problems/oddities
#. https://open.kattis.com/problems/fizzbuzz
#. https://open.kattis.com/problems/sibice
#. https://open.kattis.com/problems/bus
#. https://open.kattis.com/problems/datum
#. https://open.kattis.com/problems/dicecup
