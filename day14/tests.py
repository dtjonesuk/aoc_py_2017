import unittest

import knothash
from lib.input import Input
from day14 import solution
from day10.knothash import KnotHash


class Part1TestCase(unittest.TestCase):
    input = """##.#.#..
            .#.#.#.#   
            ....#.#.   
            #.#.##.#   
            .##.#...   
            ##..#..#   
            .#...#..   
            ##.#.##."""

    # hash phrase for use with supplied test input
    phrase = "flqrgnkx"

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()
        self.binary = [int(s.replace('#', '1').replace('.', '0'), 2) for s in self.data]

    def test_input(self):
        hashes=[]
        for i in range(8):
            knothash = KnotHash(256)
            hash = knothash.hash(f"{self.phrase}-{i}")
            hashes.append(hash[0])
        self.assertSequenceEqual(self.binary, hashes)

    def test_get_grid(self):
        grid = solution.get_grid(self.phrase)
        total = sum(bit for row in grid for bit in row)
        self.assertEqual(total, 8108)

class Part2TestCase(unittest.TestCase):
    input = ""
    # hash phrase for use with supplied test input
    phrase = "flqrgnkx"

    def setUp(self):
        self.data = Input(from_string=self.input).read_lines()

    def test_get_blocks(self):
        grid = solution.get_grid(self.phrase)
        regions = solution.get_regions(grid)

        self.assertEqual(regions, 1242)


if __name__ == '__main__':
    unittest.main()
