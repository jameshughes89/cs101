import unittest

from car_rental_topic import total_kms


class TestFunctionsTopic(unittest.TestCase):
    def test_total_kms_difference_0_returns_0(self):
        self.assertEqual(0, total_kms(0, 0))

    def test_total_kms_difference_100_returns_100(self):
        self.assertEqual(100, total_kms(0, 100))

    def test_total_kms_difference_negative_100_returns_negative_100(self):
        self.assertEqual(-100, total_kms(100, 0))
