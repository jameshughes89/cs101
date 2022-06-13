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

* Depending on your programming environment, the ``unittest`` tests may run automatically or may need to be run with a few clicks
* In our case, on Colab, we will need to run the tests with a line of code

    * ``unittest.main(argv=[''], verbosity=2, exit=False)``

* That's it --- if you wrote all your ``unittest`` tests on Colab, and you then run that line of code, it will run all your tests
* For now, ignore the arguments provided to the ``unittest.main`` call --- they're just needed to make it work

* After running your tests, if everything ran correctly, you will likely see something like this as output

.. code-block:: python
    :linenos:

    test_diameter_various_spheres_returns_correct_diameter (__main__.SphereTest) ... ok
    test_distance_between_centres_various_spheres_returns_correct_distance (__main__.SphereTest) ... ok
    test_distance_between_edges_various_spheres_returns_correct_distance (__main__.SphereTest) ... ok
    test_equal_on_sphere_and_string_returns_false (__main__.SphereTest) ... ok
    test_equals_on_equal_spheres_returns_true (__main__.SphereTest) ... ok
    test_equals_on_not_equal_spheres_returns_false (__main__.SphereTest) ... ok
    test_overlaps_various_spheres_returns_correct_boolean (__main__.SphereTest) ... ok
    test_repr_arbitrary_sphere_returns_correct_string (__main__.SphereTest) ... ok
    test_sphere_centre_point_returns_correct_point3D (__main__.SphereTest) ... ok
    test_sphere_radius_returns_correct_radius (__main__.SphereTest) ... ok
    test_surface_area_various_spheres_returns_correct_surface_area (__main__.SphereTest) ... ok
    test_volume_various_spheres_returns_correct_volume (__main__.SphereTest) ... ok

    ----------------------------------------------------------------------
    Ran 12 tests in 0.026s

    OK
    <unittest.main.TestProgram at 0x7f2810a68c90>


* In the above example output, every test passed
* However, if a test failed, we would see something like the below example

.. code-block:: python
    :linenos:

    test_diameter_various_spheres_returns_correct_diameter (__main__.SphereTest) ... ok
    test_distance_between_centres_various_spheres_returns_correct_distance (__main__.SphereTest) ...
    test_distance_between_edges_various_spheres_returns_correct_distance (__main__.SphereTest) ... ok
    test_equal_on_sphere_and_string_returns_false (__main__.SphereTest) ... ok
    test_equals_on_equal_spheres_returns_true (__main__.SphereTest) ... ok
    test_equals_on_not_equal_spheres_returns_false (__main__.SphereTest) ... ok
    test_overlaps_various_spheres_returns_correct_boolean (__main__.SphereTest) ... ok
    test_repr_arbitrary_sphere_returns_correct_string (__main__.SphereTest) ... ok
    test_sphere_centre_point_returns_correct_point3D (__main__.SphereTest) ... ok
    test_sphere_radius_returns_correct_radius (__main__.SphereTest) ... ok
    test_surface_area_various_spheres_returns_correct_surface_area (__main__.SphereTest) ... ok
    test_volume_various_spheres_returns_correct_volume (__main__.SphereTest) ... ok

    ======================================================================
    FAIL: test_distance_between_centres_various_spheres_returns_correct_distance (__main__.SphereTest) (case=(Sphere(Point3D(0, 0, 0), 1), Sphere(Point3D(1, 1, 0), 1)), expect=1.732051)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "<ipython-input-17-defcdea75152>", line 60, in test_distance_between_centres_various_spheres_returns_correct_distance
        self.assertAlmostEqual(expect, case[0].distance_between_centres(case[1]), 5)
    AssertionError: 1.732051 != 1.4142135623730951 within 5 places (0.31783743762690486 difference)

    ----------------------------------------------------------------------
    Ran 12 tests in 0.030s

    FAILED (failures=1)
    <unittest.main.TestProgram at 0x7f2810a882d0>


* To generate the error for demonstration purposes, I changed the ``test_distance_between_centres_various_spheres_returns_correct_distance`` test to be wrong
* You will see that the output from the test is a lot more helpful than the simple ``assert`` tests we used to write

    * It is telling us which test failed
    * It is telling us which *subtest* failed
    * It tells us what was expected
    * It tells us what we actually got
    * Just because a test failed, all other tests still ran





For Next Class
==============

* Check out the test folder in the `GitHub repo <https://github.com/jameshughes89/cs101>`_  to see the unit tests written for the course content 
* Read `Chapter 22 of the text <http://openbookproject.net/thinkcs/python/english3e/collections.html>`_
