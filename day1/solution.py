import os
from lib.input import Input

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

data = Input(input_path).read_lines()[0]

def sum_digits(s:str) -> int:
    total = 0
    last = s[-1]
    for digit in s:
        if digit == last:
            total += int(digit)
        last = digit
    return total

def sum_circular_digits(s:str) -> int:
    total = 0
    for idx, digit in enumerate(s):
        circular = (idx + len(s)//2) % len(s)
        if digit == s[circular]:
            total += int(digit)
    return total

def part1():
    total = sum_digits(data)
    return total

def part2():
    total = sum_circular_digits(data)
    return total

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())

