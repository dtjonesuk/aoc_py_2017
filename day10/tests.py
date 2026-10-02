import unittest
from lib.input import Input
from day10 import solution
from day10.knothash import KnotHash


class Part1TestCase(unittest.TestCase):
    input = "0,1,2,3,4"
    lengths = [3, 4, 1, 5]

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines_as_csv_ints()[0]

    def test_input(self):
        self.assertSequenceEqual(self.data, [0, 1, 2, 3, 4])

    def test_knothash_init(self):
        knot_hash = KnotHash(256)
        self.assertEqual(len(knot_hash.string), 256)
        self.assertEqual(min(knot_hash.string), 0)
        self.assertEqual(max(knot_hash.string), 255)

    def test_knot(self):
        knot_hash = KnotHash(5)
        lengths = self.lengths.copy()

        knot_hash.hash_round(lengths.pop(0))
        self.assertEqual(knot_hash.string, [2, 1, 0, 3, 4])
        self.assertEqual(knot_hash.position, 3)
        self.assertEqual(knot_hash.skip, 1)

        knot_hash.hash_round(lengths.pop(0))
        self.assertEqual(knot_hash.string, [4, 3, 0, 1, 2])
        self.assertEqual(knot_hash.position, 3)
        self.assertEqual(knot_hash.skip, 2)

        knot_hash.hash_round(lengths.pop(0))
        self.assertEqual(knot_hash.string, [4, 3, 0, 1, 2])
        self.assertEqual(knot_hash.position, 1)
        self.assertEqual(knot_hash.skip, 3)

        knot_hash.hash_round(lengths.pop(0))
        self.assertEqual(knot_hash.string, [3, 4, 2, 1, 0])
        self.assertEqual(knot_hash.position, 4)
        self.assertEqual(knot_hash.skip, 4)

    def test_calculate_hash(self):
        knot_hash = KnotHash(5)
        lengths = self.lengths.copy()

        for length in lengths:
            knot_hash.hash_round(length)
        hash = knot_hash.string[0] * knot_hash.string[1]
        self.assertEqual(hash, 12)


class Part2TestCase(unittest.TestCase):
    # input has an empty line at the beginning
    input = """
    AoC 2017
    1,2,3
    1,2,4"""

    hash_input = """a2582a3a0e66e6e86e3812dcb672a272
    33efeb34ea91902bb2f59c9920caa6cd
    3efbe78a8d82f29979031a4aa0b16a9d
    63960835bcdc130f0b66d7ff4f6a5a8e"""

    def setUp(self):
        self.data = Input(from_string=self.input, strip_empty=False).read_lines()

        self.correct_hashes = Input(from_string=self.hash_input).read_lines()

    def test_input(self):
        self.assertEqual(len(self.data), len(self.correct_hashes))

    def test_convert_to_ascii(self):
        self.assertSequenceEqual(solution.convert_to_ascii("1,2,3"), [49,44,50,44,51,17,31,73,47,23])

    def test_hash(self):
        hashes = list(map(solution.calculate_hash, self.data))
        self.assertSequenceEqual(hashes, self.correct_hashes)

if __name__ == '__main__':
    unittest.main()
