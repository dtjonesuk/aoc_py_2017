import unittest
from lib.input import Input
from day19.network import Network
from day19 import solution
import os

class Part1TestCase(unittest.TestCase):
    input = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""


    def setUp(self):
        self.data = Input(from_string=self.input, strip_lines=False).read_lines_as_chars()
        self.network = Network(self.data)

    def test_input(self):
        # print(self.network)
        self.assertEqual(self.network.shape(), (6,16))
        starting_pos = self.network.find_start()
        self.assertEqual(starting_pos, 5)

    def test_navigate(self):
        letters, _ = self.network.navigate()
        self.assertSequenceEqual(letters, list("ABCDEF"))

class Part2TestCase(unittest.TestCase):
    input = """     |          
     |  +--+    
     A  |  C    
 F---|--|-E---+ 
     |  |  |  D 
     +B-+  +--+ 
"""
    
    def setUp(self):
        self.data = Input(from_string=self.input, strip_lines=False).read_lines_as_chars()
        self.network = Network(self.data)

    def test_steps(self):
        _, steps = self.network.navigate()
        self.assertEqual(steps, 38)


if __name__ == '__main__':
    unittest.main()
