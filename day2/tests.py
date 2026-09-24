import unittest
from lib.input import Input
from day2 import solution

test_input = """5 1 9 5
7 5 3
2 4 6 8
"""

test_input2 = """5 9 2 8
9 4 7 3
3 8 6 5
"""

class Part1TestCase(unittest.TestCase):
    def test_input(self):
        data = Input(from_string=test_input).read_lines_as_tsv_ints()
        self.assertEqual(len(data), 3)
        self.assertSequenceEqual(data[0], [5, 1, 9, 5])
        self.assertSequenceEqual(data[1], [7, 5, 3])
        self.assertSequenceEqual(data[2], [2, 4, 6, 8])

    def test_line_checksum(self):
        data = Input(from_string=test_input).read_lines_as_tsv_ints()
        self.assertEqual(solution.line_checksum(data[0]), 8)
        self.assertEqual(solution.line_checksum(data[1]), 4)
        self.assertEqual(solution.line_checksum(data[2]), 6)

    def test_checksum(self):
        data = Input(from_string=test_input).read_lines_as_tsv_ints()
        self.assertEqual(solution.checksum(data), 18)

class Part2TestCase(unittest.TestCase):
    def test_something(self):
        data = Input(from_string=test_input2).read_lines_as_tsv_ints()
        self.assertEqual(solution.line_even_divisors(data[0]), 4)
        self.assertEqual(solution.line_even_divisors(data[1]), 3)
        self.assertEqual(solution.line_even_divisors(data[2]), 2)


if __name__ == '__main__':
    unittest.main()
