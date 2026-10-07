import os

from generator import Generator, GeneratorA, GeneratorB
from lib.input import Input
import operator as op
input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

def judge(A:Generator, B:Generator, N:int):
    total = 0
    for i in range(N):
        a = A.next() & 65535
        b = B.next() & 65535

        if a == b:
            total += 1
    return total

def judge2(A:Generator, B:Generator, N:int):
    total = 0
    for i in range(N):
        a = A.next2() & 65535
        b = B.next2() & 65535

        if a == b:
            total += 1
    return total

def part1(data):
    N = 40_000_000
    A = GeneratorA(data["A"])
    B = GeneratorB(data["B"])

    total = 0
    for i in range(N):
        a = A.next() & 65535
        b = B.next() & 65535

        if a == b:
            total += 1
    # print(len(list(filter(lambda x: x[0] == x[1], zip(a,b)))))

    return total


def part2(data):
    N = 5_000_000
    A = GeneratorA(data["A"])
    B = GeneratorB(data["B"])

    total = judge2(A,B, N)
    return total


if __name__ == "__main__":
    data = {"A": 618, "B": 814}
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))
