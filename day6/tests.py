import unittest
from lib.input import Input
from day6 import solution
from day6.memory import MemoryBank


class Part1TestCase(unittest.TestCase):
    input = "0  2   7   0"

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines_as_tsv_ints()[0]

    def test_input(self):
        self.assertSequenceEqual(self.data, [0, 2, 7, 0])

    def test_memory_balance(self):

        memory = MemoryBank(self.data)

        memory.balance()
        self.assertSequenceEqual(memory.banks, [2, 4, 1, 2])

        memory.balance()
        self.assertSequenceEqual(memory.banks, [3, 1, 2, 3])

        memory.balance()
        self.assertSequenceEqual(memory.banks, [0, 2, 3, 4])

        memory.balance()
        self.assertSequenceEqual(memory.banks, [1, 3, 4, 1])

        memory.balance()
        self.assertSequenceEqual(memory.banks, [2, 4, 1, 2])

    def test_memory_run(self):
        memory = MemoryBank(self.data)
        ticks, length = memory.run()
        self.assertEqual(ticks, 5)


class Part2TestCase(unittest.TestCase):
    input = "0  2   7   0"

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines_as_tsv_ints()[0]

    def test_something(self):
        memory = MemoryBank(self.data)
        ticks, length = memory.run()
        self.assertEqual(length, 4)


if __name__ == '__main__':
    unittest.main()
