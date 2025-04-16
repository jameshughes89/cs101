*****************
Country Catalogue
*****************

* **Worth**: 5%
* **DUE**: Monday June 23 at 11:55pm; submitted on MOODLE.
* **Files**: :download:`asn4.ipynb <asn4.ipynb>`/:download:`asn4.py <asn4.py>` and :download:`country_data.csv <country_data.csv>`


Task
====

The goal is to create a collection of ``Country`` objects. The collection, called a ``CountryCatalogue``, will provide
functionality to store (add/remove) the ``Country`` objects in addition to making inquiries about the data in the
collection.

You will

* Create a ``Country`` class to store details about a country
* Create a ``CountryCatalogue`` class

    * Provide a way to add and remove ``Country`` objects
    * Search through the catalogue
    * Ask questions about the data in the catalogue
    * Filter data in the catalogue

* Use the written classes to build a ``CountryCatalogue``
* Read data from a file
* Write data to a file


Provided Files
==============

You are provided with

* A notebook file called :download:`asn4.ipynp <asn4.ipynb>` containing the starting point of the assignment

    * This file is to be uploaded to `Google Colab <https://colab.research.google.com/>`_
    * The notebook contains the start of the ``Country`` and ``CountryCatalogue`` classes
    * The notebook contains unit tests for the ``Country`` and ``CountryCatalogue`` classes
    * The notebook contains already written code that will make use of the classes you are to write
    * The notebook also includes a special if statement ``if __name__ == "__main__":`` at the end

        * This is included to help with marking and unit tests
        * More details on this line are provided below

    * Alternatively, if you prefer to complete the assignment with an IDE on your own computer, you may download and use the :download:`asn4.py <asn4.py>` file

* A data file called :download:`country_data.csv <country_data.csv>` containing information about countries that will be used to populate the ``CountryCatalogue``


.. warning::

    Do not alter the function details in the provided .ipynb/.py files

        * Do not change the name of the functions
        * Do not remove the function description
        * Do not remove or add to the parameter list



Part 0 --- Read the Assignment
==============================

Read the assignment description in its entirety before starting.


Part 1 --- Uploading Files to Colab
===================================

After downloading the notebook and data files above, you will need to upload them to Colab to get started. See the
respective section from assignment 1 for an example on how to do this. I recommend saving a copy of this notebook file
and csv data file to your Google drive and then work with that one. You don't have to, but you will have to re-upload
the project every time you want to work on it.


Country Class
=============

The ``Country`` class is simply going to represent an individual country. For our purposes, a ``Country`` will know its
``name``, ``continent``, ``population``, and land ``area``. In addition to the attributes, a ``Country`` will also be
able to determine it's population density (``population/area``). A method for determining equality (``__eq__``) and
generating a nice, human readable string representation of the ``Country`` object (``__repr__``) will be written.


Part 2 --- Country Constructor
------------------------------

Write the constructor (``__init__``) for the ``Country`` class. The constructor will take a country ``name``, which
``continent`` it's on, its ``population``, and the total land ``area`` as parameters. The constructor will assign the
values passed as parameters to their respective attributes --- ``name``, ``continent``, ``population``, and ``area``.


Part 3 --- Population Density
-----------------------------

Write a method ``population_density`` that returns the population density of the ``Country`` object. The population
density should be a float.


Part 4 --- Equals and Repr
--------------------------

Write the ``__eq__`` magic method for the ``Country`` class. For our purposes, two ``Country`` objects will be
considered equal if all their attributes are equal.

Write the ``__repr__`` magic method for the ``Country`` class. For our needs, we will simply follow the pattern
``ClassName(attribute=value, attribute=value, ...)``. For example, representing the country Canada as a string would
be ``Country(name=Canada, continent=North America, population=34207000, area=9976140.00)``.


Part 5 --- Testing Country Class
--------------------------------

To help ensure correctness, run the ``CountryTest`` class and ensure all unit tests pass. If any of the tests fail, read
which test failed and under which condition. The output of the tests will help guide your debugging.

To run the tests, run the cell in the notebook containing the following

    .. code-block:: python

        # Run this cell to run all unit tests
        unittest.main(argv=[''], verbosity=2, exit=False)


Country Catalogue Class
=======================

The ``CountryCatalogue`` class holds reference to a collection of ``Country`` objects. Additionally, the
``CountryCatalogue`` provides some functionality to ask questions about the collection of data.

The ``CountryCatalogue`` is effectively a list keeping track of the ``Country`` objects with additional proprietary
methods. Details on the functionality is provided below.

Although the description of this class is provided with an order and each part is numbered, one should feel free to
complete the methods in any order they see fit. For example, the ``__len__`` magic method, which is described last, may
be helpful when writing the other methods. This may motivate one to write it earlier.


Part 6 --- Country Catalogue Constructor
----------------------------------------

Write the constructor (``__init__``) for the ``CountryCatalogue`` class. The constructor for the class is simple ---
initialize the object with an attribute assigned to a reference to an empty list. It is recommended to call the
attribute ``_catalogue``. The underscore is included before since this attribute is not intended to be accessed directly
from outside the clas. 


Part 7 --- Private Find Method
------------------------------

Write a method ``_find`` that takes a reference to a ``Country`` object and returns the index of the first occurrence of
an equivalent ``Country`` within the catalogue. If no matching ``Country`` exists, the method will return ``-1``.

This method is "private", which means that it should not be accessed/used except from inside the object. In Python,
this "private" property is not enforced, but for methods or attributes that are intended to be "private", the convention
is to start the method name with an underscore (``_``), thus the name ``_find``.


Part 8 --- Contains
-------------------

Write a method called ``contains`` that takes a reference to a ``Country`` object as a parameter and returns ``True`` if
an equivalent ``Country`` object exists within the collection, and ``False`` otherwise.


Part 9 --- Add
--------------

Write a method ``add`` that takes a ``Country`` object as a parameter and adds the provided ``Country`` to the
collection. In other words, append the provided ``Country`` to the ``CountryCatalogue`` object's attribute referencing
a list. This method returns nothing.


Part 10 --- Remove
------------------

Write a method ``remove`` that takes a ``Country`` object as a parameter and removes the first occurrence of an
equivalent ``Country`` object from the ``CountryCatalogue``. This method returns a reference to the removed ``Country``
object. If no equivalent ``Country`` object is found within the ``CountryCatalogue``, then the method will raise a
``ValueError`` exception.


Part 11 --- Largest Density
---------------------------

Write a method ``country_with_largest_population_density`` that returns a reference to the ``Country`` object within the
``CountryCatalogue`` that has the largest population density. If the ``CountryCatalogue`` is empty, this method will
raise an ``IndexError`` exception.


Part 12 --- Smallest Density
----------------------------

Write a method ``country_with_smallest_population_density`` that returns a reference to the ``Country`` object within
the ``CountryCatalogue`` that has the smallest population density. If the ``CountryCatalogue`` is empty, this method
will raise an ``IndexError`` exception.


Part 13 --- Filter by Density
-----------------------------

Write a method ``filter_countries_by_population_density`` that takes a range of population density values as parameters
and returns a new ``CountryCatalogue`` object with references to ``Country`` objects that fall within the specified
population density range. The range specified will be :math:`[low, high)`; the ``Country`` objects with a population
density greater-than or equal to the low and strictly less-than the high will be included in the filtered
``CountryCatalogue``. If no ``Country`` objects fall within the specified range, this method will return an empty
``CountryCatalogue``.

For example, calling ``some_catalogue.filter_countries_by_population_density(200, 250)`` would return a new
``CountryCatalogue`` containing references to all the ``Country`` objects within ``some_catalogue`` that have a
population density :math:`\ge 200` and :math:`< 250`.


Part 14 --- Most Populous Continent
-----------------------------------

Write a method ``most_populous_continent`` that returns the name of the continent (as a string) that has the largest
population based on information within the ``CountryCatalogue``. If the the ``CountryCatalogue`` is empty, this method
raises an ``IndexError`` exception.

This method will only consider the ``Country`` objects contained within the ``CountryCatalogue``. In other words,
although Asia has a large population, if no ``Country`` objects from Asia were included in the ``CountryCatalogue``,
then those populations are not considered in the calculation.

Further, this method should work on any arbitrary planet within our universe that may have unusual continent names (do
not hard code any details about continents based on Earth).

**Hint:** Consider using a dictionary within this method to help with determining each continent's population.


Part 15 --- Equals, Repr, get item, and Length
----------------------------------------------

Write the ``__eq__`` magic method for the ``CountryCatalogue`` class. For our purposes, two ``CountryCatalogue`` objects
will be considered equal if their attributes (list of ``Country`` objects) are equal.

Write the ``__repr__`` magic method for the ``CountryCatalogue`` class. For our needs, the string should be an aggregate
of each individual ``Country`` object's string representation, each on their own line. For example

    .. code-block:: text

        Country(name=Canada, continent=North America, population=34207000, area=9976140.00)
        Country(name=China, continent=Asia, population=1339190000, area=9596960.00)
        Country(name=Egypt, continent=Africa, population=93383574, area=1000000.00)
        Country(name=France, continent=Europe, population=64668129, area=541656.76)


Write the ``__getitem__`` magic method for the ``CountryCatalogue`` class. This method takes an index as a parameter and
returns a reference to the ``Country`` object at ths specified index. For more details on this method,
`see the relevant documentation <https://docs.python.org/3/reference/datamodel.html#object.__getitem__>`_.

Write the ``__len__`` magic method for the ``CountryCatalogue`` class. This method returns the number of ``Country``
objects stored within the ``CountryCatalogue``.


Part 16 --- Testing Country Catalogue Class
-------------------------------------------

To help ensure correctness, run the ``CountryCatalogueTest`` class and ensure all unit tests pass. If any of the tests
fail, read which test failed and under which condition. The output of the tests will help guide your debugging.

To run the tests, run the cell in the notebook containing the following

    .. code-block:: python

        # Run this cell to run all unit tests
        unittest.main(argv=[''], verbosity=2, exit=False)


Part 17 --- Putting it Together
===============================

The *main* portion of the code that was provided is what *puts everything together*. This code

* Opens a file and loads the data into a ``CountryCatalogue``
* Makes changes to the contents of the ``CountryCatalogue``
* Asks questions of the data in the ``CountryCatalogue``
* Filters the ``CountryCatalogue`` based on population density
* Saves the filtered data to a file

If everything was implemented correctly, this code should run with no issue. Although no unit tests are provided for
this portion of code, you can likely determine if everything worked correctly by checking the output of the program.


Part 18 --- Testing
===================

Unlike previous assignments, no assertion tests are provided. Instead, to help ensure that your program is correct, run
the provided **unittests**. There is no guarantee that if your code passes all the tests that you will be correct, but
it certainly helps provide peace of mind that things are working as they should.

There are no unittests for the *main* portion of the assignment discussed in the previous part.

Realistically you should have been running tests after you complete each of the above parts, but this part is here to
remind you. Remember, we are lucky that we get to test our solutions for correctness ourselves; you don't need to wait
for the marker to return your assignment before you have an idea of if it works correctly.

To run the tests, run the cell in the notebook containing the following

    .. code-block:: python

        # Run this cell to run all unit tests
        unittest.main(argv=[''], verbosity=2, exit=False)


Some Hints
==========

* Work on one function at a time
* Get each function working perfectly before you go on to the next one
* Test each function as you write it

    * This is a really nice thing about programming; you can call your functions and see what result gets returned
    * Mentally test before you even write --- what does this function do? What problem is it solving?

* If you need help, ask

    * Drop by office hours


Some Marking Details
====================

.. warning::
    Just because your program produces the correct output, that does not necessarily mean that you will get perfect, or
    even that your program is correct.

Below is a list of both *quantitative* and *qualitative* things we will look for:

* Correctness?
* Did you follow instructions?
* Comments?
* Variable Names?
* Style?
* Did you do just weird things that make no sense?


What to Submit to Moodle
========================

* Make sure your **NAME** and **STUDENT NUMBER** appear in a comment at the top of the program
* Submit your version of ``asn4.py`` to Moodle

    * Do **not** submit the .ipynb file
    * To get the ``asn4.py`` file from Colab, see the example image in Assignment 1


.. warning::

    Verify that your submission to Moodle worked. If you submit incorrectly, you will get a 0.


Assignment FAQ
==============

* :doc:`See the general FAQ </assignments/faq>`
