********
Unittest
********

* You may have noticed that our simple ``assert`` tests are becoming more difficult to write as our programs grow in complexity
* For example, consider the ``Circle``, ``Point3D``, and ``Sphere`` classes

    * There is some setup required for tests (e.g. creating an instance of a class)
    * The ``assert`` tests get jumbled together
    * It is not easy to know what the test is testing just by doing a quick look
    * There are many similar tests with redundant test code

* Fortunately, Python provides tools for helping us test our code --- ``unittest``

* ``unittest`` provides a lot of functionality

    * Special assert methods
    * Automated testing
    * Sharing setup/shutdown methods
    * Subtests
    * Nicer test result reporting
    * ...

* We will only scratch the surface here, but there is a lot one can do with ``unittest``

* Fortunately, the basic idea of testing is the same with ``unittest`` as it is with our simple ``assert`` tests


Starting a Unit Test Class
==========================

* The first thing we need to do to start writing our unit tests with ``unittest`` is to import it
* Then we need to start defining a class

    * Our tests are actually going to be written within a class

.. code-block:: python
    :linenos:

    import unittest

    class Point3DTest(unittest.TestCase):
        # Tests go here


* In the above example, you will see the import and the start of the class

    * Although it is not needed on Colab, depending on how we have our tests setup, we may need to import the class being tested

* As a convention, we call our test classes ``SomeClassTest``, where ``SomeClass`` is the name of the class we are testing

    * Since the tests will be fore the ``Point3D`` class, we call it ``Point3DTest``

* You will also notice the ``unittest.TestCase`` within parentheses next to the class name

    * The nuance of what this means is outside the scope of this course, but in short, we need it in order to make use of the ``unittest`` framework


Writing Unit Tests
==================


Subtests
--------


Running Unit Tests
==================


For Next Class
==============

* Check out the test folder in the `GitHub repo <https://github.com/jameshughes89/cs101>`_  to see the unit tests written for the course content 
* Read `Chapter 22 of the text <http://openbookproject.net/thinkcs/python/english3e/collections.html>`_
