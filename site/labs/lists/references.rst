***********************
References & More Lists
***********************

* Feel free to use your laptop
* You are strongly encourage to work with others

    * When you get stuck, ask those sitting around you for help
    * Get used to working together in the labs
    * Peer teaching and peer learning has been empirically shown to be very effective



Pre Lab Exercises
=================

* For all exercises

    * Use ``assert`` to test instead of their ``test`` function


#. `Chapter 14 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html#exercises>`_

    * 2 --- note the portions of solutions within the chapter text


#. Write assertion tests for each of your functions above



Before Kattis
=============

#. Run the following code and figure out what what it does and how it does it

    * I want to see everyone with paper here working through the logic
    * If you can't figure it out, hack around with the code

        * Comment out bits
        * Print out values
        * Do whatever you need to do to figure it out


    .. code-block:: python
        :linenos:

        a = [0, 0, 0]
        b = [a,a,a]

        for row in b:
            toPrint = ''
            for d in row:
                toPrint += str(d) + ' '

            print(toPrint)


#. Add ``b[1][1] = 1`` to line 3 and run it again and see what happens

    * Is this what you expected?


#. Alter the code such that the output will be what's below.

    * Change the list setup/creation part, not the loops

    .. code-block:: python

        0 0 0
        0 1 0
        0 0 0


#. Add ``b[0][1] = 1`` to line 3 and run it again and see what happens

    * Is this what you expected?


#. Given a list of integers, return, in a list, indices of two numbers such that they add up to a specific target

    * You may assume that each input would have exactly one solution
    * You may not use the same element twice

    * For example, given ``nums = [2, 7, 11, 15]``, target = ``9``

        * Since ``nums[0]`` + ``nums[1]`` = ``2`` + ``7`` = ``9``
        * Return ``[0, 1]``


#. Think about how much work your algorithm for the previous question had to do in terms of :math:`n`, where :math:`n` is the length of the list

    * Can you somehow think of a better algorithm that would do less work?
    * Don't spend too much time on this if you can't come up with a solution
    * **Hint:** Dictionaries (but leave the ``nums`` list alone)
 


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
