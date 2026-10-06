import os
import numpy as np

from lib.input import Input
from day10.knothash import KnotHash

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")


def get_grid(phrase: str):
    grid = []
    for i in range(128):
        knothash = KnotHash(256)
        hash = knothash.hash(f"{phrase}-{i}")
        line = list(int(bit) for byte in hash for bit in list(np.binary_repr(byte, 8)))

        grid.append(line)
    return grid


def get_regions(grid):
    grid = np.array(grid)

    # list of tuple of x,y coordinates already visited
    visited = set()

    current_region = 0

    # N,S,E,W directions
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

    for y in range(128):
        for x in range(128):
            if (x, y) in visited:
                continue

            # If location is not set, we can ignore
            if grid[x, y] == 0:
                continue

            to_visit = [(x, y)]
            while len(to_visit) > 0:
                # Take next location from top of stack
                ix, iy = to_visit.pop(0)
                visited.add((ix, iy))

                # Visit every connected location in this region
                # (exclude blocks outside valid range [0,128)
                locations = [loc for loc in ((ix + dir[0], iy + dir[1]) for dir in directions) if
                             0 <= loc[0] < 128 and 0 <= loc[1] < 128]
                # Only visit if location is set and we have not yet visited
                to_visit.extend(loc for loc in locations if loc not in visited and grid[loc[0], loc[1]] == 1)

            # All locations in this region have been visited, increment # of region counter
            current_region += 1

    return current_region


def part1(phrase):
    grid = get_grid(phrase)
    total = sum(bit for row in grid for bit in row)
    return total


def part2(phrase):
    grid = get_grid(phrase)
    total = get_regions(grid)

    return total


if __name__ == "__main__":
    data = Input(input_path).read_lines()[0]
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
