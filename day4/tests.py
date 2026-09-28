import unittest
from lib.input import Input
from day4 import solution

class Part1TestCase(unittest.TestCase):
    input:str = """aa bb cc dd ee
    aa bb cc dd aa
    aa bb cc dd aaa"""

    def test_input(self):
        data = Input(from_string=self.input).read_lines()
        self.assertEqual(len(data), 3)

    def test_is_valid_passphrase(self):
        data = Input(from_string=self.input).read_lines()
        self.assertTrue(solution.is_valid_passphrase(data[0]))
        self.assertTrue(not solution.is_valid_passphrase(data[1]))
        self.assertTrue(solution.is_valid_passphrase(data[2]))

class Part2TestCase(unittest.TestCase):
    input:str = """abcde fghij
    abcde xyz ecdab
    a ab abc abd abf abj
    iiii oiii ooii oooi oooo
    oiii ioii iioi iiio"""

    def test_input(self):
        data = Input(from_string=self.input).read_lines()
        self.assertEqual(len(data), 5)

    def test_is_valid_passphrase_no_anagrams(self):
        data = Input(from_string=self.input).read_lines()
        self.assertTrue(solution.is_valid_passphrase_no_anagrams(data[0]))
        self.assertTrue(not solution.is_valid_passphrase_no_anagrams(data[1]))
        self.assertTrue(solution.is_valid_passphrase_no_anagrams(data[2]))
        self.assertTrue(solution.is_valid_passphrase_no_anagrams(data[3]))
        self.assertTrue(not solution.is_valid_passphrase_no_anagrams(data[4]))

if __name__ == '__main__':
    unittest.main()
