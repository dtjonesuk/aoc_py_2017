import os
from pprint import pprint

from firewall import parse_line
from lib.input import Input

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")


# def navigate_firewall(depths: dict[int, int], delay=0):
#     max_layer = max(depths.keys())
#     # initialize layers to -1 (empty)
#     layers = [-1] * (max_layer + 1)
#     # initialize directions to +ve (increasing in value)
#     directions = [1] * (max_layer + 1)
#
#     # Initialize layers
#     for layer in depths.keys():
#         layers[layer] = 0
#
#     current_layer = -delay
#     score = 0
#     caught = []
#     while current_layer <= max_layer:
#         # 1. Check if discovered.  If current_layer = layer's current depth
#         if current_layer >= 0 and layers[current_layer] == 0:
#             # Discovered
#             caught.append(current_layer)
#             #score += current_layer * depths[current_layer]
#
#         # 2. Move scanners one position
#         for idx in range(len(layers)):
#             if layers[idx] < 0:
#                 continue
#             elif layers[idx] == 0:
#                 directions[idx] = 1
#             elif layers[idx] == depths[idx] - 1:
#                 directions[idx] = -1
#
#             layers[idx] += directions[idx]
#
#         # 3. Move to the next layer
#         current_layer += 1
#
#     return caught

def navigate_firewall(depths: dict[int, int], delay=0):
    caught = []
    for current_layer in depths.keys():
        # 1. Check if discovered.  If current_layer is a multiple of the scanner's period
        if ((current_layer + delay) % (2 * (depths[current_layer] - 1))) == 0:
            caught.append(current_layer)

    return caught


def calculate_score(caught, depths):
    return sum(layer * depths[layer] for layer in caught)


def find_delay(depths):
    delay = 0
    caught = navigate_firewall(depths, delay)
    while len(caught) > 0:
        delay += 1
        caught = navigate_firewall(depths, delay)
    return delay


def part1(depths):
    caught = navigate_firewall(depths)
    total = calculate_score(caught, depths)

    return total


def part2(depths):
    total = find_delay(depths)

    return total


if __name__ == "__main__":
    data = Input(input_path).read_lines()
    depths = dict(map(parse_line, data))
    print("Part 1: ", part1(depths))
    print("Part 2: ", part2(depths))
