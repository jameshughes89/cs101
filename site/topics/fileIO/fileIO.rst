*******
File IO
*******

Getting data into Python
========================

* You now know a lot about how to *manipulate* data.
* But you probably want to manipulate *specific* data. *Your* data. Not toy examples.
* We need to learn about **File I/O**.
* I wont lie to you: file I/O is boring, painful, detail-oriented work.
* Fortunately, Python makes it less painful than just about any other language I've ever used.

Read/Write to a text file
=========================

* There are a bunch of ways to do it, but here's one.

>>> my_file = open('aFileName.txt', 'r')

* Done (many programming languages do NOT make it this easy)
* This assumes the file is in the working directory
* Take a wild guess what 'r' means

.. admonition:: Activity
    :class: activity

    1. Create a text in the working directory. If using Colab, you'll have to get one there. 
    2. Open it like the above
    3. Try using the methods ``.readline()`` and ``.read()``
   
* There are a lot of methods, these are just two.

* How about writing to a file? 

>>> my_other_file = open('anotherFileName.txt', 'w')

.. admonition:: Activity
    :class: activity

    Try to figure out how to ``write`` to this file. 


* When done with files...
* Listen up, this is a very very important thing
* Pay attention
* **We must close them!**
* Failing to do this can cause serious issues!!
    * Seriously, I've spent longer than I would like to admit in my life looking for bugs that were just a result of me not closing my files. 
   
* Fortunately it's easy to close them

>>> my_other_file.close()


Loading a CSV file
==================

* Regular text files are cool, but CSVs are a great way to format data. 

* CSV stands for "Comma Separated Values".
* The file is stored in plain text (you can read it with a text editor)
* Delivers what it promises.
* Each line of the file is one item.
* Within the line, each value associated with that item is in a comma-delimited field.
    * Some people will use tabs or other things, but commas are best. 
* For example, suppose I have recorded height, weight and IQ for 3 subjects::

    name, height, weight, IQ
    Subject 1, 170, 68, 100
    Subject 2, 182, 80, 110
    Subject 3, 155, 54, 105
   
* The first line is a *header*, explaining the values in each field. 
* Headers are *not* mandatory. Some CSVs have 'em, some don't.
* Good news: Python has a built-in library to read CSV files for you!
* In fact, we've seen this before::

    def load_asn1_data():
        """
        This function loads the file `starbucks.csv` and returns a LIST of
        latitudes and longitudes for North American Starbucks'.
        We'll talk about lists formally in class in a few lectures, but maybe
        you can start guessing how they work based on what you see here...
        """
	
        import csv
	
        reader = csv.reader(open('starbucks.csv', 'r'))
        locations = []
	
        for r in reader:
            locations.append( (r[0],r[1]))
		
        return locations

* How does the ``csv.reader`` work?

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/HUHqBtNWJo8" frameborder="0" allowfullscreen></iframe>
	
.. admonition:: Activity+
    :class: activity
	
    Figure out how it works. Download :download:`this csv file <airports.csv>` to your computer. **NOTE:** If using Colab, you'll have to upload it.
   
    Now write a function called ``load_airports()`` that loads this CSV file into a list. 

    Play with this list a bit and get a feel for how the data is organized.

.. admonition:: Activity+++
    :class: activity

    Now write a function ``get_name_from_code(airport_code, airport_list)`` that will return a string containing the full name of the airport with the code ``airport_code``. 

    The parameter ``airport_list`` should be the list you loaded using ``load_airports()``.


      .. raw:: html
	
		<iframe width="560" height="315" src="https://www.youtube.com/embed/9wunG22ivJ0" frameborder="0" allowfullscreen></iframe>
   
* Suppose you have some tabular data in Python that you want to save back in to a CSV

    >>> csv_out = csv.writer(open('yourFileName', 'w'))
    >>> csv_out.writerow(['First cell','Second cell', 'Third cell'])
    write as many rows as you need to... maybe in a loop?
   

* CSV files are popular because they're simple.
* You can, e.g., export any Excel spreadsheet as a CSV.
* If you have tabular data, this is a decent choice of format.
* If you don't have tabular data... this is an awful choice.


For next class
==============

* Read `chapter 15 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_  
* Read `chapter 16 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html>`_  

