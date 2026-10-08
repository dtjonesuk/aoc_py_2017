from collections import defaultdict

from pyparsing import *

Register = Char(alphas)
Number = pyparsing_common.signed_integer
X = Register.set_results_name("x")
Xj = Register.set_results_name("x") | Number.set_results_name("x")
Y = Number.set_results_name("y") | Register.set_results_name("y")
Snd, Rcv = Keyword.using_each(["snd", "rcv"])
Set, Add, Mul, Mod, Jump = Keyword.using_each(["set", "add", "mul", "mod", "jgz"])

Stmt = Snd + X | Rcv + X | Set + X + Y | Add + X + Y | Mul + X + Y | Mod + X + Y | Jump + Xj + Y


# snd X plays a sound with a frequency equal to the value of X.
# set X Y sets register X to the value of Y.
# add X Y increases register X by the value of Y.
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
# mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
# rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
# jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)


def parse_instruction(s: str):
    return Stmt.parse_string(s)


class SoundCPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.pc = 0
        self.registers = defaultdict(int)
        self.frequency = 0
        self.recover = False

    def execute(self):
        def get_value(a: str | int):
            if isinstance(a,str):
                return self.registers[a]
            else:
                return a

        def set_value(a, b):
            self.registers[a] = get_value(b)

        instruction = self.instructions[self.pc]
        opcode = instruction[0]
        self.pc += 1
        match opcode:
            case "snd":
                self.frequency = get_value(instruction.x)
            case "set":
                set_value(instruction.x, instruction.y)
            case "add":
                set_value(
                    instruction.x,
                    get_value(instruction.x) + get_value(instruction.y)
                )
            case "mul":
                set_value(
                    instruction.x,
                    get_value(instruction.x) * get_value(instruction.y)
                )
            case "mod":
                set_value(
                    instruction.x,
                    get_value(instruction.x) % get_value(instruction.y)
                )
            case "rcv":
                self.recover = True
            case "jgz":
                if get_value(instruction.x) > 0:
                    self.pc += instruction.y - 1

    def run(self):
        while not self.recover:
            self.execute()
        return self.frequency

class SendCPU:
    def __init__(self, instructions, send_queue, recv_queue, cpuid):
        self.instructions = instructions
        self.pc = 0
        self.registers = defaultdict(int)
        self.registers["p"] = cpuid
        self.send_count = 0
        self.send_queue = send_queue
        self.recv_queue = recv_queue
        self.cpuid = cpuid
        self.blocked = False

    def send(self, value):
        # print(f"CPU{self.cpuid}: Send {value}")
        self.send_queue.append(value)
        self.send_count += 1

    def receive(self):
        if len(self.recv_queue) == 0:
            return False, 0
        value = self.recv_queue.pop(0)
        # print(f"CPU{self.cpuid}: Recv {value}")
        return True, value

    def execute(self):
        def get_value(a: str | int):
            if isinstance(a,str):
                return self.registers[a]
            else:
                return a

        def set_value(a, b):
            assert(isinstance(a, str))
            self.registers[a] = get_value(b)

        instruction = self.instructions[self.pc]
        opcode = instruction[0]
        self.pc += 1
        match opcode:
            case "snd":
                # Send
                self.send(get_value(instruction.x))
            case "rcv":
                # Receive
                ok, value = self.receive()
                if not ok:
                    # Nothing to receive, run instruction again next cycle
                    self.pc -= 1
                    self.blocked = True
                    return
                set_value(
                    instruction.x,
                    value
                )
                self.blocked = False
            case "set":
                set_value(instruction.x, instruction.y)
            case "add":
                set_value(
                    instruction.x,
                    get_value(instruction.x) + get_value(instruction.y)
                )
            case "mul":
                set_value(
                    instruction.x,
                    get_value(instruction.x) * get_value(instruction.y)
                )
            case "mod":
                set_value(
                    instruction.x,
                    get_value(instruction.x) % get_value(instruction.y)
                )
            case "jgz":
                if get_value(instruction.x) > 0:
                    self.pc += get_value(instruction.y) - 1

    def running(self):
        return 0 <= self.pc < len(self.instructions)

    # def run(self):
    #     while 0 < self.pc < len(self.instructions):
    #         self.execute()
    #     return self.send_count