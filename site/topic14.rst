**********************
Topic #14 -- Searching
**********************

.. image:: ../img/you_are_here.jpeg

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

    Write a function ``find_element(element, list)`` that returns ``True`` if ``element`` is in ``list`` and ``False`` otherwise. 

    You may *not* use the ``in`` operator (that's cheating!)

* Nothing new here... you already know how to search an unordered list.

.. admonition:: Activity
   
    Discuss this with your neighbours:
      
        * On average, how many iterations through your loop does your function make?
        * How about in the worst case?
        * Is your solution the best possible?
        * Might there exist some super clever algorithm that is somehow better (faster) than yours?   
	  
* These kinds of questions are getting you closer to computer *science* and further from straight "programming".	  

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/8unA_a5xcCU" frameborder="0" allowfullscreen></iframe>

.. admonition:: Activity

    James will now guess a number between 0 and 1023 in less than 10 guesses. 
   
.. admonition:: Activity++

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


Quick look at different programming languages
=============================================

Here are a few linear searchers in different programming languages. 

Python
------

.. code-block:: python
    :linenos:
	
    def linear_search(a_list, thing):
        for i in range(len(a_list)):
            if a_list[i] == thing:
                return True
        return False

C++
---
		
.. code-block:: cpp
    :linenos:	
	
    bool linear_search(int a_list[], int n, int thing){
        for(int i = 0 ; i < n ; i++){
            if(a_list[i] == thing){
                return true;
            }
        }
        return false;
    }

Java
----

.. code-block:: java
    :linenos:	
	
    public boolean linear_search(int[] a_list, int thing){
        for(int i = 0 ; i < a_list.length ; i++){
            if(a_list[i] == thing){
                return true;
            }
        }
        return false;
    }

Haskell
-------

.. code-block:: haskell
    :linenos:
	
    linear_search :: Eq a => [a] -> a -> Bool
    linear_search [] _ = False
    linear_search (x:xs) y = x==y || linear_search xs y
   
  
			
For next class 
==============

* Keep reading `chapter 14 of the text <http://openbookproject.net/thinkcs/python/english3e/list_algorithms.html>`_  


