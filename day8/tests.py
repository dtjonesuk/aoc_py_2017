import unittest
from lib.input import Input
from day8 import solution
from day8.cpu import CPU, Instruction, parse_instruction


class Part1TestCase(unittest.TestCase):
    input = """b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10
    """

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        instructions = [parse_instruction(line) for line in self.data]
        self.assertEqual(len(instructions), 4)

    def test_get_register_max_value(self):
        instructions = [parse_instruction(line) for line in self.data]
        cpu = CPU(instructions)
        cpu.run()
        result = solution.get_max_register_value(cpu)
        self.assertEqual(result, 1)


class Part2TestCase(unittest.TestCase):
    input = """b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10
    """

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_get_highest_register_value(self):
        instructions = [parse_instruction(line) for line in self.data]
        cpu = CPU(instructions)
        cpu.run()
        result = solution.get_highest_register_value(cpu)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
