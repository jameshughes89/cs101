import unittest

from car_rental_topic import (
    average_kms_per_day,
    calculate_total_charge,
    num_kms_above_average,
    total_kms,
)


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

    def test_calculate_total_charge_code_B_1_day_0_kms_over_25_returns_20(self):
        self.assertEqual(20, calculate_total_charge(1, 25, "B", 0, 0))

    def test_calculate_total_charge_code_B_1_day_0_kms_under_25_returns_30(self):
        self.assertEqual(30, calculate_total_charge(1, 24, "B", 0, 0))

    def test_calculate_total_charge_code_B_arbitrary_over_25_returns_correct_result(self):
        self.assertEqual(190, calculate_total_charge(2, 25, "B", 500, 1000))

    def test_calculate_total_charge_code_B_arbitrary_under_25_returns_correct_result(self):
        self.assertEqual(210, calculate_total_charge(2, 24, "B", 500, 1000))

    def test_calculate_total_charge_code_D_1_day_0_kms_over_25_returns_20(self):
        self.assertEqual(50, calculate_total_charge(1, 25, "D", 0, 0))

    def test_calculate_total_charge_code_D_1_day_0_kms_under_25_returns_30(self):
        self.assertEqual(60, calculate_total_charge(1, 24, "D", 0, 0))

    def test_calculate_total_charge_code_D_arbitrary_over_25_returns_correct_result(self):
        self.assertEqual(145, calculate_total_charge(2, 25, "D", 500, 1000))

    def test_calculate_total_charge_code_D_arbitrary_under_25_returns_correct_result(self):
        self.assertEqual(165, calculate_total_charge(2, 24, "D", 500, 1000))
