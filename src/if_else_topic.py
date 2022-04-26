def smush(a_number: float) -> float:
    """
    Returns half the value of the parameter a_number if the value is positive,
    otherwise, return the value of a_number.

    :rtype: float
    :param a_number: Some arbitrary number.
    :return: Half of a_number when it is positive, a_number when not positive.
    """
    return_value = a_number
    if a_number > 0:
        return_value = return_value / 2
    return return_value


# Tests for smush
assert 5 == smush(10)
assert -10 == smush(-10)
assert 0 == smush(0)
