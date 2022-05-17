***********************
References & More Lists
***********************

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

    * Use ``assert`` to test instead of their ``test`` function

#. `Chapter 14 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html#exercises>`_

    * 2


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
    * **Hint:** Dictionaries
 

Kattis Problems
===============

These are the same problems from last week. They're good problems. Keep going. Start where you left off. 

Grab a scrap piece of paper to start scratching your ideas down on paper. The problems are getting tricky enough where this really is becoming a requirement. 

1. https://open.kattis.com/problems/bijele
2. https://open.kattis.com/problems/cold
3. https://open.kattis.com/problems/nastyhacks
4. https://open.kattis.com/problems/grassseed
5. https://open.kattis.com/problems/pet
6. https://open.kattis.com/problems/batterup
7. https://open.kattis.com/problems/aboveaverage
8. https://open.kattis.com/problems/icpcawards
9. https://open.kattis.com/problems/quickbrownfox
10. https://open.kattis.com/problems/nodup
11. https://open.kattis.com/problems/conundrum
12. https://open.kattis.com/problems/bela
13. https://open.kattis.com/problems/kornislav


LeetCode Problems
=================

If you have somehow finished everything so far, go check out `LeetCode <https://leetcode.com/problemset/all/>`_. Sort the problems by *Acceptance* (click the table header) and start seeing if you can solve some of these problems. 

**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
