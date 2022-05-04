def vertical_print_while(a_string: str):
    """
    Print out a string vertically. In other words, print out a single character on each line.

    :param a_string: Some string to print out
    :type a_string String
    """
    character_index = 0
    while character_index < len(a_string):
        print(a_string[character_index])
        character_index += 1


def vertical_print_for(a_string: str):
    """
    Print out a string vertically. In other words, print out a single character on each line.

    :param a_string: Some string to print out
    :type a_string String
    """
    for char in a_string:
        print(char)


def character_is_in(needle: str, haystack: str) -> bool:
    """
    Search through a string to determine if a given character is contained within it. Returns True if the character is
    in the string and False otherwise.

    :param needle:  Character to look for
    :type needle: String
    :param haystack: String to search through
    :type haystack: String
    :return: True if the character is in the string, false otherwise
    :rtype: Boolean
    """
    for char in haystack:
        if char == needle:
            return True
    return False


# character_is_in tests
assert False == character_is_in("a", "")
assert False == character_is_in("", "")
assert False == character_is_in("", "hello")
assert False == character_is_in("a", "hello")
assert True == character_is_in("h", "hello")
assert True == character_is_in("o", "hello")
