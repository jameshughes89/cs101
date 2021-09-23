******
Lab #3
******

Before Kattis
=============


1. Write a function that will take a grade between 0 - 100 and have it ``return`` either 'FAIL' ``if`` the grade is < 50 or 'PASS' otherwise. 

2. Write some code to take ``input`` for a grade between 0 - 100. Store this in some variable. 

3. Call the function we wrote and give it the inputted value. 

4. ``print`` out "A grade of *X* means *Y*", where *X* is the inputted grade between 0 - 100 and *Y* is the FAIL/PASS returned by the function. Ex. if 89 was inputted, "A grade of 89 means PASS".

5. Run this code a few times for fun. See if you can break it. 

6. Let's change our function a little. Make it so it can ``return`` the letter grade (0 - 50 -> F, 50 - 60 -> D, 60 - 70 -> C, 70 - 80 -> B, 80 - 90 -> A, 90 - 100 -> A+).

7. Do you know what to expect when you run your code again? Run your code. Did it do what you expected?

.. warning::
   
   If this scares you, go back and look at the lecture notes. All the info you need is in there. BUT, if you really do get stuck, ASK FOR HELP! Ask someone next to you, ask a TA, ask me. 

Kattis Problems
===============

Remember, here is the *magic* code we needed last week::
   
   data = input()       # Read a WHOLE, SINGLE line of input
   data = data.split()  # Split string into individual pieces
   a_var = int(data[0]) # Take string from data[X], convert it to int...   
   b_var = int(data[1]) # ... And store it in some variable

.. warning::
   
   The above will only work for certain situations, so you will need to hack this to make it work for specific cases!!!!!!!!!!!!!


1. https://open.kattis.com/problems/quadrant 
2. https://open.kattis.com/problems/judgingmoose
3. https://open.kattis.com/problems/twostones (Slow down and THINK)
4. https://open.kattis.com/problems/spavanac (kinda' tricky)
5. https://open.kattis.com/problems/cetvrta (kinda' annoying)

6. https://open.kattis.com/problems/bus (seems like a sequence again... can we figure this one out on our own?)



**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
