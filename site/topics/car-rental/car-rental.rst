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
* We know how to do this, so we will start here
* The other half of the description is the calculation

**Step 3**

* Chip away at the problem

.. note::

    Understand that the example below is only one possible implementation of a solution to this problem. There is
    literally an infinite number of ways one could go about solving this problem.


Input
^^^^^

.. code-block:: python
    :linenos:
    :emphasize-lines: 7

    age = int(input('Age: '))
    classification = input('Classification Code: ')
    number_of_days = int(input('Number of Days Rented: '))
    starting_kms = float(input('Odometer reading at start: '))
    ending_kms = float(input('Odometer reading at end: '))

    total_charge = # Some function to do the total charge calculation

    print('The total charge is: ' + str(total_charge))


.. note::

    In the above example, we would want to verify it is doing what we expect. Since user input is a little difficult to
    test with ``assert``, we can simply ``print`` out the data and confirm that it is doing what we expect. For example,
    the following code could be added to the above example.

    .. code-block:: python
        :linenos:

        print(age, type(age))
        print(classification, type(classification))
        print(number_of_days, type(number_of_days))
        print(starting_kms, type(starting_kms))
        print(ending_kms, type(ending_kms))


* The above example of reading user input seems to be sufficient for what we need; however, obviously we are far from solving the problem
* Line 7 is currently non-functional; it is simply a placeholder for the actual ``total_charge`` calculation

    * If you were to run the example code, it would not work since ``total_charge`` is currently not being assigned to anything

* In other words, we need to actually write some function to do the actual calculation for us

    * The calculation may seem intimidating, but let's take the same approach as above
    * We will write the code we can and leave comments for the parts we still need to tackle


Calculating The Total Charge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    def calculate_total_charge(some_number_of_parameters):

        # Set up a variable for our total charge
        total_charge = 0

        # Calculate the number of kilometres traveled.
        total_kms_traveled =

        # Calculate the average number of kilometers travelled per day
        average_kms =

        # Calculate the charge based on rental code
        if rental_code == 'B':
            # Base charge of $20.00/days + $0.30 for every km driven
        else:
            # Base charge of $50.00/days + $0.30 for every km driven above the 100km/day average allowance
            num_kms_above_allowance =

        # if they're under 25, add additional charge
        if something :

        # Return the final total charge
        return some_total_charge


* Although it may feel like this is a rather silly function so far, it did help us outline what we need to know in order to solve the problem

    * We need to know the total kilometers travelled
    * We need to know the average kms/day
    * We need to know the number of kms driven above the 100km/day average allowance
    * We need to do the actual rental agreement classification calculation
    * We need to add the extra charge for people under 25


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

        :rtype: float
        :param odometer_start: The number of kms the car had before renting
        :param odometer_finish: The number of kms the car had after rending
        :return: The total kms driven
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
        * We also know the number of days the car was rented

.. code-block:: python
    :linenos:
   
    def average_kms_per_day(num_days: float, num_kms: float) -> float:
        """
        Calculate the average number of kilometers driven per day
        over the rental period

        :rtype: float
        :param num_days: The total number of days the car was rented
        :param num_kms: The total number of kilometers driven during the rental period
        :return: The average number of kilometers driven per day
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

    * Average kms/day given the function ``average_kms_per_day`` we wrote
   
.. code-block:: python
    :linenos:
   
    def num_kms_above_average(avg_num_kms: float) -> float:
        """
        Calculates the number of kms the renter went over of their daily allowance.
        We will use the customer's average daily kms.

        :rtype: float
        :param avg_num_kms: average number of kms driven per day
        :return: The number of kms over 100 they went (return 0 if it's less than 100)
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


Revisit Calculating the Total Charge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* With the functions we wrote, solving the big ``calculate_total_charge`` becomes simpler
  
.. code-block:: python
    :linenos:
   
    def calculate_total_charge(num_days: float, age: float, rental_code: str, odometer_start: float, odometer_finish: float) -> float:
        """
        Calculate how much the renter needs to be charged based on the classification,
        the number of kms travelled and the age of the driver.

        :rtype: float
        :param num_days: Number of days the car was rented.
        :param age: Age of the driver.
        :param rental_code: The classification code (B ord D).
        :param odometer_start: Odometer when the renter took the car.
        :param odometer_finish: Odometer when the renter returned the car.
        :return: The amount to charge the renter.
        """
        # Set up a variable for our total charge
        total_charge = 0

        # Calculate the number of kilometres traveled.
        total_kms_traveled = total_kms(odometer_start, odometer_finish)

        # Calculate the average number of kilometers travelled per day
        average_kms = average_kms_per_day(num_days, total_kms_traveled)

        if rental_code == "B":
            total_charge = 20.00 * num_days + 0.30 * total_kms_traveled
        else:
            total_charge = 50.00 * num_days + 0.30 * num_kms_above_average(average_kms)

        # if they're under 25, add additional charge
        if age < 25:
            total_charge += 10 * num_days

        # Return the final total charge
        return total_charge


    assert 20 == calculate_total_charge(1, 30, "B", 0, 0)
    assert 50 == calculate_total_charge(1, 30, "D", 0, 0)
    assert 30 == calculate_total_charge(1, 20, "B", 0, 0)
    assert 60 == calculate_total_charge(1, 20, "D", 0, 0)
    assert 50 == calculate_total_charge(1, 30, "B", 0, 100)
    assert 50 == calculate_total_charge(1, 30, "D", 0, 100)
    assert 60 == calculate_total_charge(1, 20, "B", 0, 100)
    assert 60 == calculate_total_charge(1, 20, "D", 0, 100)
    assert 190 == calculate_total_charge(2, 30, "B", 0, 500)
    assert 145 == calculate_total_charge(2, 30, "D", 0, 500)
    assert 210 == calculate_total_charge(2, 20, "B", 0, 500)
    assert 165 == calculate_total_charge(2, 20, "D", 0, 500)


* Take the time to go over all the parts of this function
* If any part feels intimidating, slow down

    * The new functions were used to simplify much of the calculation
    * The ``if`` for the rental classification simply evaluates the corresponding cost calculation
    * The ``if`` for the age adds an additional $10/day

* Let's try: `Google colab <https://colab.research.google.com/drive/1FRZ7MbPOdbGziwmxh9-PjaqsP91tRRkk?usp=sharing>`_.

.. note::

    There was nothing stopping us from writing a function for the rental classification calculation or the age
    calculation. If you feel that would be better, then I would encourage you to do that. Again, assuming your
    implementation does what is required, it would not be any more or less correct than this implementation.


.. admonition:: Activity
    :class: activity

    Think about how you would write this differently

        * Would you use all the same functions?
        * Would you change how the functions worked?
        * Would you move where you called the functions?
        * Would you add additional functions?
        * Would you use constants? Where?

      
For Next Class
==============

* Read `Chapter 7 of the text <http://openbookproject.net/thinkcs/python/english3e/iteration.html>`_


