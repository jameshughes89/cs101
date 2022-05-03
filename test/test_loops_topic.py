import unittest

from src.loops_topic import (
    factorial
)


class TestLoopsTopic(unittest.TestCase):

    def test_factorial_0_returns_1(self):
        self.assertEqual(1, factorial(0))

    def test_factorial_1_returns_1(self):
        self.assertEqual(1, factorial(1))

    def test_factorial_10_returns_correct_number(self):
        self.assertEqual(3628800, factorial(10))
        