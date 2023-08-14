import unittest
from solver import displayCube



class TestCubeSolver(unittest.TestCase):

    def test_whiteCrest(self):
        self.assertEqual(displayCube('BGGOYYWRWOBRWBROWGBGBBRRYOROORWGYYYBWWYROOYGGOGGBWBWYR'), None)
        

if __name__ == '__main__':
    unittest.main()
