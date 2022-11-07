*****************
Country Catalogue
*****************

* **Worth**: 10%
* **DUE**: December 5th at 11:55pm; submitted on MOODLE.
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

* A data file called :download:`country_cata.csv <country_data.csv>` containing information about countries that will be used to populate the ``CountryCatalogue``


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

Write the constructor (``__init__``) for the ``Country`` object. The constructor will take a country ``name``, which
``continent`` it's on, its ``population``, and the total land ``area`` as parameters. The constructor will assign the
values passed as parameters to their respective attributes --- ``name``, ``continent``, ``population, and ``area``.


Part 3 --- Population Density
-----------------------------

Write a method ``population_density`` that returns the population density of the ``Country`` object. The population
density should be a float.


Part 4 --- Equals and Repr
--------------------------

Write the ``__eq__`` magic method for the ``Country`` class. For our purposes, two ``Country`` objects will be
considered equal if all their attributes are equal.

Write the ``__repr__`` magic method for the ``Country`` class. For our needs, we will simply follow the pattern
``ClassName(attribute, values)``. For example, representing the country Canada as a string would be
``Country(name=Canada, continent=North America, population=34207000, area=9976140.00)``.


Part 5 --- Testing Country Class
--------------------------------

To help ensure correctness, run the ``CountryTest`` class and ensure all unit tests pass. If any of the tests fail, read
which test failed and under which condition. The output of the tests will help guide your debugging.


Country Catalogue Class
=======================


Part 6 --- Country Catalogue Constructor
----------------------------------------


Part 7 --- Private Find Method
------------------------------


Part 8 --- Contains
-------------------


Part 9 --- Add
--------------


Part 10 --- Remove
------------------


Part 11 --- Largest Density
---------------------------


Part 12 --- Smallest Density
----------------------------


Part 13 --- Filter by Density
-----------------------------


Part 14 --- Most Populous Continent
-----------------------------------


Part 15 --- Equals, Repr, get item, and Length
----------------------------------------------


Part 16 --- Testing Country Catalogue Class
-------------------------------------------



Part 17 --- Putting it Together
==============================




Part 18 --- Testing
===================

Unlike previous assignments, no assertion tests are provided. Instead, to help ensure that your program is correct, run
the provided **unittests**. There is no guarantee that if your code passes all the tests that you will be correct, but
it certainly helps provide peace of mind that things are working as they should.

There are no unittests for the ``asn4.py``.

Realistically you should have been running tests after you complete each of the above parts, but this part is here to
remind you. Remember, we are lucky that we get to test our solutions for correctness ourselves; you don't need to wait
for the marker to return your assignment before you have an idea of if it works correctly.


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



.. warning::

    Verify that your submission to Moodle worked. If you submit incorrectly, you will get a 0.


Assignment FAQ
==============

* :doc:`See the general FAQ </assignments/faq>`





















Part 2
======

Make a CountryCatalogue class. 

**Properties/attributes** for the CountryCatalogue class:

* catalogue: set
    * Will hold Country objects
* country_continent: dictionary
    * Will let us look up a country's continent easily

**Methods**:

* Constructor --- This one is complex-ish
    * Create the two properties/attributes (catalogue, country_continent)
    * This constructor will be given additional parameters, *continent_file_name* and *country_file_name*. Both are strings. 
    * Open the file named *continent_file_name* and add the country continent information from the file to the country_continent dictionary.
        * *continent_file_name* is a parameter. So, imagine the file is called "continents.txt", then *continent_file_name* would contain the string "continent.txt".
		
    * Open the file named *country_file_name*. Read the contents and use it to create country objects. Add these country objects to the catalogue set. 
        * I wonder how we can easily get the country's continent?
        * I wonder if we can use one of the below methods to basically do all this for us? (maybe, maybe not, idk)
        * Be sure you're actually creating country objects, and not like a list of strings or something. That would be bad.
        		

    * Obtain the sample data files (you might have to *right click* and select *save link as*):
        * :download:`Continents <continent.txt>`
        * :download:`Countries <country.txt>`
		
    * Note that they have headers. 
	
* add_country
    * Gets parameters *country_name*, *country_population*, *country_area*, and *country_continent*.
    * Given the parameters, create a country object. 
    * If there is a country in the catalogue with the same name, return *False*. 
    * If the country does not exist in the catalogue, add it to the catalogue.
    * Be sure to add appropriate information to the country_continent dictionary. 
    * Return *True* after success. 
    * I wonder if this method will be handy for the constructor? Maybe, maybe not. 
	
* delete_country
    * Given a parameter *country_name*, if a country with that name exists in the catalogue, remove it. 
    * Don't worry about updating the country_continent dictionary. 
    * Print a message informing the user if it was successfully removed or not.
    * Do **not** return anything.

* find_country
    * Given a parameter *country_name*, if the country exists, return it.
	* If it does not exist, return *None*. 
	
* filter_countries_by_continent
    * Given a parameter *continent_name*, return a list containing all the countries from the continent.
    * If the continent does not exist, return just an empty list. 

* print_country_catalogue
    * Print out the countries in the catalogue to the screen.
    * To do this, just loop through the catalogue and call ``print`` on the countries (this will work once ``__repr__`` is done in the Country class. 
	
* set_population_of_country
    * Given parameters *country_name* and *country_population*, set the country's population. 
    * Return *True* if it worked, *False* otherwise. 

* find_country_largest_pop
    * Find the country with the largest population and return the country object. 
	
* find_country_smallest_area
    * Find the country with the smallest area and return the country object. 
	
* filter_countries_pop_density
    * Given parameters *lower_bound* and *upper_bound* (both integers).
    * Find all countries that have a population density that falls between the bounds (inclusively)
    * Return a list that contains all of these countries. 
    * If nothing falls within the bounds, return an empty list. 
	
* find_most_populous_continent
    * Find the continent with the most number of people living on it (based on the countries in the catalogue). 
    * Return the name of the continent **and** its total population. 
    * Do this by writing ``return continent_name, population``, where *continent_name* is the name of the population with the highest population and *population* is the highest population. 
	
* save_country_catalogue
    * Given a parameter *file_name* (a string), write the catalogue data in a file named *file_name*. 
    * This function must return the number of lines written to the file. 
    * Format the file like this:
    
    **Format**
    NAME|CONTINENT|POPULATION|POPULATION_DENSITY

    **For Example**
  
    China|Asia|1339190000|139.5431469965489

	
	

.. code-block:: python

    class CountryCatalogue:
   
        def __init__(self, continent_file_name, country_file_name):

        def filter_countries_by_continent(self, continent_name):
	   
        def print_country_catalogue(self):
	   
        def find_country(self, country_name):
	   
        def delete_country(self, country_name):
	   
        def add_country(self, country_name, country_population, country_area, country_continent):
		
        def set_populationOfASelectedCountry(self, country_name, country_population):
			
        def save_country_catalogue(self, file_name):
	
        def find_country_largest_pop(self):
	
        def find_country_smallest_area(self):
	
        def find_most_populous_continent(self):
	
        def filter_countries_pop_density(self, lowerBound, upperBound):
	

Part 3
======

This part is just for making sure everything works. 

.. Warning::

    These links will work when the course website goes back up, For the time being, I have included a folder in the course content you download with these files. 

Make sure you have downloaded the files:

    * :download:`Continents <continent.txt>`
    * :download:`Countries <country.txt>`

.. Warning::

    It's probably a good call to **not** alter these files. You can, but when we test your code, we will test it using these files. 
	
Also, download this file:

    * :download:`main.py <main.py>`

.. Warning::

    Feel free to comment out certain tests for your purposes. Just note that it's not a good idea to change the main file to make your object work properly. I will test your code with this main.py script as is. 
	
    Also, just because your code passes the tests, that does **NOT** mean that your code is necessarily correct. 
		

Do not worry about dealing with exceptions. 

Do not worry about uppercase vs lowercase. Like, Canada vs. canada. You can pretend they are two separate countries.  	
		
What to submit
==============

* Your ``Country.py`` and ``CountryCatalogue.py`` classes. Do not submit the ``main.py`` part.
* If you used Colab, you probably have everything in one script. This is ok. 
* If you used PyCharm or Spyder, you may have them in different files. This is OK, just submit both.  

    * Make sure your **NAME** and **STUDENT NUMBER** appear in a comment at the top of the scripts.
    * Make sure it's *commented* and has *function headers*!!
    * Include a list of the people you worked with. Don't worry, this won't be used against anyone, I just want to make sure credit is given where it's due. 
    * Use proper variable names
  
General FAQ:
============
* I don't know how to do *X*.
    * OK, go to `google.ca <https://www.google.ca>`_ and type in *X*.
* It’s not working, therefore Python is broken!
    * Probably not; you’re very likely doing something wrong   
* Do I have enough comments?
    * I don't know, maybe? If you're looking at code and have to ask if you should comment it... just comment it. That said, don't write me a book.
* I know you told me to do it this way, but I did it another way, and I think my way is better.
    * Your way may be better, but I don’t care. Do it the way I told you.
* Can I work with my friend?
    * **YES!**
* I know our code looks the same, but we only worked together at a high level.
    * Cool. In fact, you can work together on a *low* level too for all I care. 
* I know I cheated, I know I know I was cheating, but I’m reeeeaaaaaaaaallllllly sorry [that I got caught]. Can we just ignore it this time?
    * You probably didn't do anything wrong. 
* If I submit it at 11:56pm, you’ll still mark it, right? I mean, commmmon!
    * No. 11:55pm and earlier is on time. Anything after 11:55pm is late. Anything late is not marked. It’s rather simple really.
* Moodle was totally broken, it’s not my fault it’s late.
    * Nice try.
* I accidentally submitted the wrong code. Here is the right code, but it’s late. But you can see that I submitted the wrong code on time! You’ll still accept it, right?
    * Do you think I was born yesterday? No.

