import io
import unittest
import unittest.mock

from src.loops_topic import factorial, int_sum, int_sum_print, sum_even_numbers


class LoopsTopicTest(unittest.TestCase):
    def test_factorial_0_returns_1(self):
        self.assertEqual(1, factorial(0))

    def test_factorial_1_returns_1(self):
        self.assertEqual(1, factorial(1))

    def test_factorial_10_returns_correct_number(self):
        self.assertEqual(3628800, factorial(10))

    def test_int_sum_0_returns_0(self):
        self.assertEqual(0, int_sum(0))

    def test_int_sum_1_returns_1(self):
        self.assertEqual(1, int_sum(1))

    def test_int_sum_10_returns_55(self):
        self.assertEqual(55, int_sum(10))

    def test_int_sum_negative_1_returns_0(self):
        self.assertEqual(0, int_sum(-1))

    def test_int_sum_print_0_returns_0(self):
        self.assertEqual(0, int_sum_print(0))

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_int_sum_print_0_prints_correct_string(self, mock_stdout):
        int_sum_print(0)
        expected = "0\t0 -> 0\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_int_sum_print_1_returns_1(self):
        self.assertEqual(1, int_sum_print(1))

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_int_sum_print_1_prints_correct_string(self, mock_stdout):
        int_sum_print(1)
        expected = "0\t0 -> 0\n1\t0 -> 1\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_int_sum_print_10_returns_55(self):
        self.assertEqual(55, int_sum_print(10))

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_int_sum_print_10_prints_correct_string(self, mock_stdout):
        int_sum_print(10)
        expected = (
            "0\t0 -> 0\n"
            "1\t0 -> 1\n"
            "2\t1 -> 3\n"
            "3\t3 -> 6\n"
            "4\t6 -> 10\n"
            "5\t10 -> 15\n"
            "6\t15 -> 21\n"
            "7\t21 -> 28\n"
            "8\t28 -> 36\n"
            "9\t36 -> 45\n"
            "10\t45 -> 55\n"
        )
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_int_sum_print_negative_1_returns_0(self):
        self.assertEqual(0, int_sum_print(-1))

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_int_sum_print_negative_1_prints_nothing(self, mock_stdout):
        int_sum_print(-1)
        expected = ""
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_sum_even_numbers_0_returns_0(self):
        self.assertEqual(0, sum_even_numbers(0))

    def test_sum_even_numbers_1_returns_0(self):
        self.assertEqual(0, sum_even_numbers(1))

    def test_sum_even_numbers_10_returns_correct_number(self):
        self.assertEqual(30, sum_even_numbers(10))

    def test_sum_even_numbers_negative_1_returns_0(self):
        self.assertEqual(0, sum_even_numbers(-1))
