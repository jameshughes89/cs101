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

.. Warning::
   Before you do ANYTHING, take out a scrap piece of paper. If I do not see your paper at the end of the lab, you will get **0** on this lab. 


**1**

Run the below code and **figure out what exactly is going on**. I want to see everyone with paper here working through the logic. If you can't figure it out, hack around with the code. Comment out bits. Print out bits. Do whatever you need to do to figure it out. 

.. code-block:: python
    :linenos:
    
    a = [0, 0, 0]
    b = [a,a,a]

    for row in b:
        toPrint = ''
        for d in row:
            toPrint += str(d) + ' '
            
        print(toPrint)



**2**

Add ``b[1][1] = 1`` to line 3 and run it again. Is this what you wanted? (no, it's not). Fix this code such that the output will be what's below. **Hint:** Change the list setup part, not the loops.  


.. code-block:: python

    0 0 0 
    0 1 0 
    0 0 0

**2.5**

Change line 3 ``b[0][1] = 1`` and hit run. Did it do what you expected?


**3**

Given a list of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

EXAMPLE

Given ``nums = [2, 7, 11, 15]``, target = ``9``,

Because ``nums[0]`` + ``nums[1]`` = ``2`` + ``7`` = ``9``,

return ``[0, 1]``.



**4**

Think about how much work your algorithm for **3** had to do in terms of *n*, where *n* is the length of the list. Can you somehow think of a better algorithm that would do less work? Don't spend too much time on this if you can't come up with a solution. Just give yourself a fair chance. **Hint:** Dictionaries...  
 

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
