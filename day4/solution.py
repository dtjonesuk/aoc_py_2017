import os
from itertools import count

from lib.input import Input

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")

data = Input(input_path).read_lines()

def is_valid_passphrase(passphrase: str) -> bool:
    wordlist = passphrase.split()
    words = set()

    for word in wordlist:
        if word in words:
            return False
        words.add(word)
    return True

def is_valid_passphrase_no_anagrams(passphrase: str) -> bool:
    wordlist = passphrase.split()
    words = set()

    for word in wordlist:
        w = "".join(sorted(word))
        if w in words:
            return False
        words.add(w)
    return True

def part1():
    total = sum(map(is_valid_passphrase, data))
    return total

def part2():
    total = sum(map(is_valid_passphrase_no_anagrams, data))
    return total

if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())

