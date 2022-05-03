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


def calculate_total_charge(
        num_days: float, age: float, rental_code: str, odometer_start: float, odometer_finish: float
) -> float:
    """
    Calculate how much the renter needs to be charged based on the classification,
    the number of kms travelled and the age of the driver.

    @rtype: float
    @param num_days: Number of days the car was rented.
    @param age: Age of the driver.
    @param rental_code: The classification code (B ord D).
    @param odometer_start: Odometer when the renter took the car.
    @param odometer_finish: Odometer when the renter returned the car.
    @return: The amount to charge the renter.
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

age = int(input('Age: '))
classification = input('Classification Code: ')
number_of_days = int(input('Number of Days Rented: '))
starting_kms = float(input('Odometer reading at start: '))
ending_kms = float(input('Odometer reading at end: '))

print(age, type(age))
print(classification, type(classification))
print(number_of_days, type(number_of_days))
print(starting_kms, type(starting_kms))
print(ending_kms, type(ending_kms))

total_charge = calculate_total_charge(number_of_days, age, classification, starting_kms, ending_kms)

print('The total charge is: ' + str(total_charge))
