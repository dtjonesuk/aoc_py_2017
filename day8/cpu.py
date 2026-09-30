from collections import defaultdict
from pyparsing import *

identifier = Word(alphas)
INC, DEC = Keyword.using_each(["inc", "dec"])
EQ, NE, LE, LT, GE, GT = Keyword.using_each(["==", "!=", "<=", "<", ">=", ">"])
operator = INC | DEC
comparator = EQ | NE | LE | LT | GE | GT
number = pyparsing_common.signed_integer

parser = identifier + operator + number + "if" + identifier + comparator + number


class Instruction:
    def __init__(self, elems):
        self.destination = elems[0]
        self.operation = elems[1]
        self.value = elems [2]
        self.where = elems[4]
        self.comparator = elems[5]
        self.compare_to = elems[6]

    def calculate(self, a, b):
        if self.operation == "inc":
            return a + b
        else:
            return a - b

    def compare(self, a, b) -> bool:
        if self.comparator == "==":
            return a == b
        elif self.comparator == "!=":
            return a != b
        elif self.comparator == "<":
            return a < b
        elif self.comparator == ">":
            return a > b
        elif self.comparator == "<=":
            return a <= b
        else:
            return a >= b

    def __repr__(self):
        return f"{self.destination} {self.operation} {self.value} if {self.where} {self.comparator} {self.compare_to}"

def parse_instruction(s:str) -> Instruction|None:
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
        if instruction.compare(a,b):
            # carry out operation
            self.registers[instruction.destination] = instruction.calculate(
                self.registers[instruction.destination],
                instruction.value)
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
