import unittest
from lib.input import Input
from day17 import solution
from day17.spinlock import Spinlock


class Part1TestCase(unittest.TestCase):
    input = ""
    correct_answers = [
        ([0, 1], 1),
        ([0, 2, 1], 1),
        ([0, 2, 3, 1], 2),
        ([0, 2, 4, 3, 1], 2),
        ([0, 5, 2, 4, 3, 1], 1),
        ([0, 5, 2, 4, 3, 6, 1], 5),
        ([0, 5, 7, 2, 4, 3, 6, 1], 2),
        ([0, 5, 7, 2, 4, 3, 8, 6, 1], 6),
        ([0, 9, 5, 7, 2, 4, 3, 8, 6, 1], 1)
    ]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_spinlock_step(self):
        spinlock = Spinlock(3)
        for n in range(1, 10):
            spinlock.step(n)
            buffer, position = self.correct_answers[n - 1]
            self.assertSequenceEqual(spinlock.buffer, buffer)
            self.assertEqual(spinlock.position, position)

    def test_spinlock_run(self):
        spinlock = Spinlock(3)
        spinlock.run()
        number = spinlock.get_next_number()
        self.assertEqual(number, 638)

class Part2TestCase(unittest.TestCase):
    input = ""

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertSequenceEqual(self.data, [])


if __name__ == '__main__':
    unittest.main()
