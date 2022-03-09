import pytest
from src.functions_topic import *


def test_concatenate_strings_empty_strings_returns_empty_string():
    assert "" == concatenate_strings("", "")


def test_concatenate_strings_returns_contatenated_strings():
    assert "ab" == concatenate_strings("a", "b")


def test_criss_cross_concatenation_empty_strings_returns_empty_string():
    assert "" == criss_cross_concatenation("", "", "", "")


def test_criss_cross_concatenation_returns_contatenated_strings_in_correct_order():
    assert "acbd" == criss_cross_concatenation("a", "b", "c", "d")
