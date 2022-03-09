import pytest
from src.functions_topic import *


@pytest.mark.parametrize("string1, string2, expected",
                         [("", "", ""),
                          (" ", " ", "  "),
                          ("a", "b", "ab"),
                          ("Hello", "World", "HelloWorld")])
def test_concatenate_strings_returns_concatenated_string(string1, string2, expected):
    assert concatenate_strings(string1, string2) == expected


@pytest.mark.parametrize("string1, string2, string3, string4, expected",
                         [("", "", "", "", ""),
                          (" ", " ", " ", " ", "    "),
                          ("a", "b", "c", "d", "acbd"),
                          ("This", "Is", "A", "Test", "ThisAIsTest")])
def test_criss_cross_concatenation_returns_concatenated_string_in_correct_order(string1, string2, string3, string4,
                                                                                expected):
    assert criss_cross_concatenation(string1, string2, string3, string4) == expected
