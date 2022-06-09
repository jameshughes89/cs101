***********************************
Objects III --- Interacting Objects
***********************************

* We completed the ``Sphere`` class in the previous topic, and it will work for our needs
* However, there are a few things we could do to improve the design and implementation
* One idea is to make a ``Point3D`` class to manage all the point related things

    * Location in three dimensional space
    * Distance between points
    * Equality on points

* Although there is nothing wrong with the original ``Sphere`` implementation, let's consider that

    * It will make our ``Sphere`` class simpler and easier to understand
    * It allows us to write the methods at a higher-level of abstraction since can deal with ``Point3D`` objects instead of individual coordinates
    * If we wanted to make other three dimensional shapes, they could use something like a ``Point3D`` class to represent their position
    * It allows us to abstract and delegate some functionality to another class
    * It will help with testing since we can test the ``Point3D`` class' functionality and the ``Sphere``\s independently


Point3D Class
=============


Constructor and Attributes
--------------------------


Methods
-------


Magic Methods
^^^^^^^^^^^^^



Testing
-------

* Below is a series of ``assert`` tests verifying the ``Point3D`` class' correctness
* Like before, these tests *work*, but we area pushing the limits of our simple ``assert`` tests

.. code-block:: python
    :linenos:

    point_origin = Point3D(0, 0, 0)
    assert 0 == point_origin.x
    assert 0 == point_origin.y
    assert 0 == point_origin.distance_from_origin()
    assert 0 == point_origin.distance_from_point(Point3D(0, 0, 0))
    assert 0.001 > abs(point_origin.distance_from_point(Point3D(1, 1, 1)) - 1.732051)
    assert 0.001 > abs(point_origin.distance_from_point(Point3D(-1, -1, -1)) - 1.732051)
    assert Point3D(1, 1, 1) == point_origin.find_midpoint(Point3D(2, 2, 2))
    assert Point3D(-1, -1, -1) == point_origin.find_midpoint(Point3D(-2, -2, -2))
    assert Point3D(0, 0, 0) == point_origin.find_midpoint(Point3D(0, 0, 0))
    assert "Point3D(0, 0, 0)" == str(point_origin)

    point = Point3D(-2, 7, 4)
    assert 0.001 > abs(point.distance_from_origin() - 8.306624)
    assert 0.001 > abs(point.distance_from_point(Point3D(0, 0, 0)) - 8.306624)
    assert 0.001 > abs(point.distance_from_point(Point3D(6, 3, 0)) - 9.797959)
    assert Point3D(5, 5.5, 3) == point.find_midpoint(Point3D(12, 4, 2))
    assert "Point3D(-2, 7, 4)"

    assert point != point_origin
    assert point_origin == Point3D(0, 0, 0)


Sphere Class
============


Constructor and Attributes
--------------------------


Methods
-------



Testing
-------



For Next Class
==============

* Read `Chapter 21 of the text <http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html>`_