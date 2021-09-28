******
Lab #4
******

Before Kattis
=============


.. image:: ../img/carRental.png

A car rental place needs our help. They want a simple program to calculate how much a customer is to be charged based on their rental agreement, age, how far they drove, and how long they had the car. 

.. warning::
   
   I'm obviously aware that this is directly from class. Don't just copy/paste the solution. Take this as an opportunity to re-implement the solution. In fact, I will be very very happy if you have slightly different solutions than what I had. Use this as a place to work through what you understand in the course and figure out what you don't quite understand yet. Then, when you know what you don't know, ASK FOR HELP!!!!!!!!!!

**Rules:**

* We will get the customer's:
   * Age
   * Rental agreement classification code (B or D)
   * Number of days rented
   * Starting odometer reading
   * Ending odometer reading
* If the classification code is **B**
   * Base charge of $20.00/day
   * Plus $0.30 for every km driven
* If the classification is **D**
   * Base charge of $50.00/day
   * Plus $0.30 for every km driven above the 100km/day average allowance. 
* All renters under the age of 25 are charged an additional $10.00/day 
* Print out the final total cost

Kattis Problems
===============

If you finish the above task, go back and work on unsolved Kattis problems from previous labs. 

If you're sick of Kattis, check out `LeetCode <https://leetcode.com/problemset/all/>`_. Leet code is amazing, but it's less *programming competition* prep and more *coding interview* prep. 

Remember, here is the *magic* code we needed last week::
   
   data = input()       # Read a WHOLE, SINGLE line of input
   data = data.split()  # Split string into individual pieces
   a_var = int(data[0]) # Take string from data[X], convert it to int...   
   b_var = int(data[1]) # ... And store it in some variable

If you are done everything, feel free to work on the assignment. Just note that Lab time is **not** office hours and I will likely not provide support for assignment 1. 


**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
