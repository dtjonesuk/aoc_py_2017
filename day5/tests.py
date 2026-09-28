import unittest
from lib.input import Input
from day5 import solution
from day5.cpu import CPU

class Part1TestCase(unittest.TestCase):
    input = """0
            3
            0
            1
            -3"""

    def test_input(self):
        data = Input(from_string=self.input).read_lines_as_ints()
        self.assertSequenceEqual(data, [0,3,0,1,-3])

    def test_run_program(self):
        data = Input(from_string=self.input).read_lines_as_ints()
        self.assertEqual(solution.run_program(data), 5)


class Part2TestCase(unittest.TestCase):
    input = """0
                3
                0
                1
                -3"""

    def test_run_program(self):
        print("---")
        data = Input(from_string=self.input).read_lines_as_ints()
        cpu = CPU(data, rules=2)
        self.assertEqual(solution.run_program(data, rules=2), 10)
        cpu.run()
        pass

if __name__ == '__main__':
    unittest.main()
