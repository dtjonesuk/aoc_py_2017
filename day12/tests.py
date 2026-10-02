import unittest
from lib.input import Input
from day12 import solution
from day12.pipes import Nodes


class Part1TestCase(unittest.TestCase):
    input = """0 <-> 2
    1 <-> 1
    2 <-> 0, 3, 4
    3 <-> 2, 4
    4 <-> 2, 3, 6
    5 <-> 6
    6 <-> 4, 5
    """

    correct_nodes = {0: [2],
                     1: [1],
                     2: [0, 3, 4],
                     3: [2, 4],
                     4: [2, 3, 6],
                     5: [6],
                     6: [4, 5]}

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()
        self.nodes = Nodes(self.data)

    def test_input(self):
        self.assertDictEqual(self.nodes.nodes, self.correct_nodes)

    def test_get_group(self):
        group = self.nodes.get_group(0)
        self.assertSetEqual(group, {0, 2, 3, 4, 5, 6})


class Part2TestCase(unittest.TestCase):
    input = """0 <-> 2
    1 <-> 1
    2 <-> 0, 3, 4
    3 <-> 2, 4
    4 <-> 2, 3, 6
    5 <-> 6
    6 <-> 4, 5
    """

    correct_groups = [{0, 2, 3, 4, 5, 6}, {1}]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()
        self.nodes = Nodes(self.data)

    def test_find_all_groups(self):
        groups = self.nodes.find_all_groups()
        self.assertSequenceEqual(groups, self.correct_groups)


if __name__ == '__main__':
    unittest.main()
