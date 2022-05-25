*******
File IO
*******

* We know how to read input from a user
* We know how to store data in variables and lists
* We know how to manipulate data
* The trouble is, if we have large amounts of data, inputting data with ``input`` is not workable
* Fortunately an easy way to address this is reading data from a file

Text Files
==========

* Test files are great way to store textual data
* They typically have the file extension ".txt", but the actual extension doesn't really matter
* Most of what we are about to see will work on many different file types too (not just text files)


Reading from a Text File
------------------------

* There are a few ways to open and read from a file, but the easiest is as follows

.. code-block:: python
    :linenos:

    my_file = open("someFileName.txt", "r")


* The above example opens up a file named ``"someFileName.txt"`` in read only mode (``"r"``)

    * This assumes that the file being opened is in the current working directory

* A reference to the file is stored in the variable ``my_file``

.. admonition:: Activity
    :class: activity

    #. Create a text file somewhere on your computer (perhaps Desktop for ease).
    #. Upload the file to Colab.
    #. Open your file like in the above example, but with your proper file name.
    #. Try using the methods ``.readline()`` and ``.read()``.
    #. See if you can figure out how to re-read from the file after you already read the full contents.


* Note that there are many more methods available beyond ``.readline()`` and ``.read()``
* It is also good to ``.close()`` the file once you are done using it in Python


Writing to a Text File
----------------------

* Writing to a text file is similarly simple

.. code-block:: python
    :linenos:

    my_other_file = open("anotherFileName.txt", "w")


* Unlike reading however, the file does not need to exist
* Python will create a new file with the name ``"anotherFileName.txt"``

.. admonition:: Activity
    :class: activity

    #. Open some file in write only mode (``"w"``) in Python with a name of your choice.
    #. Use the ``.write()`` method to write contents to the file.
    #. Once you are done writing to the file, use the ``.close()`` method to close the file.
    #. Open the file you just created in some text editor and confirm that it matches what you wrote.


.. warning::

    It is very important to ``.close()`` your files when you are done with them, especially when writing to a file.
    Based on how Python writes to files, the contents you write are not sent to the file right away. Instead, it goes to
    something called a *buffer* that periodically writes to the file. If you fail to ``.close()`` your file, there is a
    chance that the buffer never finished writing to the file before the program terminated. When you ``.close()`` the
    file, it *flushes the buffer*, meaning that anything left in the buffer will be written to the file.


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

