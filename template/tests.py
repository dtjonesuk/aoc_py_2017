import unittest
from lib.input import Input
from day5 import solution


class Part1TestCase(unittest.TestCase):
    input = ""

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertSequenceEqual(self.data, [])


class Part2TestCase(unittest.TestCase):
    input = ""
    
    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertSequenceEqual(self.data, [])


if __name__ == '__main__':
    unittest.main()
