def test_function(expected, func, *args):
    result = func(*args)
    if result == expected:
        message = f"Function {func.__name__} on {args} passed."
    else:
        message = f"Function {func.__name__} on {args} FAILED --- expected {expected}, returned {result}."
    print(message)
