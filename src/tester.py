def test_function(expected, func, *args):
    """
    This function tests a provided function and checks if the result of the function on the provided
    parameters/arguments matches what was expected. The function prints a message indicating pass/fail.

    @rtype: NoneType
    @param expected: What the correct output is for the provided function and parameters/arguments
    @param func: The function under test
    @param args: The parameters/arguments being provided to the function under test
    @return: none
    """
    result = func(*args)
    if result == expected:
        message = f"Function {func.__name__} on {args} passed."
    else:
        message = f"Function {func.__name__} on {args} FAILED --- expected {expected}, returned {result}."
    print(message)
