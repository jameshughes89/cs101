***********
Hello World
***********

* Feel free to use your laptop if yo have it
* Ensure I have recorded your completion --- failure to do so will result in a grade of 0
* I strongly encourage you to work with others in the lab

    * When you get stuck, do me a favour and ask those sitting around you for help
    * I want people to get used to working together in the labs
    * Peer teaching and peer learning is super effective

.. note::

    To obtain full marks for the lab, you must:

        #. Have completed the pre-lab exercises
        #. Have been working on the lab content
        #. Demonstrate competency in the topics


Pre Lab Exercises
=================

.. warning::

    You must have completed the specified exercises prior to the start of the lab. If you have not come to lab prepared,
    you will be asked to leave and you will obtain a grade of 0 for the lab.


#. `Chapter 1 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/way_of_the_program.html#exercises>`_

    * 2
    * 4

#. `Chapter 2 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html#exercises>`_

    * 1
    * 5


Hello World
===========

#. Log onto your computer
#. Log into Colan

    * If you do not have a Google account, you can make one for the purpose of this course

#. Get *Hello World* working on Colab

    * If you are unsure of what this is, review :doc:`Topic 1 </topics/data-intro/intro>`


Refreshing What We Learned
==========================

#. Enter and run the following code

.. code-block:: python
    :linenos:

    a = 5
    a = a * 2


    * Have Python print out the type of ``a``

#. Enter and run the following code

.. code-block:: python
    :linenos:

    a = 5
    a = a * 2.5


    * Have Python print out the type of ``a``
    * Is this what you expected?


#. Complete the following

    * Make two variables and assign arbitrary numerical values to them
    * Add the variables together and assign the resulting value to a new, third variable
    * Print out the value of the third variable


Kattis
======

.. admonition:: Note
    :class: note

    You are not expected to complete all the Kattis problems. Just work on them until the time runs out. If you need
    help, ask those around you for help. If you're still stuck, ask us for help.

.. admonition:: Note
    :class: note

    It will be a lot easier to build your solutions on Colab and then copy/paste them into Kattis. 


#. Kattis sign up (be sure to set affiliation)

    * Go to settings to do this
    * Also, I highly recommend setting your default language to Python 3
    
#. https://open.kattis.com/problems/hello

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/k1PK3CGOskA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


#. https://open.kattis.com/problems/carrots

    * Although I provide a working solution below, the actual task I want you to do is to look at the code, read the comments, and try to figure out what is going on
    * Talk to each other
    * Make sure it makes sense
    * Take your time
    * Ask questions
    * That's what this is all about.

    .. code-block:: python
        :linenos:
   
        # This loads in the first line (it's of type STRING!)
        # For example, if we take the first sample input of --- 2 1
        # Then the contents of data after this line is complete is '2 1'
        data = input()

        # This is going to sadly be *magic* code at this stage. 
        # This line *splits* the string ('2 1' in this case)
        # into separate smaller strings. The split happens on space characters 
        # The result is a *list* of the split string (['2', '1'] in our example)
        # We then overwrite the contents of data with this result (['2', '1'])
        data = data.split()

        # Now data is a *list*. To access data from the list at a specific location
        # We just *index* the list at the desired location: data[location]
        # HOWEVER, computer scientists are weird and like to start counting at 0
        # So, when we say data[1], we are actually getting the string '1' from data
        # data[0] would give us '2' in this case (weird, I know, but deal with it)
        carrots = data[1]

        # Now we just print out what we stored in carrots
        print(carrots)
      
      
    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/wWG9eOrEW3Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    .. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/k1WWm-QiCZw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


#. https://open.kattis.com/problems/r2
#. https://open.kattis.com/problems/faktor
#. https://open.kattis.com/problems/ladder
#. https://open.kattis.com/problems/planina

**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
