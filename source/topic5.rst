*******************************************
Topic #5 -- Logic, Booleans, More Functions
*******************************************

The Boolean type
================
* A value that is either ``True`` or ``False`` (and nothing else) has type `Boolean <http://en.wikipedia.org/wiki/George_Boole>`_.
* We've used comparison operators (e.g., ``<, >, ==``) in conditionals.
* What's going on "under the hood" with the comparison, though?
    >>> 5>2
    True
    
    >>> 5<2
    False
	
* A comparison like ``a > b`` is just an *expression*, like ``a + b``.
* The difference is that the value it produces isn't an integer, it's either ``True`` or ``False``
* This may seem like a subtle thing, but it's a big deal:
    * An operator that takes 2 numbers and produces a number: 
        * `1 + 1 -> 2`
    * An operator that takes 2 booleans and produces a boolean: 
        * `True and False -> False`
    * An operator that athes 2 numbers and produces a boolean: 
        * `1 < 2 -> True`
   

    >>> type(5>2)
    <class 'bool'>

.. admonition:: Activity

    Write a function ``is_negative(n)`` that *returns* ``True`` if the argument ``n`` is negative and ``False`` otherwise.

    Verify that the return type is correct.

     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/xrBzzvmLCvQ" frameborder="0" allowfullscreen></iframe>   


More about returns
==================

* We've already seen that functions can return a value at the end.
* In fact, a function can return a value *at any time*, not just the end.
* We can take advantage of this fact to have multiple returns!::

    def divisible_by(a,b):
        if a % b == 0:
            return True
        else:
            return False

.. admonition:: Activity

    * What is the result of the function call ``divisible_by(4, 2)``? 
    * How about ``divisible_by(4, 3)``? 
    * Now write a new function ``not_divisible_by(a, b)`` that returns ``True`` when ``a`` is *not* divisible by ``b`` and ``False`` otherwise.
    * Now write this function to do the same thing with only **1** return statement.
    * Now write it with only **1** line of code within the function (so, 2 lines including the function header).
   
* Functions returning Boolean values are pretty handy. Why? Where do you see yourself using them?

The function type
=================

* In Python, *functions* have a type, too:
	>>> type(divisible_by)
	<class 'function'>
	
* Not all programming languages are so enlightened.
* You can read up on `first-class functions <http://en.wikipedia.org/wiki/First-class_function>`_ if you want to be a nerd about it.
* This allows us to do some very "meta" things and quickly write code that is really general::

    def add(a,b):
        return a+b

    def subtract(a,b):
        return a-b
        
    def do_something(f,a,b):
        return f(a,b)

.. admonition:: Activity

    * What is the value of ``do_something(add, 5, 7)``?
    * How about ``do_something(substract, 5, 7)``?
    * Now make sense of what exactly is happening!
   
* If all of this weirds you out... good. You're normal. Passing around functions is crazy weird stuff.
* Don't worry if you aren't 100% confident on this yet. We'll come back to it in more detail later.

  .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/7CAIlaxRpsg" frameborder="0" allowfullscreen></iframe>


Developing bigger programs
==========================

.. image:: ../img/softeigineering.jpeg

* The best way to do this is still a (very) open research problem in software engineering.
* Here, I'm going to suggest *bottom up*, incremental, development.
* Start with an empty function that returns a constant value (e.g., 0.0)
* Try the function. Works? Ok, step 1 down.
* Add 1 or 2 lines of code to accomplish part of what you want to do.
* Try the function. Make sure those lines worked!
* Repeat.
* Build up your function *incrementally* and **test** at each increment.
* The alternative is to try to sit down and bang out the whole function in one go.
    * If you're perfect, this is faster.
    * Otherwise... you'll spend a *lot* of time debugging.
        * You're already going to spend a lot of time debugging, so don't give yourself more work. 
    * Besides, I'm sorry, but you're not perfect.
   
.. admonition:: Activity

    Build a function to compute compound interest given a starting amount(``P``), an annual interest rate (``r``), the number of compounding periods per year(``n``) and the total number of years (``t``). 

    Your function should return the value of the principle plus the interest after compounding.

     .. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/epghFryGafA" frameborder="0" allowfullscreen></iframe>
	

* For bigger projects: break your problem down into a hierarchy of subproblems (remember, think in terms of *levels of abstraction*!).
* Solve the easiest, smallest, subproblems first.
* For us, solving means "writing a function to do it".
* Immediately after writing the function, *test it right there and then*.
* Once you've written all the really easy, low level, functions, start combining them to write the higher level ones.
