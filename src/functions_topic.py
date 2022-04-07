def celsius_to_fahrenheit(temp_in_celsius):
    """
    Convert a temperature from Celsius units to Fahrenheit units.

    :param temp_in_celsius: The temperature in Celsius to be converted.
    :return: The temperature in Fahrenheit.
    """
    partial_conversion = temp_in_celsius * 9 / 5
    temp_in_fahrenheit = partial_conversion + 32
    return temp_in_fahrenheit


# Tests for celsius_to_fahrenheit function
assert 32 == celsius_to_fahrenheit(0)
assert -40 == celsius_to_fahrenheit(-40)
assert 86 == celsius_to_fahrenheit(30)
assert 89.6 == celsius_to_fahrenheit(32)
# To address precision issues, we can look for a sufficiently small difference between the expected and actual
assert 0.001 > abs(celsius_to_fahrenheit(37.7777) - 100)


def concatenate_strings(string1: str, string2: str) -> str:
    """
    Returns the concatenation of two strings.
    E.g.
        concatenate_strings("hello", "world") -> "helloworld"

    @rtype: str
    @param string1: First string of the concatenation
    @param string2: Second string of the concatenation
    @return: The concatenation of string1 and string2
    """
    concatenated = string1 + string2
    return concatenated


# Tests for the concatenate_strings method
assert "" == concatenate_strings("", "")
assert "ab" == concatenate_strings("a", "b")


def criss_cross_concatenation(string1: str, string2: str, string3: str, string4: str) -> str:
    """
    Returns the concatenation of the strings in the order of first third second fourth.
    E.g.
        criss_cross_concatenation("hello", "world", "CSCI", "161") -> "helloCSCIworld161"

    @rtype: str
    @param string1: First string of the concatenation
    @param string2: Second string of the concatenation (that should be the third one on output)
    @param string3: Third string of the concatenation (that should be the second one on the output)
    @param string4: Fourth string of the concatenation
    @return: The concatenation of string1 string3 string2 string4
    """
    first_third = concatenate_strings(string1, string3)
    second_fourth = concatenate_strings(string2, string4)
    first_third_second_fourth = concatenate_strings(first_third, second_fourth)
    return first_third_second_fourth


# Tests for the criss_cross_concatenation method
assert "" == criss_cross_concatenation("", "", "", "")
assert "acbd" == criss_cross_concatenation("a", "b", "c", "d")
