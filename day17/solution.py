import os
from lib.input import Input
from spinlock import Spinlock, BufferlessSpinlock

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

def part1(cycles):
    spinlock = Spinlock(cycles)
    spinlock.run()
    total = spinlock.get_next_number()
    return total

def part2(cycles):
    spinlock = BufferlessSpinlock(cycles)
    spinlock.run(50_000_000)
    total = spinlock.get_next_number()
    return total

if __name__ == "__main__":
    cycles = Input(input_path).read_lines_as_ints()[0]
    print("Part 1: ", part1(cycles))
    print("Part 2: ", part2(cycles))

