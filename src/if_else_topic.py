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


def smush_version_2(a_number: float) -> float:
    """
    Returns half the value of the parameter a_number if the value is positive,
    otherwise, return the value of a_number.

    :rtype: float
    :param a_number: Some arbitrary number.
    :return: Half of a_number when it is positive, a_number when not positive.
    """
    if a_number > 0:
        return_value = a_number / 2
    else:
        return_value = a_number
    return return_value


# Tests for smush_version_2
assert 5 == smush_version_2(10)
assert -10 == smush_version_2(-10)
assert 0 == smush_version_2(0)


def smush_version_3(a_number: float) -> float:
    """
    Returns half the value of the parameter a_number if the value is positive,
    otherwise, return the value of a_number.

    :rtype: float
    :param a_number: Some arbitrary number.
    :return: Half of a_number when it is positive, a_number when not positive.
    """
    if a_number > 0:
        return a_number / 2
    else:
        return a_number


# Tests for smush_version_3
assert 5 == smush_version_3(10)
assert -10 == smush_version_3(-10)
assert 0 == smush_version_3(0)


def is_negative(a_number: float) -> bool:
    """
    Checks if the provided number is negative or not. Returns True if a_number
    is negative, False otherwise.

    :rtype: float
    :param a_number: Some arbitrary number.
    :return: True if a_number is negative, False otherwise.
    """
    if a_number < 0:
        return True  # Remember, once a return statement is run the function stops
    return False


assert False == is_negative(10)
assert True == is_negative(-10)
assert False == is_negative(0)


def is_negative_version_2(a_number: float) -> bool:
    """
    Checks if the provided number is negative or not. Returns True if a_number
    is negative, False otherwise.

    :rtype: float
    :param a_number: Some arbitrary number.
    :return: True if a_number is negative, False otherwise.
    """
    return a_number < 0


assert False == is_negative_version_2(10)
assert True == is_negative_version_2(-10)
assert False == is_negative_version_2(0)


def hail(n: float) -> float:
    """
    Hailstone Numbers. Return n/2 if n is even, otherwise return 3n+1.

    :rtype: float
    :param n: Some arbitrary number.
    :return: n/2 if n is even, 3n+1 when n is odd.
    """
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


# Tests for hail
assert 0 == hail(0)
assert 4 == hail(1)
assert 1 == hail(2)
assert -14 == hail(-5)


def letter_grade(percent_grade: float) -> str:
    """
    Calculate the letter grade associated with the provided percent grade.

    :rtype: str
    :param percent_grade: A grade as a percent
    :return: Letter grade for the provided percentage
    """
    letter_grade = ""
    if percent_grade >= 90:
        letter_grade = "A+"
    elif percent_grade >= 80:
        letter_grade = "A"
    elif percent_grade >= 70:
        letter_grade = "B"
    elif percent_grade >= 60:
        letter_grade = "C"
    elif percent_grade >= 50:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


# Test letter_grade
assert "A+" == letter_grade(90)
assert "A" == letter_grade(80)
assert "B" == letter_grade(70)
assert "C" == letter_grade(60)
assert "D" == letter_grade(50)
assert "F" == letter_grade(49)
