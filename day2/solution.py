import os
from lib.input import Input

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

data = Input(input_path).read_lines_as_tsv_ints()

def line_checksum(numbers: list[int]) -> int:
    return max(numbers) - min(numbers)

def checksum(numbers: list[list[int]]) -> int:
    return sum(map(line_checksum, numbers))

def line_even_divisors(numbers: list[int]) -> int:
    for idx, a in enumerate(numbers[:-1]):
        for b in numbers[idx+1:]:
            if max(a,b) % min(a,b) == 0:
                return max(a,b) // min(a,b)
    raise ValueError("Input error: Line does not contain two evenly divisible values.")

def checksum2(numbers: list[list[int]]) -> int:
    return sum(map(line_even_divisors, numbers))

def part1():
    total = checksum(data)
    return total

def part2():
    total = checksum2(data)
    return total

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())

