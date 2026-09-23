import unittest
from lib.input import Input
from day1 import solution

test_input = ""

class Part1TestCase(unittest.TestCase):
    def test_input(self):
        data = Input(solution.input_path).read_lines()
        self.assertEqual(len(data), 1)
        self.assertIsInstance(data[0], str)

    def test_sum_digits(self):
        self.assertEqual(solution.sum_digits("1122"), 3)
        self.assertEqual(solution.sum_digits("1111"), 4)
        self.assertEqual(solution.sum_digits("1234"), 0)
        self.assertEqual(solution.sum_digits("91212129"), 9)

class Part2TestCase(unittest.TestCase):
    def test_sum_circular_digits(self):
        self.assertEqual(solution.sum_circular_digits("1212"), 6)
        self.assertEqual(solution.sum_circular_digits("1221"), 0)
        self.assertEqual(solution.sum_circular_digits("123425"), 4)
        self.assertEqual(solution.sum_circular_digits("123123"), 12)
        self.assertEqual(solution.sum_circular_digits("12131415"), 4)

if __name__ == '__main__':
    unittest.main()
