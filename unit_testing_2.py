import math
import unittest

def calculate_mean(data):
    """
    Calculate the mean (average) of the numerical data.

    Parameters:
    data (list): List of numerical data.

    Returns:
    float: Mean value.
    """
    if not data:
        raise ValueError("The input list is empty.")
    return sum(data) / len(data)

def calculate_median(data):
    """
    Calculate the median of the numerical data.

    Parameters:
    data (list): List of numerical data.

    Returns:
    float: Median value.
    """
    if not data:
        raise ValueError("The input list is empty.")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]

def calculate_standard_deviation(data):
    """
    Calculate the standard deviation of the numerical data.

    Parameters:
    data (list): List of numerical data.

    Returns:
    float: Standard deviation value.
    """
    if not data:
        raise ValueError("The input list is empty.")
    mean = calculate_mean(data)
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    return math.sqrt(squared_diff_sum / len(data))

# Unit tests
class TestStatisticalCalculations(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(calculate_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_mean([2, 2, 2, 2, 2]), 2.0)

    def test_median(self):
        self.assertEqual(calculate_median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5, 6]), 3.5)

    def test_standard_deviation(self):
        self.assertAlmostEqual(calculate_standard_deviation([1, 2, 3, 4, 5]), 1.414213562, places=6)
        self.assertAlmostEqual(calculate_standard_deviation([2, 2, 2, 2, 2]), 0.0, places=6)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_mean([])
        with self.assertRaises(ValueError):
            calculate_median([])
        with self.assertRaises(ValueError):
            calculate_standard_deviation([])

    def test_single_element_list(self):
        self.assertEqual(calculate_mean([10]), 10)
        self.assertEqual(calculate_median([10]), 10)
        self.assertEqual(calculate_standard_deviation([10]), 0)

if __name__ == "__main__":
    unittest.main()
