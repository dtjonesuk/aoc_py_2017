import os
from lib.input import Input
from cpu import Instruction, CPU, parse_instruction

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

def get_max_register_value(cpu):
    return max(cpu.registers.values())

def get_highest_register_value(cpu):
    return cpu.highest

def part1(instructions):
    cpu = CPU(instructions)
    cpu.run()

    total = get_max_register_value(cpu)
    return total

def part2(instructions):
    cpu = CPU(instructions)
    cpu.run()

    total = get_highest_register_value(cpu)
    return total

if __name__ == "__main__":
    data = Input(input_path).read_lines()
    instructions = [parse_instruction(line) for line in data]
    print("Part 1: ", part1(instructions))
    print("Part 2: ", part2(instructions))

