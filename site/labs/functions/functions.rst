*********
Functions
*********

* Feel free to use your laptop if you have it
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

#. `Chapter 2 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/variables_expressions_statements.html#exercises>`_

    * 5 **but** have it in a function that returns the result

#. `Chapter 4 exercise(s) <http://openbookproject.net/thinkcs/python/english3e/functions.html#exercises>`_

    * 8


Before Kattis
=============

* :doc:`If you forget how to do the function related stuff, go back to the class notes </topics/functions/functions>`

#. Write a function called ``add_five_print(some_integer)``

    * The function will take one parameter ``some_integer``
    * The function adds five to the parameter and ``print``\s out the result
    * The function will not return anything
    * Call the function a few times to verify that it works properly

    .. code-block:: python
        :linenos:

        def add_five_print(some_integer):
            # stuff goes here


#. Write a function called ``add_two_numbers_print(some_integer, some_other_integer)``

    * The function will take two parameters ``some_integer`` and  ``some_other_integer``
    * The function will calculate their sum and ``print`` out the result
    * The function will not return anything
    * Call the function a few times to verify that it works properly

    .. code-block:: python
        :linenos:

        def add_two_numbers_print(some_integer, some_other_integer):
            # stuff goes here


#. Write a function called ``add_two_numbers_return(some_integer, some_other_integer)``

    * The function will take two parameters ``some_integer`` and  ``some_other_integer``
    * The function will calculate their sum
    * The function will ``return`` the result
    * Call the function a few times to verify that it works properly


#. Run the following code and take note of the output

    .. code-block:: python
        :linenos:

        result = add_two_numbers_return(4, 5)
        print(result)


#. Run the following code and take note of the output

    .. code-block:: python
        :linenos:

        result = add_two_numbers_print(4, 5)
        print(result)


#. Why do these two functions behave differently when called?

    * Take note of when and where ``print`` is called

        
7. Write a function called ``this_is_tough`` that takes four integers as parameters. This function will ultimately add up the four integers and *return* the result. **HOWEVER**, inside this function you are **not** allowed to use the addition operator (or any arithmetic trick to do addition, like, ``5 - (-1*6)``), you are required to use the ``add_two_nums_return`` written above. You may **not** use ``print`` inside this function (use ``return``). A big hint: You will likely want to call the ``add_two_nums_return`` function a total of 3 times. Test that it works with the following code. 
  
    .. code-block:: python
        
        c = this_is_tough(3, 4, 6, 7)
        print(c)



Kattis Problems
===============

The problems below are 

Remember, here is *magic* code we needed last week::
   
    data = input()       # Read a WHOLE, SINGLE line of input
    data = data.split()  # Split string into individual pieces
    a_var = int(data[0]) # Take string from data[X], convert it to int...   
    b_var = int(data[1]) # ... And store it in some variable

.. warning::
   
    The above will only work for certain situations, so you will need to hack this to make it work for specific cases!!!!!!!!!!!!!

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/wWG9eOrEW3Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/k1WWm-QiCZw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> 
 

Grab a scrap piece of paper to start scratching your ideas down on paper. Paper and pencil is where a lot of **programming** happens. 

Skip any of the following problems if you did them already. 

8. https://open.kattis.com/problems/hello 
9. https://open.kattis.com/problems/carrots 
10. https://open.kattis.com/problems/r2
11. https://open.kattis.com/problems/faktor (This one is kinda' a brain teaser. It requires the simplest of math, but it's not trivial.)
12. https://open.kattis.com/problems/ladder (Hope you remember your Gr 10 math... if not, good thing Google exists)
13. https://open.kattis.com/problems/planina (Looks like an INTEGER SEQUENCE (if only there was an *On-line encyclopedia*).

14. `Go to Kattis and sort the problems by difficulty <https://open.kattis.com/problems?order=problem_difficulty>`_. Read them, understand the problem, then see if you can figure any out. Most you can't yet, but still see what you can do and what you CAN'T.  Try to figure out *why* you can't.  

**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
