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

    It will be a lot easier to build your solutions on Colab and then copy/paste them into Kattis. 
    

14. Kattis sign up (be sure to set affiliation) 

    * Go to settings to do this
    * Also, you might want to set your default language to Python 3
    
15. https://open.kattis.com/problems/hello (Let's get that O in IO working)   

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/k1PK3CGOskA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   

16. https://open.kattis.com/problems/carrots (Let's now get the I in IO working)

    Although I give you a solution below, the actual task I want you to do for this step is to look at the code, read the comments, and try to figure out WTF is going on. Talk to each other. Make sure it makes sense. Take your time. Ask us questions. That's what this is all about.

    * Here is a solution with an explanation::
   
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
      
      
Back to Not Kattis
==================

17. Seriously, look at the above code and take your time to understand it. 

18. Go back to Colab and play around with the input function. Try different things with it. The best way to learn this stuff is to play around with the code and see what you can do with it. 

19. To make sure you get ``input``, write some code to ask the user for their first name. Then after that, write the code to ask the user for their last name. Then, after the 2nd input, print out the first name and then the last name. **Hint:** you'll probably need variables here. 
    

More Kattis Problems
====================
Do not worry if you do not get this far. 

Grab a scrap piece of paper to start scratching your ideas down on paper.

20. https://open.kattis.com/problems/r2 (IO might be tricky, but should be similar to above so definitely try to re-use the code)
21. https://open.kattis.com/problems/faktor (IO might be tricky, but should be similar to above)   
22. https://open.kattis.com/problems/ladder (Hope you remember your Gr 10 math... if not, good thing Google exists)
23. https://open.kattis.com/problems/planina (Looks like an INTEGER SEQUENCE (if only there was an *On-line encyclopedia*).




**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
