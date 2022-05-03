import io
import unittest
import unittest.mock

from src.strings_topic import vertical_print_for, vertical_print_while


class TestStringsTopic(unittest.TestCase):
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_while_empty_string_prints_nothing(self, mock_stdout):
        vertical_print_while("")
        expected = ""
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_while_hello_string_prints_nothing(self, mock_stdout):
        vertical_print_while("Hello")
        expected = "H\ne\nl\nl\no\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_for_empty_string_prints_nothing(self, mock_stdout):
        vertical_print_for("")
        expected = ""
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_vertical_print_for_hello_string_prints_nothing(self, mock_stdout):
        vertical_print_for("Hello")
        expected = "H\ne\nl\nl\no\n"
        self.assertEqual(expected, mock_stdout.getvalue())
