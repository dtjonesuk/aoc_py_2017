from pyparsing import *

DANCER_NAMES = "abcdefghijklmnop"
Dancer = Char(DANCER_NAMES)
Position = pyparsing_common.integer
Spin = "s" + Position
Exchange = "x" + Position + Suppress("/") + Position
Partner = "p" + Dancer + Suppress("/") + Dancer

Move = Spin | Exchange | Partner

def parse_move(m: str):
    return Move.parse_string(m)

class Dance:
    def __init__(self,names, moves):
        self.positions = list(names)
        self.moves = moves
        self.names = names

    def move(self, move):
        if move[0] == "s":
            # Swap back half with front half
            a = move[1]
            self.positions = self.positions[-a:]+self.positions[:-a]

        elif move[0] == "x":
            # Exchange two positions
            a,b = move[1:]
            temp = self.positions[a]
            self.positions[a] = self.positions[b]
            self.positions[b] = temp

        elif move[0] == "p":
            # Partner: exchange two named dancers
            a,b = move[1:]
            ia = self.positions.index(a)
            ib = self.positions.index(b)
            temp = self.positions[ia]
            self.positions[ia] = self.positions[ib]
            self.positions[ib] = temp

    def run(self):
        for move in self.moves:
            self.move(move)

    def __repr__(self):
        return "".join(self.positions)