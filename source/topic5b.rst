************************************
Topic #5b -- Putting Things Together
************************************

What have we seen so far?

* Values
* Types
* Variables
* Print
* Input
* Functions
* Booleans
* Logic
* If/Else

.. image:: ../img/carRental.png

A car rental place needs our help. They want a simple program to calculate how much a customer is to be charged based on their rental agreement, age, how far they drove, and how long they had the car. 


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
    * Plus $0.30 for every km driven above the 100km/day average allowance 
    
* All renters under the age of 25 are charged an additional $10.00/day because they hate young people
* Print out the final total cost

   
**Step 1**

* Freak out
   
   
**Step 2**
   
* Let's take a deep breath and break this problem down

* Half of the description is IO 
    * Let's save this for last because it's super easy
   
* The only beefy part of this is the calculation
    * Freak out again
    * Then realize we can break it down into bits and pieces that we can solve
   
   
**Let's look at the requirements:**
   
* *If* the classification code is B
    * Base charge of $20.00/days
    * Plus $0.30 *for every km* driven
* *If* the classification is D
    * Base charge of $50.00/days
    * Plus $0.30 *for every km* driven *above* the 100km/day *average* allowance.


**What do I see?**

* I see ``if`` statements there
    * Well I know how to do that
* I see that there is some math, which isn't too bad 
    * I can do simple math
* Looks like we need to know the total kms
    * I can do that
* Need to know the average number of kms driven
    * Easy stuff
* Need to know how many kms above 100 we are
    * So just figure out if a number is greater than 100?


**Step 3:**

Based on this, I will write:

* Function to calculate the kms
* Function to calculate average kms
* Function to calculate the number of kms above the 100 allowance
* Function to calculate the total charge

.. warning::
   
    THERE ARE LITERALLY INFINITE WAYS YOU COULD DO THIS. THIS IS JUST ONE!
   
   
Function to calculate the total number of kms. What do we know? 
    * Odometer readings!
   
.. code-block:: python
    :linenos:
   
    def total_kms(odometer_start, odometer_finish):
        '''
        This function calculates the total number of kilometers driven based
        based on starting and ending odometer readings.

        :param odometer_start: The number of kms the car had before renting
        :param odometer_finish: The number of kms the car had after rending
        :return: The total kms driven during the rental period
        '''
        
        return odometer_finish - odometer_start

**Who thought that was too easy?**


Function to calculate the daily average number of kms. What do we know? 
    * We have a function to calculate the total kms 
    * We also know the number of days the car was rented. 

.. code-block:: python
    :linenos:
   
    def average_kms_per_day(num_days, num_kms):
        '''
        Calculate the average number of kilometers driven per day
        over the rental period

        :param num_days: The total number of days the car was rented
        :param num_kms: The total number of kilometers driven during the rental period
        :return: The average number of kilometers driven per day
        '''
        
        return num_kms/num_days

**Who thought that was also too easy?**

Ok. Now for something harder... Number of kms over the daily average allowance. What do we know?
    * Function to calculate the daily average 
   
.. code-block:: python
    :linenos:
   
    def num_kms_above_average(num_days, num_kms):
        '''
        Calculates the number of kms the renter went over of their daily allowance.
        We will use the customer's average daily kms.

        :param num_days: Number of days the renter had the car
        :param num_kms: Number of kms the renter drove in total
        :return: The number of kms over 100 they went (return 0 if it's less than 100)
        '''
        
        # Calculate the number of kms traveled per day.
        kms_per_day = average_kms_per_day(num_days, num_kms)
        
        # If the average kms traveled is above 100, 
        # return how much above
        if kms_per_day  > 100:
            return kms_per_day - 100
        else:
            return 0
		 
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
        :param odometer_finish: Odomoter when the renter returned the car.
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

        # if they're young, screw-em with an additional $10/day charge.
        if age < 25:
            total_charge += (10 * num_days)

        # return the result
        return total_charge

**Hmm, defo was tricker, but still not too bad at all!**

Now just do the IO part, which is easy

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


