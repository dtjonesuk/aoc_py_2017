import os
from lib.input import Input
from pipes import Nodes

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")


def part1(data):
    nodes = Nodes(data)
    group = nodes.get_group(0)
    total = len(group)

    return total


def part2(data):
    nodes = Nodes(data)
    groups = nodes.find_all_groups()
    total = len(groups)
    return total


if __name__ == "__main__":
    data = Input(input_path).read_lines()
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
