******************
Sorting Algorithms
******************

.. Warning::

    At this stage of the course we are starting to see nontrivial algorithms. Although you may have been able to quickly
    understand the previous algorithms, going forward you should not expect to observe an algorithm and immediately
    understand how it works.

    Although you are all equipped with the requisite skills to understand these algorithms, they require *careful study*
    to understand. The best strategy for approaching these algorithms is to carefully trace through their operation,
    step by step, making no assumptions of the code.


* Similar to searching, sorting is a problem you are all familiar with
* Unlike searching, we have not investigated any sorting algorithms
* Believe it or not, there are many ways one could sort a list

    * Some are better than others
    * Some are better than others under certain conditions
    * Some are just plain terrible

.. admonition:: Activity
    :class: activity

    #. Have you ever sorted things in your life?
    #. Take a moment to talk amongst yourselves about *how* you you sorted things.

        * What was the step-by-step *algorithm*?

    You can keep your discussion high-level, but try to explain it such that the person you are explaining it to could
    follow your instructions to sort things.





.. Warning::

    Each of the following algorithms have many implementations. What makes the algorithm the algorithm is the *high-level* idea, not the actual, literal implementations.
   
Insertion sort
==============

	.. image:: insertion.gif

* You give me a list called ``in_list``
* I create a new, empty, list called ``sorted_list``
* For each element in ``in_list``
    * I *insert* that element into ``sorted_list`` in the correct spot.
    * e.g., if I'm asked to insert ``5`` into the list ``[1,3,7]``, I should end up with: ``[1,3,5,7]``

.. admonition:: Activity
    :class: activity

    Do an insertion sort, with pencil and paper, on the list ``[3,7,15,9,4,11,1,5,2]``. Record the value of ``sorted_list`` at each step.   
   
Let's have a look at an insertion sort implementation in Python::

    def insertion_sort(in_list):
        sorted_list = []
        for element in in_list:
            i = 0
            while i < len(sorted_list) and (element > sorted_list[i]):
                i = i + 1
            sorted_list.insert(i, element)
        return sorted_list

.. admonition:: Activity
    :class: activity

    Modify the ``insertion_sort()`` function above so that it prints out the value of ``sorted_list`` after each iteration of the `for` loop. Try sorting a few lists and following the output. Does it make sense to you?

* Now that we've got the idea down, let's be computer science nerds about it.

.. admonition:: Activity
    :class: activity

    * How many times do I go around the `for` loop in ``insertion_sort()`` ? On each trip through the `for` loop, I also have to go through the inner `while` loop.
        * How many times do I go through the `while` loop, on average?
        * In the worst case?
	  
    * Is Insertion sort the best possible sort? Can we do better?

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/ofZ5ygghj9g" frameborder="0" allowfullscreen></iframe>
	
Selection Sort
==============

	.. image:: selection.gif

* You give me a list called ``in_list``
* I scan through the whole list to find the smallest element
* I swap the smallest element with the first element in the list
* I repeat the above process for the remainder of the list (excluding the first element)
* Lather, rinse, repeat.

.. admonition:: Activity
    :class: activity

    Do a selection sort, with pencil and paper, on the list ``[3,7,15,9,4,11,1,5,2]``. Record the value of your list at each step.  

* Different idea than Insertion sort, but still gets the job done!
* This is a very important thing to understand:
    * *Sorting* is a *problem*, not an algorithm
    * There are (infinitely) *many* algorithms to solve any (solvable) problem
    * Some algorithms will always solve the problem more efficiently than others
    * Some will solve the problem more efficiently only for certain conditions
    * For some problems we can *prove* that a particular algorithm is the best (in the sense that any other algorithm can, at best, be equally efficient)
    * For many problems, we *still don't know* how to do this!
   
* Fortunately, for sorting we *do* know how to do this analysis... and both Insertion Sort and Selection Sort suck.
 
Let's see Selection sort in action::

    def selection_sort(in_list):
        for i in range(len(in_list)):
      
            # Find the smallest remaining element
            min_index = i
            min_val = in_list[i]
            for j in range(i+1,len(in_list)):
                if in_list[j] < min_val:
                    min_val = in_list[j]
                    min_index = j
                   
            # Swap it to the left side of the list
            in_list[min_index] = in_list[i]
            in_list[i] = min_val
         
        return in_list
    
.. admonition:: Activity
    :class: activity

    Modify the ``selection_sort()`` function above so that it prints out the value of ``in_list`` after each iteration of the outer `for` loop. Try sorting a few lists and following the output. 

.. admonition:: Activity
    :class: activity

    How many times do I go around the outer `for` loop in ``selection_sort()`` ? How about the inner `for` loop?
   
.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/ADD6jsSS9HI" frameborder="0" allowfullscreen></iframe> 

Bubble Sort
===========

	.. image:: bubble.gif

* Maybe you find Insertion sort or Selection sort ugly or offensive?
* No problem. Remember: there are *many* algorithms to solve any one problem.
* You give me a list called ``in_list``
* I scan through the list, looking at adjacent pairs of values.
* If I see a pair that is "out of order" (e.g., ``[17, 9]`` ), I swap the two values to be in order ( ``[9,17]`` ).
* I keep doing that until the list is sorted.

.. admonition:: Activity
    :class: activity

    Do a bubble sort, with pencil and paper, on the list ``[3,7,15,9,4,11,1,5,2]``. Record the value of your list at each step.  

* It's called "bubble sort" because the smaller values seem to "bubble up to the top".
* Kinda cool because:
    * We end up effecting a *global* change on the list (it goes from unsorted to sorted)...
    * ... but we only use *local* information about the elements (we only ever compare neighbours in the list)
   
Let's see Bubble sort in Python::

    def bubble_sort(in_list):
        swapped_something = True
        while swapped_something:
            swapped_something = False
         
            for i in range(len(in_list)-1):
                if in_list[i] > in_list[i+1]:
                    tmp = in_list[i]
                    in_list[i]=in_list[i+1]
                    in_list[i+1]=tmp
                    swapped_something = True
        return in_list

* Ugh... Wouldn't the above code be better if there were comments?

.. admonition:: Activity
    :class: activity

    Modify the ``bubble_sort()`` function above so that it prints out the value of ``in_list`` after each iteration of the outer `while` loop. Try sorting a few lists and following the output.   
   
.. admonition:: Activity
    :class: activity

    How many times do I go around the outer `while` loop ? How
    about the inner `for` loop?

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/NfmAFOlM5Jw" frameborder="0" allowfullscreen></iframe>
	
	
Bogosort
========

Here's another attempt at a sorting algorithm::

    import random
   
    def is_sorted(in_list):
        last = in_list[0]
        for element in in_list[1:]:
            if last > element:
                return False
            last = element
        return True
     
     
    def bogo_sort(in_list):
        while not is_sorted(in_list):
            random.shuffle(in_list)

        return in_list

.. admonition:: Activity
    :class: activity

    How does this sorting algorithm work? We're "working backwards" this time. Starting from the code, come up with an English explanation for how the algorithm works. You might want to add a ``print`` statement after the ``random.shuffle(in_list)`` line to get some intuition. If you aren't sure what ``random.shuffle()`` does... look it up, or just *try* it on some sample lists. Likewise, you'll have to figure out what ``is_sorted()`` is doing (though the name should help). 
   
.. admonition:: Activity
    :class: activity
   
    Is this a good sorting algorithm? How many times do I have to go through the ``while`` loop in ``bogo_sort``? How about the ``for`` loop in ``is_sorted()``?

WTF!?
=====

* Searching a list is *way* faster when we have a sorted list. 
* Why would someone want to sort a list in order to search it slightly faster when sorting is so slow?
* Well, we might want to search the same list many times.
    * We only need to sort it once.
* We might want to sort something without the end goal of searching.
* BUT, also, there are better sorting algorithms...

Why are we doing this again?
============================

* In your day-to-day life as a programmer, you won't write your own sorting routines. You'll rely on routines written by others, like Python's built-in ``sort()`` (which, by the way, uses the `Timsort algorithm <http://en.wikipedia.org/wiki/Timsort>`_ )
* BUT... even if you don't build the tools yourself, you should understand how they work
* More importantly: you **WILL** need to develop your own algorithms for some task that is much less well-studied than sorting.
* You're learning fundamentals of algorithm development here... not just the details of sorting.
* Let me say that again... **THE POINT OF THIS IS TO LEARN THE ALGORITHM FUNDAMENTALS**



The horrible truth
==================

* Insertion, Selection, and Bubble sort generally suck as sorting algorithms.
* BUT... they are within our current means.
* Once we've studied *recursion*, we will revisit sorting and see two *very good* sorting algorithms (Quicksort and Mergesort).
* If you want to geek out on sorting *right now*:
    * `The relevant Wikipedia page is very good <http://en.wikipedia.org/wiki/Sorting_algorithm>`_
    * Knuth's `The Art of Computer Programming Volume 3: Sorting and Searching <http://www.amazon.com/Art-Computer-Programming-Volume-Searching/dp/0201896850>`_ .
        * It would be nearly impossible to overstate the importance of Donald Knuth's contributions to Computer Science.

Let's see some sorting in action!
=================================

* http://www.sorting-algorithms.com/

   
For next class 
==============

* Read `chapter 18 of the text <http://openbookproject.net/thinkcs/python/english3e/recursion.html>`_  

