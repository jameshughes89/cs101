********************************
Testing Your Code and Type Hints
********************************

* Writing code is a big part of your job when programming
* But testing and debugging your code is a bigger part


Testing
=======

* Once you write a function, you need to ensure that it is actually correct

    * Once a function is written we often call it a few times to check that it is doing what we expect
    * But we want to be a little more systematic and thorough in our tests

* We end up writing small snippets of code designed to test our code
* In addition to ensure correctness, writing tests for our code also helps us *think* about our code more

    * What is correct/incorrect
    * Different cases that your function needs to deal with
    * If there are any *edge cases*


Writing Tests
-------------

* For simplicity, we will keep our testing strategy to assertions about the data
* Let's say we want to test the absolute value function ``abs``

    * This function is provided to you by Python, so there is no actual need to test it here

* If we are to consider how we could test the ``abs`` function, we want to check that the function output (returns) matches what it should be based on the input (arguments)
* There is not too much to check with ``abs``

    * Check that the absolute value of a positive number is itself
    * Check that the absolute value of a negative number is the positive version of itself
    * Check that the absolute value of zero is zero

* Checking zero is perhaps not necessary, but it is somewhat of a peculiar case since zero doesn't have a sign, so it is good to test it

.. code-block:: python
    :linenos:

    assert 5 == abs(5)
    assert 5 == abs(-5)
    assert 0 == abs(0)


* If we run the above example, we should expect the program to produce no output since the assertions were all correct
* For the sake of demonstrating what would happen if an assertion failed, here is a broken absolute value function

.. code-block:: python
    :linenos:

    # Broken
    def broken_abs(x):
        return x

    assert 5 == broken_abs(5)
    assert 5 == broken_abs(-5)  # Should Fail
    assert 0 == broken_abs(0)


* The above ``broken_abs`` is clearly not correct as it just returns whatever ``x`` is, regardless of the sign
* If we run this code, we would see an error message like this

.. code-block:: python

        assert 5 == broken_abs(-5)
    AssertionError

* This is Python telling us that the assertion failed
* More precisely, it failed on the input of ``-5``
* This now informs us that the function is not correct, and under which condition it is not correct


Square of Sums Example Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Celsius to Fahrenheit Example Tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Automated Testing
-----------------




	
For Next Class
==============

* If you have not yet, read `Chapter 5 of the text <http://openbookproject.net/thinkcs/python/english3e/conditionals.html>`_
