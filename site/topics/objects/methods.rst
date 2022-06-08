******************************
Objects II --- More on Methods
******************************

* The ``Circle`` class discussed in the previous topic introduced:

    * How to write classes
    * How to write and make use of a constructor
    * Attributes, both how to set them and how to access them
    * How to write and use methods
    * How to make instances of the class

* In this topic, we will create more classes containing more complex functionality
* Additionally, we will see objects interacting with one another and how objects can provide a nice level of abstraction


* The goal is to define a ``Sphere`` class

    * Like the ``Circle`` class, it will know its radius
    * It will also know its position within some three dimensional space
    * It will provide functionality to measure distances between ``Sphere`` objects and check if they overlap/collide

* The catch is, we also need a way to specify the point in the three dimensional space
* To address this, we will define a ``Point3D`` class

    * It will know its position in the three dimensional space based on a three dimensional coordinate system
    * Provide some simple geometry functionality
    * Provide a way to measure distance between ``Point3D`` objects, which will help with implementing the ``Sphere`` class' functionality


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