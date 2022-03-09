import pytest
from src.functions_topic import *


@pytest.mark.parametrize("string1, string2, expected",
                         [("", "", ""),
                          (" ", " ", "  "),
                          ("a", "b", "ab"),
                          ("Hello", "World", "HelloWorld")])
def test_absolute_value_returns_correct_value(string1, string2, expected):
    assert concatenate_strings(string1, string2) == expected
