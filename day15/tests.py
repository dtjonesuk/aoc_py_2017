import unittest

from generator import Generator, GeneratorA, GeneratorB
from lib.input import Input
from day15 import solution


class Part1TestCase(unittest.TestCase):
    input = ""
    correct_answers = [
        (1092455,   430625591),
        (1181022009,  1233683848),
        (245556042,  1431495498),
        (1744312007,   137874439),
        (1352636452,   285222916)
    ]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_input(self):
        self.assertSequenceEqual(self.data, [])

    def test_generator(self):
        A = Generator(65, 16807)
        B = Generator(8921, 48271)
        a = [A.next() for i in range(5)]
        b = [B.next() for i in range(5)]
        self.assertSequenceEqual(list(zip(a,b)), self.correct_answers)

    def test_judge(self):
        gen_a = GeneratorA(65)
        gen_b = GeneratorB(8921)
        # total = solution.judge(gen_a, gen_b, 40_000_000)

        # self.assertEqual(total, 588)

class Part2TestCase(unittest.TestCase):
    input = ""
    correct_answers = [
        (1352636452,  1233683848),
        (1992081072,   862516352),
        (530830436,  1159784568),
        (1980017072,  1616057672),
        (740335192,   412269392)
    ]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_generator(self):
        A = GeneratorA(65)
        B = GeneratorB(8921)
        a = [A.next2() for i in range(5)]
        b = [B.next2() for i in range(5)]
        self.assertSequenceEqual(list(zip(a,b)), self.correct_answers)

    def test_judge2(self):
        gen_a = GeneratorA(65)
        gen_b = GeneratorB(8921)
        total = solution.judge2(gen_a, gen_b, 5_000_000)

        self.assertEqual(total, 309)

if __name__ == '__main__':
    unittest.main()
