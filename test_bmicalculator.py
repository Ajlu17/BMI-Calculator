import math
import unittest

from bmicalculator import calculate_bmi


class CalculateBmiTests(unittest.TestCase):
    def test_calculates_bmi_from_imperial_measurements(self):
        self.assertAlmostEqual(calculate_bmi(150, 5, 10), 21.52, places=2)

    def test_rejects_non_positive_weight(self):
        with self.assertRaisesRegex(ValueError, "Weight must be greater than 0"):
            calculate_bmi(0, 5, 10)

    def test_rejects_invalid_inches(self):
        with self.assertRaisesRegex(ValueError, "less than 12"):
            calculate_bmi(150, 5, 12)

    def test_rejects_non_finite_values(self):
        with self.assertRaisesRegex(ValueError, "finite numbers"):
            calculate_bmi(math.inf, 5, 10)

    def test_rejects_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be greater than 0"):
            calculate_bmi(150, 0, 0)


if __name__ == "__main__":
    unittest.main()
