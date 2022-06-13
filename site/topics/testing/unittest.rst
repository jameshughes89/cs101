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

.. code-block:: python
    :linenos:

    import unittest

    class SphereTest(unittest.TestCase):

        def test_sphere_centre_point_returns_correct_point3D(self):
            sphere = Sphere(Point3D(0, 0, 0), 1)
            self.assertEqual(Point3D(0, 0, 0), sphere.centre_point)

        def test_sphere_radius_returns_correct_radius(self):
            sphere = Sphere(Point3D(0, 0, 0), 1)
            self.assertEqual(1, sphere.radius)


* Above are two tests confirming the correctness of the constructor and the assigning of the ``Sphere`` class' attributes
* Key things to note here are

    * The tests are methods that belong to the class
    * Each method starts with the name ``test_``

        * The method names are descriptive so it's easy to know what it tests

    * We make use of ``assertEqual``, which is a method referenced by the ``self`` reference variable

        * Although we did not write this method, we inherit it from ``unittest.TestCase``
        * We used ``assertEqual`` here, but there are many other methods for various types of tests, some of which will be covered here

    * The method provides a simple mechanism for setup code to be grouped with the test itself

        * Create a ``Sphere`` object
        * Test something about the object

    * Each test should test one thing

        * This makes it easier to isolate what exactly went wrong


* Other than those points, so far there is not much more to point out here since we have been writing tests for a while
* The basic idea of how we write the tests is the same
* The only difference is the syntax of writing the tests with ``unittest``


.. code-block:: python
    :linenos:

    import unittest

    class SphereTest(unittest.TestCase):

        # Other test methods not shown for brevity

        def test_equals_on_equal_spheres_returns_true(self):
            sphere_a = Sphere(Point3D(1, 2, 3), 1)
            sphere_b = Sphere(Point3D(1, 2, 3), 1)
            self.assertTrue(sphere_a == sphere_b)

        def test_equals_on_not_equal_spheres_returns_false(self):
            sphere_a = Sphere(Point3D(1, 2, 3), 1)
            sphere_b = Sphere(Point3D(1, 2, 3), 2)
            self.assertFalse(sphere_a == sphere_b)

        def test_equal_on_sphere_and_string_returns_false(self):
            sphere = Sphere(Point3D(1, 2, 3), 4)
            self.assertFalse("Sphere(Point3D(1, 2, 3), 4)" == sphere)

        def test_repr_arbitrary_sphere_returns_correct_string(self):
            sphere = Sphere(Point3D(1, 2, 3), 4)
            self.assertEqual("Sphere(Point3D(1, 2, 3), 4)", str(sphere))


* Above are additional tests for the magic methods ``__eq__`` and ``__repr__``
* For two of the ``__eq__`` methods, you will see the setup is a little more involved as we need two ``Sphere`` objects for the test
* You will also notice the use of ``assertTrue`` and ``assertFalse``

* Although all test methods must start with ``test_``, as a convention for consistency and readability, method names will follow a pattern

    * ``test_method_condition_expected``

* One of the above examples is  ``test_equals_on_equal_spheres_returns_true``

    * ``equals`` is the method being tested
    * ``on_equal_spheres`` is the condition
    * ``returns_true`` is what is expected



Subtests
--------


Running Unit Tests
==================


For Next Class
==============

* Check out the test folder in the `GitHub repo <https://github.com/jameshughes89/cs101>`_  to see the unit tests written for the course content 
* Read `Chapter 22 of the text <http://openbookproject.net/thinkcs/python/english3e/collections.html>`_
