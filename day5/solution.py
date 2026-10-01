import os
from lib.input import Input
from cpu import CPU

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

data = Input(input_path).read_lines_as_ints()

def run_program(memory, rules=1):
    cpu = CPU(memory, rules)
    return cpu.run()

# NB Need to supply a copy of 'data' to the cpu, as the memory is modified by running the program

def part1():
    total = run_program(data.copy())
    return total

def part2():

    total = run_program(data.copy(), rules=2)
    return total

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())

