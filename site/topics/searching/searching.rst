*********
Searching
*********

* Before continuing, we should take a moment and reflect on what we have learned so far

    * The Python programming environment is a relatively familiar sight (Colab, IPython, PyCharm, Spyder)
    * You know how to ``print`` and ``input`` information
    * You know about types, values, and variables
    * You have been making use of functions
    * You have learned about basic logic and know how to use``if`` and ``else``
    * ``for`` and ``while`` loops are tools you have used
    * You learned how to use objects
    * Linear data structures, like a ``List``, are familiar and you are used to working with reference variables
    * You know how to read and write data from/to files
    * You have learned how to write classes and define your own objects
    * You can look at Python code and have a reasonable understanding of what it is doing
    * You know how to write your own code, one step at a time
    * You know the importance of testing your code and how to write tests

* The last few topics of the course have been heavy on data and data structures
* At this stage of the course, we have actually equipped ourselves with the majority of tools programmers use on a daily basis
* Here, we will start to focus more on algorithms and how we can use all the tools we have learned to solve more interesting problems
* Further, we will take some time to think about the amount of work the algorithm does and what makes an algorithm *good*


Searching (again)
=================

* I know I've beaten this into you at this point, but... *linear* search...

.. admonition:: Activity
    :class: activity

    Write a function ``find_element(element, list)`` that returns ``True`` if ``element`` is in ``list`` and ``False`` otherwise. 

    You may *not* use the ``in`` operator (that's cheating!)

* Nothing new here... you already know how to search an unordered list.

.. admonition:: Activity
    :class: activity
   
    Discuss this with your neighbours:
      
        * On average, how many iterations through your loop does your function make?
        * How about in the worst case?
        * Is your solution the best possible?
        * Might there exist some super clever algorithm that is somehow better (faster) than yours?   
	  
* These kinds of questions are getting you closer to computer *science* and further from straight "programming".	  

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/8unA_a5xcCU" frameborder="0" allowfullscreen></iframe>


Binary Search
=============

.. admonition:: Activity
    :class: activity

    I will guess a number between :math:`0 -- 1023` in :math:`10` or less guesses.

    There is a catch however --- you have to tell me if the number is *higher* or *lower* than my guess before I guess
    again.


* This is an example of a *binary search*
* Like linear search, binary search is used to find an element within some collection
* However, if I was doing a linear search for a number between :math:`0 -- 1023`, I could only guarantee that I would find the element in :math:`1024` guesses
* But with binary search, I was able to do it in :math:`10` or less guesses
* Though, this required the higher/lower information --- the data was sorted

    * A linear search has no such requirement


Complexity Analysis
-------------------

* The magic with binary search is that, with every guess I made, I was able to eliminate half of the remaining numbers

    * My first guess was :math:`512` --- if you said *lower* I know the number is between :math:`0 -- 511`, if you said *higher* I know it's between :math:`513 -- 1023`

* To generalize the idea, if I had :math:`n` numbers, and I guess the number :math:`\frac{n}{2}`

    * If you say lower, then the number must be between :math:`0 -- \frac{n}{2} - 1`
    * If you said higher, then the number must be between :math:`\frac{n}{2} + 1 -- (n - 1)`

* With linear search, every guess only eliminated one number

* Once again, let's consider the worse case scenario --- the ``needle`` is not within the ``haystack`` of size :math:`1024`

    * One guess gets me to :math:`512` numbers
    * Two guesses gets me to :math:`256` numbers
    * Three guesses get me to :math:`128`
    * Four gets me to :math:`64`
    * Five gets me to :math:`32`
    * Six gets me :math:`16`
    * Seven :math:`8`
    * Eight :math:`4`
    * Nine :math:`2`
    * Ten :math:`1`


* Originally, with linear search, the relationship between the input :math:`n` and the amount of work is :math:`n`

    * If there are :math:`n` things in the ``haystack``, I have to look at all :math:`n`
    * If we doubled the size to :math:`2n`, the amount of things needed to be looked at also doubles to :math:`2n`

* With binary search however, the relationship between the size of the input :math:`n` and the amount of work is :math:`log_{2}(n)`

    * Doubling the size to :math:`2n` only adds one more guess

        * :math:`log_{2}(2n)`
        * :math:`log_{2}(n) + log_{2}(2)`
        * :math:`log_{2}(n) + 1`

* Given that binary search requires :math:`log{2}(n)` basic operations vs. linear search's :math:`n`, binary search is the clear winner
* But, there is no such thing as a free lunch
* With binary search, we have the catch that the data must be sorted

* This is a *very* common pattern in developing algorithms

    * The more *general* your algorithm is, the worse the solution
    * The more you know about the *structure* of your problem, the more opportunities you have to use that knowledge to improve your algorithm


Linear Search in Other Programming Languages
============================================

* At this stage we have been programming exclusively in Python
* However, there are many other programming languages
* Learning a new programming language may feel intimidating, but you may be surprised at how similar many of them are

    * First, the underlying algorithms are the same, regardless of the language --- a linear search is a linear search
    * Second, even the syntax between many languages are remarkably similar

* Below is a collection of linear search algorithms in various popular programming languages

    * The purpose of their inclusion here is to get a sense of how similar and dissimilar programing languages can be

* Despite never learning the various languages, chances are you can still understand much of the code completely


Python
------

.. code-block:: python
    :linenos:
	
    def linear_search(haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle:
                return True
        return False


Java
----

.. code-block:: java
    :linenos:

    public static boolean linearSearch(int[] haystack, int needle){
        for(int i = 0 ; i < haystack.length ; i++){
            if(haystack[i] == needle){
                return true;
            }
        }
        return false;
    }


C#
--

.. code-block:: c#
    :linenos:

    public static boolean linearSearch(int[] haystack, int needle){
        for(int i = 0 ; i < haystack.length ; i++){
            if(haystack[i] == needle){
                return true;
            }
        }
        return false;
    }


C++
---

.. code-block:: cpp
    :linenos:

    bool linear_search(std::vector<int> haystack,  int needle){
        for(int i = 0 ; i < haystack.size() ; i++){
            if(haystack[i] == needle){
                return true;
            }
        }
        return false;
    }


C
-

.. code-block:: c
    :linenos:

    bool linear_search(int haystack[], int n, int needle){
        for(int i = 0 ; i < n ; i++){
            if(haystack[i] == needle){
                return true;
            }
        }
        return false;
    }


Haskell
-------

* Below you will see a linear search that looks quite different from the previous
* Haskell is an entirely different kind of programming language --- it is a *functional* programming language

    * It is, for better or worse, not nearly as popular as the languages seen in the above examples


.. code-block:: haskell
    :linenos:
	
    linear_search :: Eq a => [a] -> a -> Bool
    linear_search [] _ = False
    linear_search (x:xs) y = x==y || linear_search xs y
   
  
			
For Next Class
==============

* Read `Chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_


