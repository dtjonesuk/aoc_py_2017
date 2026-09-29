import unittest
from lib.input import Input
from day7 import solution
from program import Program, parse_program
from graph import Graph

class Part1TestCase(unittest.TestCase):
    input = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertEqual(len(self.data), 13)

    def test_parse_program(self):
        program_list = [parse_program(line) for line in self.data]
        self.assertEqual(len(program_list), 13)

        for program in program_list:
            self.assertIsInstance(program, Program)

    def test_graph_repr(self):
        program_list = [parse_program(line) for line in self.data]
        graph = Graph(program_list)
        self.assertEqual(repr(graph), self.input)

    def test_find_roots(self):
        program_list = [parse_program(line) for line in self.data]
        graph = Graph(program_list)
        roots = graph.find_roots()
        self.assertEqual(len(roots), 1)

        root = roots.pop()
        self.assertEqual(root.name, "tknk")

class Part2TestCase(unittest.TestCase):
    input = """pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)
    """
    
    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_find_balance(self):
        program_list = [parse_program(line) for line in self.data]
        graph = Graph(program_list)
        balance = graph.find_balance()
        self.assertEqual(balance, 60)

if __name__ == '__main__':
    unittest.main()
