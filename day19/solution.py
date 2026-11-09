import os
from lib.input import Input
from network import Network

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

def part1(data):
    network = Network(data)
    letters, _ = network.navigate()
    return "".join(letters)

def part2(data):
    network = Network(data)
    _, steps = network.navigate()
    return steps

if __name__ == "__main__":
    data = Input(input_path, strip_lines=False).read_lines_as_chars()
    print("Part 1: ", part1(data.copy()))
    print("Part 2: ", part2(data.copy()))

