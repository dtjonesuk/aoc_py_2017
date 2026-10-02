import os

import knothash
from knothash import KnotHash
from lib.input import Input

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

# convert a string into a list of ascii values plus some magic numbers provided by the puzzle
def convert_to_ascii(s: str):
    lengths = list(map(ord, s))
    return lengths + [17, 31, 73, 47, 23]

def calculate_single_hash_round(lengths:list[int]):
    knot_hash = KnotHash(256)
    for length in lengths:
        knot_hash.hash_round(length)
    return knot_hash.string[0] * knot_hash.string[1]

def calculate_hash(s: str):
    # 1. Convert input string to ascii values
    lengths = convert_to_ascii(s)

    # 2. Run 64 rounds of hashing
    knot_hash = KnotHash(256)
    for i in range(64):
        for length in lengths:
            knot_hash.hash_round(length)

    # 3. Calculate dense hash
    blocks = knot_hash.get_dense_hash(16)

    # 4. Convert to hexadecimal string
    hex = "".join("{:02x}".format(n) for n in blocks)

    return hex


def part1(lengths):
    total = calculate_single_hash_round(lengths)
    return total

def part2(s):
    total = calculate_hash(s)
    return total

if __name__ == "__main__":
    data = Input(input_path).read_lines_as_csv_ints().pop()
    print("Part 1: ", part1(data))

    data = Input(input_path).read_lines().pop()
    print("Part 2: ", part2(data))

