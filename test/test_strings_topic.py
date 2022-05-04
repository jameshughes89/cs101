import io
import unittest
import unittest.mock

from src.strings_topic import character_is_in, vertical_print_for, vertical_print_while


class TestStringsTopic(unittest.TestCase):
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_while_empty_string_prints_nothing(self, mock_stdout):
        vertical_print_while("")
        expected = ""
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_while_hello_string_prints_correctly(self, mock_stdout):
        vertical_print_while("Hello")
        expected = "H\ne\nl\nl\no\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_for_empty_string_prints_nothing(self, mock_stdout):
        vertical_print_for("")
        expected = ""
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_for_hello_string_prints_correctly(self, mock_stdout):
        vertical_print_for("Hello")
        expected = "H\ne\nl\nl\no\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_character_is_in_a_in_empty_string_returns_false(self):
        self.assertFalse(character_is_in("a", ""))

    def test_character_is_in_empty_string_in_empty_string_returns_false(self):
        self.assertFalse(character_is_in("", ""))

    def test_character_is_in_empty_string_in_hello_string_returns_false(self):
        self.assertFalse(character_is_in("", "hello"))

    def test_character_is_in_no_matching_character_returns_false(self):
        self.assertFalse(character_is_in("a", "hello"))

    def test_character_is_in_first_character_match_returns_true(self):
        self.assertTrue(character_is_in("h", "hello"))

    def test_character_is_in_last_character_match_returns_true(self):
        self.assertTrue(character_is_in("o", "hello"))
