import unittest

import garbage
from lib.input import Input
from day9 import solution
from day9.garbage import parse_groups


class Part1TestCase(unittest.TestCase):
    input = """{}
    {{{}}}
    {{},{}}
    {{{},{},{{}}}}
    {<{},{},{{}}>}
    {<a>,<a>,<a>,<a>}
    {{<a>},{<a>},{<a>},{<a>}}
    {{<!>},{<!>},{<!>},{<a>}}
    """

    # number of groups in each line of input
    num_groups = [1, 3, 3, 6, 1, 1, 5, 2]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertEqual(len(self.data), 8)

    def test_count_groups(self):
        groups = [garbage.parse_groups(line) for line in self.data]
        counts = list(map(solution.get_group_count, groups))
        self.assertSequenceEqual(counts, self.num_groups)


# Test input is subtly different for the scores
class Part1TestScoreCase(unittest.TestCase):
    input = """{}
    {{{}}}
    {{},{}}
    {{{},{},{{}}}}
    {<a>,<a>,<a>,<a>}
    {{<ab>},{<ab>},{<ab>},{<ab>}}
    {{<!!>},{<!!>},{<!!>},{<!!>}}
    {{<a!>},{<a!>},{<a!>},{<ab>}}"""

    # correct score for each line of input
    correct_scores = [1, 6, 5, 16, 1, 9, 9, 3]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_scores(self):
        groups = [garbage.parse_groups(line) for line in self.data]
        scores = list(map(solution.get_total_score, groups))
        self.assertSequenceEqual(scores, self.correct_scores)


class Part2TestCase(unittest.TestCase):
    input = """<>
    <random characters>
    <<<<>
    <{!>}>
    <!!>
    <!!!>>
    <{o"i!a,<{i<a>"""

    character_counts = [0, 17, 3, 2, 0, 0, 10]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        groups = [garbage.parse_groups(line) for line in self.data]
        counts = list(map(solution.get_character_count, groups))
        self.assertSequenceEqual(counts, self.character_counts)


if __name__ == '__main__':
    unittest.main()
