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
            # As soon as the needle has been found, return True
            return True
    # If the loop ever finishes, that means we never found needle
    return False


# character_is_in tests
assert False == character_is_in("a", "")
assert False == character_is_in("", "")
assert False == character_is_in("", "hello")
assert False == character_is_in("a", "hello")
assert True == character_is_in("h", "hello")
assert True == character_is_in("o", "hello")


def character_is_at(needle: str, haystack: str) -> int:
    """
    Search through a string to determine if a given character is contained within it. Returns the index of the first
    occurence of the character if it exists, return -1 if the character does not exist in the string.

    :param needle:  Character to look for
    :type needle: String
    :param haystack: String to search through
    :type haystack: String
    :return: Index of the first occurrence of the character, or -1 if the character does not exist within the string
    :rtype: Integer
    """
    index = 0
    while index < len(haystack):
        if haystack[index] == needle:
            # As soon as the needle has been found, return the index
            return index
        else:
            # If we didn't find the needle, keep looking
            index += 1
    # If the loop ever finishes, that means we never found needle
    return -1


# character_is_at tests
assert -1 == character_is_at("a", "")
assert -1 == character_is_at("", "")
assert -1 == character_is_at("", "hello")
assert -1 == character_is_at("a", "hello")
assert 0 == character_is_at("h", "hello")
assert 4 == character_is_at("o", "hello")
assert 2 == character_is_at("l", "hello")
