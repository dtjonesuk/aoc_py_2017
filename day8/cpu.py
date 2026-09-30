from collections import defaultdict
from pyparsing import *
import operator as op

identifier = Word(alphas)
INC, DEC = Keyword.using_each(["inc", "dec"])
EQ, NE, LE, LT, GE, GT = Keyword.using_each(["==", "!=", "<=", "<", ">=", ">"])
operator = INC | DEC
comparator = EQ | NE | LE | LT | GE | GT
number = pyparsing_common.signed_integer

parser = identifier + operator + number + Suppress("if") + identifier + comparator + number

operator_map = {
    "==": op.eq,
    "!=": op.ne,
    "<=": op.le,
    "<": op.lt,
    ">=": op.ge,
    ">": op.gt,
    "inc": op.add,
    "dec": op.sub
}


class Instruction:
    def __init__(self, elems):
        self.destination = elems[0]
        self.operation = operator_map[elems[1]]
        self.value = elems[2]
        self.where = elems[3]
        self.comparator = operator_map[elems[4]]
        self.compare_to = elems[5]

    def __repr__(self):
        return f"{self.destination} {self.operation} {self.value} if {self.where} {self.comparator} {self.compare_to}"


def parse_instruction(s: str) -> Instruction | None:
    return Instruction(parser.parse_string(s))


class CPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.pc = 0
        self.highest = 0
        self.registers = defaultdict(int)

    def execute(self, instruction):
        # test condition
        a = self.registers[instruction.where]
        b = instruction.compare_to
        if instruction.comparator(a, b):
            # carry out operation
            a = self.registers[instruction.destination]
            b = instruction.value
            self.registers[instruction.destination] = instruction.operation(a, b)

            # store highest value (if greater than existing highest) for later
            self.highest = max(self.highest, max(self.registers.values()))

    def run(self):
        self.pc = 0
        for instruction in self.instructions:
            self.execute(instruction)
            self.pc += 1


if __name__ == "__main__":
    test = """b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a <= 1
    c inc -20 if c == 10"""

    parser.run_tests(test)
    instructions = [parse_instruction(line) for line in test.splitlines()]
