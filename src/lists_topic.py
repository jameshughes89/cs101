def contains_while(needle, haystack) -> bool:
    """
    Linear search on a list. Return true if needle is found within haystack and false if it is not. Note that type
    hints are not included in the definition of the function as we can search for things of arbitrary types within
    a list containing a variety of arbitrary types.

    :param needle: Element to look for
    :type needle: Some arbitrary type
    :param haystack: List to search through
    :type haystack: A list of arbitrary types
    :return: True if needle is contained in haystack, false otherwise
    :rtype: Boolean
    """
    index = 0
    while index < len(haystack):
        if haystack[index] == needle:
            return True
        else:
            index += 1
    return False


# contains_while tests
assert False == contains_while("a", [])
assert False == contains_while("b", ["a", 1, 2.0, False])
assert True == contains_while("a", ["a", 1, 2.0, False])
assert True == contains_while(False, ["a", 1, 2.0, False])


def index_of_for(needle, haystack) -> int:
    """
    Linear search on a list. Return the index of the needle if it is found within haystack and -1 if it is not. Note
    that type hints are not included in the definition of the function as we can search for things of arbitrary types
    within a list containing a variety of arbitrary types.

    :param needle: Element to look for
    :type needle: Some arbitrary type
    :param haystack: List to search through
    :type haystack: A list of arbitrary types
    :return: Index of the needle within haystack if it is found, -1 otherwise
    :rtype: Integer
    """
    counter = 0
    for thing in haystack:
        if thing == needle:
            return counter
        else:
            counter += 1
    return -1


# index_of_for tests
assert -1 == index_of_for("a", [])
assert -1 == index_of_for("b", ["a", 1, 2.0, False])
assert 0 == index_of_for("a", ["a", 1, 2.0, False])
assert 3 == index_of_for(False, ["a", 1, 2.0, False])
