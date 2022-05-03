***********************
Putting Things Together
***********************

* What have we seen so far?

    * Values
    * Types
    * Variables
    * Print
    * Input
    * Functions
    * Booleans
    * Logic
    * If/Else

* Each of the individual topics may feel simple on their own
* The difficult part tends to be when putting these topics together to solve complex problems


Writing Bigger Programs
=======================

* There is no single correct way to write programs, but there are some strategies
* For now I recommend a bottom up, incremental approach

    #. Start with an empty function and have it return some arbitrary constant value (e.g., ``0``)
    #. Run the function and verify that it does what you expect
    #. Add one or two lines of code
    #. Run the function and verify that it does what you expect
    #. Repeat

* This incremental strategy is great because a lot of the problem solving you will be doing will be incremental
* Additionally, it helps you make sure everything is working along the way

    * If everything *was* working and you added two lines of code and suddenly it stops working, perhaps the issue is with the two new lines you wrote

* We would still want to write tests for our completed functions, but you may find it difficult to debug a whole complete function when compared to one or two lines of code


Car Rental
==========

.. image:: carRental.png

* Here we solve a bigger problem than we are used to, but we will follow the incremental approach
* In fact, we will take it to another extreme
* Instead of just writing a few lines of code, we will make each part a function we can test easily, regardless of how "simple" the part seems

**Problem**

A car rental place needs our help. They want a program to calculate how much a customer is to be charged based on their
rental agreement, age, how far they drove, and how long they had the car.

* We will get and record the customer's:

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
    * Plus $0.30 for every km driven above the 100km/day average allowance 
    
* All renters under the age of 25 are charged an additional $10.00/day


An Incremental Solution
-----------------------
   
**Step 1**

* Read the problem

**Step 2**

* Understand the problem

    * This cannot be understated --- this is a big part of solving any problem

* Half of the description is IO 
* The only beefy part of this is the calculation

    * But even then, we can break that down into smaller bits and pieces that we can solve
   
   
**Let's look at the requirements:**
   
* *If* the classification code is **B**

    * Base charge of $20.00/days
    * Plus $0.30 *for every km* driven

* *If* the classification is **D**

    * Base charge of $50.00/days
    * Plus $0.30 *for every km* driven *above* the 100km/day *average* allowance.


**What do we see?**

* We see ``if``\s, which know how to do
* We see that there is some math, which isn't too bad

    * We need to know the total kms
    * We need to know the average number of kms driven
    * Need to know how many kms above 100 we are


**Step 3:**

Based on this, I will write:

* Function to calculate the kms
* Function to calculate average kms
* Function to calculate the number of kms above the 100 allowance
* And finally, a function putting it all together to calculate the total charge

.. note::

    Understand that the example below is only one possible implementation of a solution to this problem. There is
    literally an infinite number of ways one could go about solving this problem.


Total Kilometers
^^^^^^^^^^^^^^^^

* A function to calculate the total number of kms

    * What do we know?

        * Odometer readings
   
.. code-block:: python
    :linenos:
   
    def total_kms(odometer_start: float, odometer_finish: float) -> float:
        """
        This function calculates the total number of kilometers driven based
        on starting and ending odometer readings.

        @rtype: float
        @param odometer_start: The number of kms the car had before renting
        @param odometer_finish: The number of kms the car had after rending
        @return: The total kms driven
        """

        return odometer_finish - odometer_start

    assert 0 == total_kms(0, 0)
    assert 100 == total_kms(0, 100)
    assert -100 == total_kms(100, 0)
    assert 100.5 == total_kms(100.5, 201)

* You may be thinking that turning this simple sub-problem (calculating the total kilometers) into a function is overkill
* Perhaps you are right
* But, it's also really straightforward to confirm correctness of this function
* It is solving an important sub-problem
* It is facilitating our incremental development approach
* Although the functionality and purpose of ``odometer_finish - odometer_start`` is by no means difficult to understand, ``total_kms`` is even clearer


Average Kilometers Per Day
^^^^^^^^^^^^^^^^^^^^^^^^^^

* A Function to calculate the daily average number of kms

    * What do we know?

        * We have a function to calculate the total kms
        * We also know the number of days the car was rented.

.. code-block:: python
    :linenos:
   
    def average_kms_per_day(num_days: float, num_kms: float) -> float:
        """
        Calculate the average number of kilometers driven per day
        over the rental period

        @rtype: float
        @param num_days: The total number of days the car was rented
        @param num_kms: The total number of kilometers driven during the rental period
        @return: The average number of kilometers driven per day
        """

        return num_kms / num_days


    assert 0 == average_kms_per_day(1, 0)
    assert 1 == average_kms_per_day(1, 1)
    assert -1 == average_kms_per_day(-1, 1)
    assert 0.5 == average_kms_per_day(3, 1.5)


Kilometers Above Allowable Average
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Now for something a little harder
* Number of kms over the daily average allowance
* What do we know?

    * Function to calculate the daily average
   
.. code-block:: python
    :linenos:
   
    def num_kms_above_average(avg_num_kms: float) -> float:
        """
        Calculates the number of kms the renter went over of their daily allowance.
        We will use the customer's average daily kms.

        @rtype: float
        @param avg_num_kms: average number of kms driven per day
        @return: The number of kms over 100 they went (return 0 if it's less than 100)
        """

        # If the average kms traveled is above 100,
        # return how much above, otherwise zero
        if avg_num_kms > 100:
            return avg_num_kms - 100
        else:
            return 0


    assert 0 == num_kms_above_average(100)
    assert 1 == num_kms_above_average(101)
    assert 0 == num_kms_above_average(99)
    assert 100 == num_kms_above_average(200)


.. note::

    If you were wondering why ``num_kms_above_average`` had the two ``return`` statements instead of having only one,
    good observation; however, having two vs. one is not any more or less correct --- it's simply different.

    Further, there is a good argument for making use of a constant instead of hard coding the ``100`` for the daily
    average limit. Perhaps something like ``AVERAGE_DAILY_LIMIT``. Or maybe have the function include another parameter
    for the limit as that would make it far more general.

    Remember, with these small differences discussed, one is not more correct than the other. There is literally an
    infinite number of ways one could go about solving this problems.


**Who thought that wasn't too bad?**
		
Now for the tough one... calculate the total cost. What do we know?
    * age
    * class
    * odometer readings
    * number of days
    * the above functions   
  
.. code-block:: python
    :linenos:
   
    def calculate_total_charge(num_days, age, code, odometer_start, odometer_finish):
        '''
        Calculate how much the renter needs to be charged based on the classification,
        the number of kms travelled and the age of the driver.

        :param num_days: Number of days the car was rented.
        :param age: Age of the driver.
        :param code: The classification code (B ord D).
        :param odometer_start: Odometer when the renter took the car.
        :param odometer_finish: Odometer when the renter returned the car.
        :return: The amount to charge the renter.
        '''

        # Setup a variable for our total charge
        total_charge = 0
        
        # Calculate the number of kilometres traveled.
        total_kms_traveled = total_kms(odometer_start, odometer_finish)

        # If B, $20/day + km charge of 0.30/km
        if code == 'B':
            total_charge = 20.00 * num_days + 0.30 * total_kms_traveled
        # If D, $50 base charge, + 0.30/km OVER 100km
        else:
            total_charge = 50.00 * num_days + 0.30 * num_kms_above_average(num_days, total_kms_traveled)

        # if they're young, add an additional $10/day charge.
        if age < 25:
            total_charge += (10 * num_days)

        # return the result
        return total_charge

**Hmm, defo was tricker, but still not too bad at all!**

Now just do the IO part, which we have done a bunch of times before

.. code-block:: python
    :linenos:
   
    age = int(input('Age: '))
    classification = input('Classification Code: ')
    number_of_days = int(input('Number of Days Rented: '))
    starting_kms = float(input('Odometer reading at start: '))
    ending_kms = float(input('Odometer reading at end: '))

    total_charge = calculate_total_charge(number_of_days, age, classification, starting_kms, ending_kms)

    print('The total charge is: ' + str(total_charge))


Let's try: `Google colab <https://colab.research.google.com/drive/1FRZ7MbPOdbGziwmxh9-PjaqsP91tRRkk?usp=sharing>`_.

.. admonition:: Activity
    :class: activity

    Think about how you would write this differently 
        * Would you use all the same functions?
        * Would you change how the functions worked?
        * Would you move where you called the functions?
        * Would you add additional functions?
        * Would you use constants? (say yes)

* So, why did I write it the way I did?
* Honestly, just *because*
* No other reason other than it was the way I wrote it
* What matters here is that it worked
* But I could write this so so so many other ways and still have it work 
* This is NORMAL
      
For next class
==============

* Read `chapter 7 of the text <http://openbookproject.net/thinkcs/python/english3e/iteration.html>`_


