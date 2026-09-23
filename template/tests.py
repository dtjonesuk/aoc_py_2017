import unittest
from lib import Input
from day1 import solution

test_input = ""

class Part1TestCase(unittest.TestCase):
    def test_input(self):
        data = Input(from_string=test_input).read_lines()
        self.assertSequenceEqual(data, [])


class Part2TestCase(unittest.TestCase):
    def test_something(self):
        pass

if __name__ == '__main__':
    unittest.main()
