def total_kms(odometer_start, odometer_finish):
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
