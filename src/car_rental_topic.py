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
