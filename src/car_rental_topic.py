def total_kms(odometer_start: float, odometer_finish: float) -> float:
    """
    This function calculates the total number of kilometers driven based
    on starting and ending odometer readings.

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
