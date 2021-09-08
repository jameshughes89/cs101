******
Lab #2
******

Remember, the point of the lab is **not** to complete the tasks. The point of the labs is to understand why the code you have written does what it does. Do not rush through the steps. Take your time and understand everything we are doing. The understanding is important, **not** just knocking off the tasks. 

Before Kattis
=============

1. If you missed the first lab, go complete steps 10 -- 16 in lab 1. 

**NOTE:**  :doc:`If you forget how to do the function stuff, go back to the class notes. </topic3>`

2. Write a **function** called ``add_five_print`` that takes one integer as a parameter, adds five to it, and then prints out the result. Call the function to verify its correctness. You **MUST** do this with a function. Below I have given you the code you need to start writing your function. 

    .. code-block:: python
   
        def add_five_print(aNum):
            # stuff goes here

3. Write a **function** called ``add_two_nums_print`` that takes two integers as parameters, adds them together, and then prints out the result. Call the function to verify its correctness. You **MUST** do this with a function. Below is the code you can use to call the function and test it after you have written/defined the function. 

    .. code-block:: python
    
        add_two_nums_print(4, 5)

4. Write a **function** called ``add_three_nums_print`` that takes three integers as parameters, adds them together, and then prints out the result. Call the function to verify its correctness. You **MUST** do this with a function.

5. Write a **function** called ``add_two_nums_return`` that takes two integers as parameters, adds them together, and then *returns* the result. Effectively this will be identical to ``add_two_nums_print``, but replace the ``print`` inside the function (in addition to the one in the name of the function) with ``return``. Run the following code to verify its correctness. 

    .. code-block:: python
   
        a = add_two_nums_return(4, 5)
        print(a)

6. Call the function ``add_two_nums_print`` you wrote in step 3 with the below code. What do you notice? See if you can hack around a little to figure out the difference between ``print`` and ``return`` (there's a HUGE difference). Take your time on this one. 

    .. code-block:: python
        
        b = add_two_nums_print(4, 5)
        print(b)
        
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

.. warning::
   
    If you are in the online section, you **must** submit the .py (python scripts), not the .ipynb (notebook files). To get the python scripts from Colab, simply select *File* and in te dropdown menue, hit *Download .py*. 
