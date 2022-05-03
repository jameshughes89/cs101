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
