*********
Searching
*********

.. image:: you_are_here.jpeg

You are *here*
==============

* At this point in the course you should feel like:
    * The Python programming environment is a relatively familiar sight (Colab, IPython, PyCharm, Spyder)
    * You're growing more comfortable using Python to accomplish small tasks
    * If you saw a simple Python program, you could figure out, more or less, what it does without having to run it
    * You know what a variable is
    * You know what a data *type* is (particularly: strings, integers, booleans and floating point numbers)
    * You know that strings are *special*
    * You know that you have to be *very careful* with floating point values
    * You know what lists, arrays, tuples and dictionaries are and how they differ
    * You know about mutability and aliasing in data structures
    * You know how to use ``if`` statements to *conditionally* execute code
    * You know how to write, and call, functions
    * You know what a "pure" function is and what "side effect" means.
    * You know how (and when) to use both ``for`` loops and ``while`` loops
    * You know how to develop your own code, one small step at a time, testing along the way.
    * You know how to debug and use a debugger
    * You know how to comment your code so you can read it next week.
    * You know how to get data into and out of python with files. 
    * You know that exceptions are a thing
    * You know how to use objects
    * You know how to make your own objects

Back to fundamentals
====================

* We've actually gone pretty deep into topics, so it's time to go back to some basic CS.
* We have a lot of tools in our tool belt 
* We have a solid understanding of some *data structures*
* We're kinda' missing out on the *algorithms* at this point
* We'll actually look at some real, but challenging problems
* We will look at some *good* ways to solve these problems  
* We'll look at *bad* ways too. 


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

    I will guess a number between 0 -- 1023 in 10 or less guesses.

    There is a catch however --- you have to tell me if the number is *higher* or *lower* than my guess before I guess
    again.


* This is an example of a *binary search*
* Like a linear search, binary search is used to find an element within some collection
* However, if I was doing a linear search for a number between 0 -- 1023, I could only guarantee that I would find the element in 1024 guesses
* But with binary search, I was able to do it in 10 or less guesses
* Though, this required the higher/lower condition --- the data was sorted

    * A linear search has no such requirement


Complexity Analysis
-------------------

*



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


