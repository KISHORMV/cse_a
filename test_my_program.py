import unittest
from my_program import calculate_sum

class TestCalculateSum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        result = calculate_sum([1, 2, 3, 4, 5])
        self.assertEqual(result, 15)

    def test_sum_negative_numbers(self):
        result = calculate_sum([-1, -2, -3, -4, -5])
        self.assertEqual(result, -15)

    def test_new(self):
        result = calculate_sum([100,1])
        self.assertEqual(result,101)

if __name__ == "__main__":
    unittest.main()