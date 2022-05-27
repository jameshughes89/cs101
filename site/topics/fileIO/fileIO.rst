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


* Note that there are many more methods available beyond ``.readline()`` and ``.read()``, but these will likely be the ones you use the most

    * ``read`` reads the entire contents of the file
    * ``readline`` reads a single line from the file

* It is also important to ``.close()`` the file once you are done using it in Python


Writing to a Text File
----------------------

* Writing to a text file is similarly simple

.. code-block:: python
    :linenos:

    my_other_file = open("anotherFileName.txt", "w")


* Unlike reading however, the file does not need to exist
* Python will create a new file with the name ``"anotherFileName.txt"``

* The most commonly used methods you will likely use when writing to a file will be ``.write(text)`` and ``.writelines(listOfText)``

    * ``write`` will write the provided text to the file
    * ``writelines`` will write multiple lines of text to a file based on a list of strings --- each string in the list will be its own line


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
    :emphasize-lines: 13

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


* The emphasized line with the ``for`` loop is the trick to reading data from the csv reader
* When using the ``for`` loop, we read one row at a time from the file

    * The file is like a collection of rows
    * So, for each *row* in the *collection of rows*

* Here, the variable ``row`` will store a reference to the row's data in the form of a list, where each element in the list is from a different column


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/HUHqBtNWJo8" frameborder="0" allowfullscreen></iframe>


.. admonition:: Activity
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

    * This is similar to how the data is read in as a list

* With a csv writer, there are two important methods for us to know

    * ``writerow``, which was discussed above
    * ``writerows``, which takes a list of lists to write a large block of data


For Next Class
==============

* Read `Chapter 19 of the text <http://openbookproject.net/thinkcs/python/english3e/exceptions.html>`_


