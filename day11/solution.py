import os

from hexgrid import Hex
from lib.input import Input

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

def move_hexagon(moves:list[str]):
    origin = Hex(0,0,0)
    h = Hex(0, 0, 0)
    max_distance = 0
    for direction in moves:
        h.move_direction(direction)
        max_distance = max(max_distance, origin.distance(h))
    return origin.distance(h), max_distance

def part1(data):
    total, max_distance = move_hexagon(data)
    return total

def part2(data):
    total, max_distance = move_hexagon(data)
    return max_distance

if __name__ == "__main__":
    data = Input(input_path).read_lines_as_csv()[0]
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))

