import os
from lib.input import Input
from program import Program, parse_program
from graph import Graph

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

def part1(data):
    graph = Graph(data)
    # we can assume graph has a single root
    answer = graph.find_roots().pop()
    return answer.name

def part2(data):
    graph = Graph(data)
    # we can assume graph has a single root
    answer = graph.find_balance()
    return answer

if __name__ == "__main__":
    data = Input(input_path).read_lines()
    program_list = [parse_program(line) for line in data]

    print("Part 1: ", part1(program_list))
    print("Part 2: ", part2(program_list))

