import unittest
from lib.input import Input
from day11 import solution
from day11.hexgrid import Hex


class Part1TestCase(unittest.TestCase):
    input = """ne,ne,ne
    ne,ne,sw,sw
    ne,ne,s,s
    se,sw,se,sw,sw"""

    correct_distances = [3, 0, 2, 3]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines_as_csv()

    def test_hex_move(self):
        distances = [solution.move_hexagon(d)[0] for d in self.data]
        self.assertEqual(distances, self.correct_distances)


class Part2TestCase(unittest.TestCase):
    input = ""

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertSequenceEqual(self.data, [])


if __name__ == '__main__':
    unittest.main()
