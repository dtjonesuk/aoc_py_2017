import numpy as np
import string


class Network:
    def __init__(self, data):
        self.array = np.array(data)

    def __repr__(self) -> str:
        return repr(self.array)

    def shape(self):
        return self.array.shape

    def find_start(self):
        # iterate over the top most row until you find  '|'
        row = self.array[0, :]
        for i, ch in enumerate(row):
            if ch == '|':
                return i
        raise RuntimeError("No starting position was found.")

    def navigate(self):
        letters = []

        # position is a tuple(row, column)
        position = (0, self.find_start())

        # direction is a tuple (row, col) that represents one move when added to position
        direction = (1, 0)

        # Initial steps = 1 (the position we start at)
        steps = 1

        while True:
            # Update position by adding direction vector
            position = (position[0] + direction[0], position[1] + direction[1])

            # Exit in case we go out of bounds
            if position[0] < 0 or position[0] >= self.array.shape[0] or position[1] < 0 or position[1] >= \
                    self.array.shape[1]:
                raise RuntimeError(f'Packet went out of bounds ({position}).')

            # Get current character
            ch = self.array[position[0], position[1]]

            # Stop once we reach the end
            if ch == ' ':
                break

            # Increment step counter
            steps += 1

            # print(position, str(ch), steps)

            if ch == '+':
                # Found a branch, turn left or right
                if direction[0] == 0:
                    # Traveling E/W, look for N/S branch
                    if position[0] > 0:
                        if self.array[position[0] - 1, position[1]] in string.ascii_uppercase + '|':
                            # Found a branch (N)
                            direction = (-1, 0)
                            continue

                    if position[0] < self.array.shape[0] - 1:
                        if self.array[position[0] + 1, position[1]] in string.ascii_uppercase + '|':
                            # Found a branch (S)
                            direction = (1, 0)
                            continue

                else:
                    # Traveling N/S, look for E/W branch
                    if position[1] > 0:
                        if self.array[position[0], position[1] - 1] in string.ascii_uppercase + '-':
                            # Found a branch (W)
                            direction = (0, -1)
                            continue

                    if position[1] < self.array.shape[1] - 1:
                        if self.array[position[0], position[1] + 1] in string.ascii_uppercase + '-':
                            # Found a branch (E)
                            direction = (0, 1)
                            continue

            elif ch in string.ascii_uppercase:
                # we found a letter, direction remains the same
                letters.append(str(ch))
                continue
            else:
                # all other characters
                # continue the current direction
                continue
        return letters, steps
