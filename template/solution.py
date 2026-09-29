import os
from lib.input import Input

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def part1(data):
    total = 0
    return total

def part2(data):
    total = 0
    return total

if __name__ == "__main__":
    data = Input(input_path).read_lines()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))

