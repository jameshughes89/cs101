******************************************
Assignment #4: Playing with Objects is fun
******************************************

* **Worth**: 20%
* **DUE**: November 30th at 11:55pm; submitted on MOODLE.

.. Warning::

    On this assignment **you are allowed to work with others**. Peer learning and peer teaching are some of the best possible things you can do when learning something new. So feel free to work together. I don't even care if your code is identical. **BUT** be warned. You better understand what's going on. If not, you **will** fail the exam and probably the class. Don't be that person. 

* Learning Objectives
    * Starting from scratch 
    * Interpreting requirements correctly
    * File IO
    * Strings
    * Building objects
    * Working with objects
    * Lists
    * Complex data structures
    * Generalizing rules 
    * Testing code

.. image:: ../img/world.png

Now for another more engineering-ie assignment where we will build something. In fact, we're going to build our own objects from scratch. This may seem intimidating, but in reality, coding this way can often really simplify all of your problems. It's all about nice *encapsulation*. 

We're going to write a program that will use objects to store, search, remove, and filter data. Specifically, we're going to keep a record of some country details. 

.. Warning::

    The trick here is to really focus on the sub-problems. I have seen a lot of people on the previous assignments get overwhelmed and distracted by the bigger picture. It's not a bad idea to keep the big picture in mind, but here just focus on the small problems, one at at time. Everything will come together. 
   
Part 1
======

Make a Country Class. 

**Properties/attributes** we want country objects to have are:

* name: str
* population: int
* area: float
* continent: str

That's it. Those are the properties/attributes we want out country objects to have. Also, you don't have to worry about making them *private* here. If you do, great, if not, whatever. 

We're going to write some **methods** for our country object. We'll have:

* Constructor --- sets the instance's attributes. 
* *Getter* Methods
    * get_name
    * get_population
    * get_area
    * get_continent
* get_pop_density --- a method that calculates and returns the population density of a country (population divided by area)
* *Setter* Method
    * set_population
* __repr__ --- generate a string representation of the country instance. 
    "``name`` in ``continent``", so, for example: "China in Asia"

Your class should look like this, but with the functions filled in:	
   
.. code-block:: python

    class Country:
   
        def __init__(self, name, pop, area, continent):
	   
        def __repr__(self):
	   
        def set_population(self, pop):
	   
        def get_name(self):
	   
        def get_area(self):
	   
        def get_population(self):
	   
        def get_continent(self):
       	
        def get_pop_density(self):

.. Warning::

   Test that your Country objects work correctly. Test **THOROUGHLY**. Do **not** move on until you know everything here is working properly.

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
        * `Continents <http://people.stfx.ca/jhughes/cs161/data/continent.txt>`_
        * `Countries <http://people.stfx.ca/jhughes/cs161/data/country.txt>`_		
		
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

    * `Continents <http://people.stfx.ca/jhughes/cs161/data/continent.txt>`_
    * `Countries <http://people.stfx.ca/jhughes/cs161/data/country.txt>`_	

.. Warning::

    It's probably a good call to **not** alter these files. You can, but when we test your code, we will test it using these files. 
	
Also, download this file:

    * `main.py <http://people.stfx.ca/jhughes/cs161/data/main_py.zip>`_	

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

