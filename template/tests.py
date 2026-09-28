import unittest
from lib.input import Input
from day5 import solution


class Part1TestCase(unittest.TestCase):
    input = ""
    def test_input(self):
        data = Input(from_string=self.input).read_lines()
        self.assertSequenceEqual(data, [])


class Part2TestCase(unittest.TestCase):
    input = ""
    def test_something(self):
        data = Input(from_string=self.input).read_lines()
        pass

if __name__ == '__main__':
    unittest.main()
