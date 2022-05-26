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


Comma Seperated Values (CSV)
============================

* CSV files are are a popular file format for tabular data

    * Data that can be stored in a table
    * Think of rows and columns of data, like in a spreadsheet

* CSV files are stored in plain text, but values are seperated with commas

    * You may come across CSV files that use tabs or spaces to separate data

* They can be read in a simple text editor, or even in a spreadsheet program where it will format the data nicely

    * In fact, you can typically save data from a spreadsheet into a CSV file

* An example of data in a CSV is as follows

.. code-block:: python
    :linenos:

    name, height, weight, IQ
    Subject 1, 170, 68, 100
    Subject 2, 182, 80, 110
    Subject 3, 155, 54, 105


* The above example can be represented in a table as follows

.. list-table:: CSV Viewed as a Table
   :widths: 50 25 25 25
   :header-rows: 1

    * - name
      - height
      - weight
      - IQ
    * - Subject 1
      - 170
      - 68
      - 100
    * - Subject 2
      - 182
      - 80
      - 110
    * - Subject 3
      - 155
      - 54
      - 105


* The first line in the example CSV is a *header*, which explains the values in each column

    * You do not need these, some CSV files have them, some don't


Reading a CSV File
------------------

* Python has a built-in library to help make reading CSV files simple
* In fact, you have already seen this in the Starbucks Density assignment

.. code-block:: python
    :linenos:

    def load_starbucks_data(file_name: str) -> list:

        import csv

        # Open the Starbucks file specified by file_name
        starbucks_file = open(file_name, "r")
        starbucks_file_reader = csv.reader(starbucks_file)

        # Create an empty list that the Starbucks location tuples will be added to
        starbucks_locations = []

        # For each row in the file, create a tuple of the lat/lon pair and add it to the list
        for row in starbucks_file_reader:
            location_tuple = (float(row[0]), float(row[1]))
            starbucks_locations.append(location_tuple)

        starbucks_file.close()
        return starbucks_locations


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/HUHqBtNWJo8" frameborder="0" allowfullscreen></iframe>


.. admonition:: Activity+
    :class: activity

    #. Download :download:`this csv file <airports.csv>` to your computer and then upload it to Colab.
    #. Write a function called ``load_airports()`` that loads this CSV file into a list and returns the list.

        * Use ``load_starbucks_data`` as a reference

    #. Play around with the data a little to get a feel for how the information is stored in the list.


.. admonition:: Activity
    :class: activity

    Write a function ``get_name_from_code(airport_code, airport_list)`` that will return a string containing the full
    name of the airport with the corresponding ``airport_code``. The parameter ``airport_list`` should be the list you
    loaded using ``load_airports()``.

    If your function made use of a linear search, can you think of a way to alter ``get_name_from_code`` and
    ``load_airports`` such that you do not need a linear search?

    .. raw:: html
	
        <iframe width="560" height="315" src="https://www.youtube.com/embed/9wunG22ivJ0" frameborder="0" allowfullscreen></iframe>


Writing to a CSV File
---------------------

* If we have large amounts of tabular data in our program we want to save to a file, we can write to a CSV file

.. code-block:: python
    :linenos:

    # Create a file to write to
    out_file = open("nameOfOutputFile.csv", "w")
    csv_out_file = csv.writer(out_file)

    # Write a row to the file
    csv_out_file.writerow(['First cell','Second cell', 'Third cell'])


* In the above example, notice that all the data for the row is contained within a list



For next class
==============

* Read `chapter 15 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html>`_  
* Read `chapter 16 of the text <http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html>`_  

