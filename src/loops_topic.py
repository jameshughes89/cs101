def factorial(n: int) -> int:
    """
    Calculate factorial of n.

    :param n:   Number to calculate factorial of
    :type n:    Integer
    :return:    The factorial of n
    :rtype:     Integer
    """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


# Test trace_me_by_hand
assert 1 == factorial(0)
assert 1 == factorial(1)
assert 3628800 == factorial(10)


def int_sum(n: int) -> int:
    """
    Returns the sum of all numbers between 0 and n inclusively (be sure to include the value of n in the sum)

    :param n: Number to sum to
    :type n: Integer
    :return: The sum of all numbers between 0 and n inclusively
    :rtype: Integer
    """
    current_integer = 0
    running_total = 0
    while current_integer <= n:
        running_total += current_integer
        current_integer += 1
    return running_total


assert 0 == int_sum(0)
assert 1 == int_sum(1)
assert 55 == int_sum(10)
assert 0 == int_sum(-1)
