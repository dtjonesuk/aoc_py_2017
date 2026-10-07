import unittest

from dancing import parse_move, Dance
from lib.input import Input
from day16 import solution


class Part1TestCase(unittest.TestCase):
    input = """s1,x3/4,pe/b"""

    correct_moves = [
        ["s", 1],
        ["x", 3, 4],
        ["p", "e", "b"]
    ]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines_as_csv()[0]
        self.dance_moves = [list(parse_move(m)) for m in self.data]

    def test_input(self):
        self.assertSequenceEqual(self.dance_moves, self.correct_moves)

    def test_dance(self):
        dance = Dance("abcde", self.dance_moves)
        dance.run()
        self.assertEqual(repr(dance), "baedc")


class Part2TestCase(unittest.TestCase):
    input = ""
    
    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertSequenceEqual(self.data, [])


if __name__ == '__main__':
    unittest.main()
