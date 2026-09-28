class CPU:
    def __init__(self, memory: list[int], rules=1):
        self.memory = memory
        self.pc = 0
        self.ticks = 0
        self.rules = rules

    def tick(self) -> bool:
        # increment tick counter
        self.ticks += 1

        # get next instruction
        instruction = self.memory[self.pc]

        # apply rule to this instruction's memory
        if self.rules == 1:
            # part one
            self.memory[self.pc] += 1
        elif self.rules == 2:
            # part two
            if instruction >= 3:
                self.memory[self.pc] -= 1
            else:
                self.memory[self.pc] += 1

        # calculate next pc
        next_pc = self.pc + instruction

        if next_pc >= len(self.memory):
            return False

        self.pc = next_pc
        return True

    def run(self):
        self.pc = 0
        self.ticks = 0

        while self.tick():
            pass

        return self.ticks
