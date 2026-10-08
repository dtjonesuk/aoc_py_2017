import unittest
from lib.input import Input
from day18 import solution
from day18.duet import parse_instruction, SoundCPU


class Part1TestCase(unittest.TestCase):
    input = """set a 1
            add a 2
            mul a a
            mod a 5
            snd a
            set a 0
            rcv a
            jgz a -1
            set a 1
            jgz a -2"""

    correct_instructions = [
        ['set', 'a', 1],
        ['add', 'a', 2],
        ['mul', 'a', 'a'],
        ['mod', 'a', 5],
        ['snd', 'a'],
        ['set', 'a', 0],
        ['rcv', 'a'],
        ['jgz', 'a', -1],
        ['set', 'a', 1],
        ['jgz', 'a', -2]
    ]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()
        self.instructions = [parse_instruction(line) for line in self.data]

    def test_input(self):
        instructions = [list(ins) for ins in self.instructions]
        self.assertSequenceEqual(instructions, self.correct_instructions)

    def text_execute(self):
        cpu = SoundCPU(self.instructions)
        freq = cpu.run()
        self.assertEqual(freq, 4)


class Part2TestCase(unittest.TestCase):
    input = ""

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertSequenceEqual(self.data, [])


if __name__ == '__main__':
    unittest.main()
