import os
from lib.input import Input
from memory import MemoryBank

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

# single line of input
data = Input(input_path).read_lines_as_tsv_ints()[0]

def part1():
    memory = MemoryBank(data.copy())
    ticks, length = memory.run()
    return ticks

def part2():
    memory = MemoryBank(data.copy())
    ticks, length = memory.run()
    return length

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())

