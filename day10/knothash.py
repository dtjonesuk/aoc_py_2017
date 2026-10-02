from functools import reduce
import operator

class KnotHash:
    def __init__(self, length):
        self.length = length
        self.position = 0
        self.skip = 0
        self.string = list(range(length))

    def hash_round(self, length: int):
        end = (self.position + length) % self.length
        if length == 0:
            # Nothing to do
            pass
        elif end <= self.position:
            # Create reversed sublist, then update string in two chunks
            sublist = list(reversed(self.string[self.position:] + self.string[:end]))

            # Current position -> end of list
            n = self.length - self.position
            self.string[self.position:] = sublist[:n]

            # Beginning of list -> end point
            self.string[:end] = sublist[n:]
        else:
            # reverse selected section
            self.string[self.position:end] = reversed(self.string[self.position:end])

        # move position forward
        self.position = (self.position + length + self.skip) % len(self.string)

        # increase skip size
        self.skip += 1

    def get_dense_hash(self, block_size:int):
        # 1. Split the string into length/block_size blocks of size block_size
        blocks = [self.string[i:i+block_size] for i in range(0, self.length, block_size)]

        # 2. Calculate block[0] xor block[1] xor block[2]... for each block
        dense_hash = [reduce(operator.xor, block, initial=0) for block in blocks]

        return dense_hash