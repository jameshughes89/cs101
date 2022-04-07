********************************
Testing Your Code and Type Hints
********************************

* Writing code is a big part of your job when programming
* But testing and debugging your code is a bigger part


Testing
=======

* Once you write a function, you need to ensure that it is actually correct

    * Once a function is written we often call it a few times to check that it is doing what we expect
    * But we want to be a little more systematic and through in our tests

* We end up writing small snippets of code designed to test our code
* In addition to ensure correctness, writing tests for our code also helps us *think* about our code more

    * You will have to think about what is correct/incorrect
    * Think about the different cases that your function needs to deal with
    * If there are any *edge cases*


Writing Tests
-------------

* For simplicity, we will keep our testing strategy to assertions about the data
* Let's say we want to test the absolute value function ``abs``

    * This function is provided to you by Python, so there is no actual need to test it here
    * It is just being used for demonstration purposes

* If we are to consider how we could test the ``abs`` function, I would want to make sure that the function output (returns) matches what it should be based on the input (parameters)
* There is not too much to check with ``abs``
    * Check that the absolute value of a positive number is itself
    * Check that the absolute value of a negative number is the positive version of itself
    * Check that the absolute value of zero is zero

* Checking zero is perhaps not necessary, but it is somewhat of a peculiar case since zero doesn't have a sign


Square of Sums Example Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Celsius to Fahrenheit Example Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Automated Testing
-----------------




	
For Next Class
==============

* If you have not yet, read `Chapter 5 of the text <http://openbookproject.net/thinkcs/python/english3e/conditionals.html>`_
