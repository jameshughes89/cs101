************************
Searching and Complexity
************************

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


Linear Search
=============

* By now we have seen linear search multiple times
* Given our familiarity of the problem and the linear search algorithm, we will use it as a starting point to begin thinking a little deeper into our algorithms

.. code-block:: python
    :linenos:

    def linear_search(haystack, needle):
        for element in haystack:
            if element == needle:
                return True
        return False


* Having a correct algorithm for a problem is clearly important
* But we also want to make sure we have a *good* algorithm
* However, what does it mean for an algorithm to be *good*?

.. admonition:: Activity
    :class: activity
   
    Discuss this with your neighbours:
      
        * On average, how many iterations of the loop does ``linear_search`` need before it finds the ``needle``?
        * If the element you are looking for is *not* in the list, how many times will the loop run?
        * What would be the situation to cause the loop to only need to run one iteration?
        * How much *space* does your algorithm require?
        * Is your solution the best possible?
        * Might there exist some super clever algorithm that is somehow better (faster) than yours?   
	  

  .. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/8unA_a5xcCU" frameborder="0" allowfullscreen></iframe>


Complexity Analysis
-------------------

* The above activity highlights the major ideas used to discuss the *goodness* of an algorithm
* More precisely, we analyze the *Computational Complexity* of an algorithm

    * The amount of resources the algorithm needs to run

* The main focus is the *time complexity* and the *space* complexity

    * Time complexity is the number of basic operations the algorithm requires
    * Space complexity is the amount of memory the algorithm requires

* To keep things simple, it is common to think about the worst case scenario for the complexity analysis
* We also like to consider the amount of work required based on the size of the input
* For example, the worst case scenario for ``linear_search`` is if the ``needle`` does not exist within ``haystack``

    * If ``haystack`` has length of 10, the loop will run 10 times before we conclude that ``needle`` is not there
    * If ``haystack`` has length of 100, the loop will run 100 times
    * If ``haystack`` has length of 10,000,000, the loop will run 10,000,000 times
    * If ``haystack`` has length of :math:`n`, the loop will run :math:`n` times

* As for space complexity, this ``linear_search`` only requires space for storing ``haystack``

    * Assuming ``haystack`` has length :math:`n`, then we require :math:`n` amount of space


.. admonition:: Activity
    :class: activity

    James will now guess a number between 0 and 1023 in less than 10 guesses. 
   
.. admonition:: Activity++
    :class: activity

    Think of how a function ``find_element(element,sorted_list)`` that returns ``True`` if ``element`` is in ``sorted_list``  and ``False`` otherwise would be written.

    You may *not* use the ``in`` operator (that's still cheating!). 

    This time, I *promise* you that I will only call your function on a list which is *already sorted*. Do this in a group. It's not an easy one. 
   
    If you can, code up the solution. 
   

* Now we need to ask the same questions as before:
    * On average, how many iterations through your loop does your function make?
    * How about in the worst case?
    * Is your solution the best possible?
    * Might there exist some super clever algorithm that is somehow better (faster) than yours?	
			
* This is a *very* common pattern in developing algorithms:
    * The more *general* your problem is, the slower the solution is.
    * The more you know about the *structure* of your problem (e.g., "the list is always sorted"), the more opportunities you have to use that knowledge to make the solution faster.


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


