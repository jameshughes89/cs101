import unittest

from car_rental_topic import total_kms, average_kms_per_day, num_kms_above_average


class TestFunctionsTopic(unittest.TestCase):
    def test_total_kms_difference_0_returns_0(self):
        self.assertEqual(0, total_kms(0, 0))

    def test_total_kms_difference_100_returns_100(self):
        self.assertEqual(100, total_kms(0, 100))

    def test_total_kms_difference_negative_100_returns_negative_100(self):
        self.assertEqual(-100, total_kms(100, 0))

    def test_average_kms_per_day_0_over_1_returns_zero(self):
        self.assertEqual(0, average_kms_per_day(1, 0))

    def test_average_kms_per_day_100_over_1_returns_100(self):
        self.assertEqual(100, average_kms_per_day(1, 100))

    def test_num_kms_above_average_200_avg_returns_100(self):
        self.assertEqual(100, num_kms_above_average(200))

    def test_num_kms_above_average_50_avg_returns_0(self):
        self.assertEqual(0, num_kms_above_average(50))


num_kms_above_average
