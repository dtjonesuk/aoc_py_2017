import os

from duet import SoundCPU, parse_instruction, SendCPU
from lib.input import Input

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")


def part1(instructions):
    cpu = SoundCPU(instructions)
    freq = cpu.run()
    return freq


def part2(instructions):
    p0queue = []  # Messages for program 0
    p1queue = []  # Messages for program 1
    program0 = SendCPU(instructions, p1queue, p0queue, 0)
    program1 = SendCPU(instructions, p0queue, p1queue, 1)

    # Program stops execution when
    # - Both programs' PC are outside bounds
    # or
    # - Both programs are blocked waiting to receive a message (deadlocked)
    while (program0.running() or program1.running()) and not (program0.blocked and program1.blocked):
        program0.execute()
        program1.execute()

    return program1.send_count


if __name__ == "__main__":
    data = Input(input_path).read_lines()
    instructions = [parse_instruction(line) for line in data]
    print("Part 1: ", part1(instructions))
    print("Part 2: ", part2(instructions))
