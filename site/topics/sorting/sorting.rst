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

.. note::

    Each of the following algorithms have many possible implementations. What makes the algorithm the *algorithm* is the
    high-level idea, not the actual, literal implementations. This idea will be emphasized as we discuss the individual
    sorting algorithms below.


Selection Sort
==============

.. image:: selection_sort.gif
   :height: 333 px
   :align: center
   :target: https://en.wikipedia.org/wiki/Selection_sort


* Selection sort is fairly accessible, and chances are you have sorted things in real life using this algorithm
* Selection sort works by repeatedly selecting the smallest element from the collection
* The high-level algorithm is as follows

    * Start with the unsorted list and an empty list for the sorted elements
    * For each element in the collection

        * Perform a linear search on the unsorted list for the current smallest element
        * Remove the current smallest element from the unsorted list and append it to the sorted list


* To reason about how and it works, consider

    * The first time the linear search finds the smallest element, that element must be the first element in the sorted collection
    * Every other subsequent linear search finds the remaining smallest element and appends it to the sorted collection

        * It cannot come *before* anything in the sorted collection since we know it must be greater than (or equal to) all elements in the sorted collection


.. admonition:: Activity
    :class: activity

    Perform a insertion sort, with pencil and paper, on the list ``[3,7,4,1,5,2]``. Keep track of both the unsorted list
    and sorted list at each step of the algorithm.


* Now that we know a little bit about how to analyze algorithms, let's figure out how much work this algorithm needs in order to solve the problem

    * Selection sort requires a linear search to find the current smallest element in the collection

        * We know that linear search takes :math:`n` amount of work for a list of size :math:`n`

    * But, selection sort needs to perform a linear search for each element in the collection

        * If our unsorted list is of size :math:`n`, that means the linear search must be run :math:`n` times

    * If we put it together, we need to run linear search, which takes :math:`n` amount of work, a total of :math:`n` times

        * We need to do :math:`n` work :math:`n` times
        * This would be a total of :math:`n^{2}` work for an unsorted list of size :math:`n`


.. code-block:: python
    :linenos:

    def selection_sort(collection):
        sorted_collection = []
        for _ in range(len(collection)):
            current_smallest = collection[0]
            for element in collection:
                if element < current_smallest:
                    current_smallest = element
            collection.remove(current_smallest)
            sorted_collection.append(current_smallest)
        return sorted_collection


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/ADD6jsSS9HI" frameborder="0" allowfullscreen></iframe>


Insertion Sort
==============

.. image:: insertion_sort.gif
   :height: 333 px
   :align: center
   :target: https://en.wikipedia.org/wiki/Insertion_sort


* Insertion sort works by repeatedly inserting elements into their proper location within a collection
* The high-level algorithm is as follows

    * Start with the unsorted list and an empty list for the sorted elements
    * For each element in the collection

        * Remove the element from the unsorted list
        * Perform a linear search on the sorted list to find the index where the new element should be inserted
        * Insert the new element into the sorted list at the index where it belongs


* To reason about how and it works, consider

    * Elements are inserted into their proper relative location to the elements already within the sorted collection
    * Any subsequent insertion cannot disrupt the ordering of the whole list if it is being inserted in its proper location

        * For example, consider the list `[1, 4, 7, 9]`
        * If we need to insert the number `6`, it obviously goes between the `4` and `7` since ``4 < 6 < 7`` --- `[1, 4, 6, 7, 9]`
        * The order of the elements ``1`` and ``4`` remain unchanged, and similarly with ``7`` and ``9``



.. admonition:: Activity
    :class: activity

    Perform a selection sort, with pencil and paper, on the list ``[3,7,4,1,5,2]``. Keep track of both the unsorted list
    and sorted list at each step of the algorithm.


* The analysis of the algorithm is very similar to that of selection sort

    * We need to perform a linear search for each of the :math:`n` elements in the unsorted list
    * We know linear search takes :math:`n` amount of work for a list of size :math:`n`
    * Therefore, we need to do :math:`n` work :math:`n` times --- a total of :math:`n^{2}` work for an unsorted list of size :math:`n`


.. code-block:: python
    :linenos:

    def insertion_sort(collection):
        sorted_collection = []
        for element in collection:
            i = 0
            # Scan sorted collection to find insertion spot
            while i < len(sorted_collection) and sorted_collection[i] < element:
                i += 1
            sorted_collection.insert(i, element)
        return sorted_collection


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/ofZ5ygghj9g" frameborder="0" allowfullscreen></iframe>


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

