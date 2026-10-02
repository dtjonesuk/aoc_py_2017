from dataclasses import dataclass


@dataclass
class Hex:
    q: int = 0
    r: int = 0
    s: int = 0

    def move(self, direction:Hex) -> Hex:
        self.q += direction.q
        self.r += direction.r
        self.s += direction.s
        return self

    def distance(self, other:Hex) -> int:
        return max(abs(self.q - other.q), abs(self.r - other.r), abs(self.s - other.s))

    def move_direction(self, direction: str):
        return self.move(direction_map[direction])

direction_map = {
    "n": Hex(-1, 1, 0),
    "ne": Hex(0, 1, -1),
    "se": Hex(1, 0, -1),
    "s": Hex(1, -1, 0),
    "sw": Hex(0, -1, 1),
    "nw": Hex(-1, 0, 1)
}


