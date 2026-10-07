import os

from dancing import Dance, DANCER_NAMES, parse_move
from lib.input import Input

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

def part1(moves):
    dance = Dance(DANCER_NAMES, moves)
    dance.run()
    position = repr(dance)
    return position

# There are only a small number of dance positions before we get back to the starting position.
# Therefore, we can make a list of all the positions in order and calculate where the 1-billionth
# round will leave us without having to simulate all 1 billion rounds.

def part2(moves):
    seen = list()
    dance = Dance(DANCER_NAMES, moves)
    d = repr(dance)
    while d not in seen:
        seen.append(d)
        dance.run()
        d = repr(dance)

    # We can't assume that the looped positions will take us all the way back to the initial position
    # (although it probably does).
    first = seen.index(d)
    num_moves = len(seen) - first

    # Most of the 1 billion dances will leave us back where we started.  We only need the remaining number
    # of dances that don't neatly divide by one billion to calculate the final position.
    position = seen[first + (1_000_000_000 % num_moves)]

    return position

if __name__ == "__main__":
    data = Input(input_path).read_lines_as_csv()[0]
    moves = [list(parse_move(m)) for m in data]
    print("Part 1: ", part1(moves))
    print("Part 2: ", part2(moves))

