import unittest
from lib.input import Input
from day13 import solution
from day13.firewall import parse_line


class Part1TestCase(unittest.TestCase):
    input = """0: 3
    1: 2
    4: 4
    6: 4"""

    correct_firewall = {0: 3, 1: 2, 4: 4, 6: 4}

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()
        self.depths = dict(map(parse_line, self.data))

    def test_input(self):
        self.assertDictEqual(self.depths, self.correct_firewall)

    def test_navigate(self):
        caught = solution.navigate_firewall(self.depths)
        score = solution.calculate_score(caught, self.depths)
        self.assertEqual(score, 24)

class Part2TestCase(unittest.TestCase):
    input = """0: 3
    1: 2
    4: 4
    6: 4"""

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()
        self.depths = dict(map(parse_line, self.data))

    def test_find_delay(self):
        self.assertEqual(solution.find_delay(self.depths), 10)


if __name__ == '__main__':
    unittest.main()
