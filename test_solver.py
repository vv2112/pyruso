import unittest
from solver import display_cube


class TestCubeSolver(unittest.TestCase):

    def test_whiteCrest(self):
        self.assertEqual(display_cube('BGGOYYWRWOBRWBROWGBGBBRRYOROORWGYYYBWWYROOYGGOGGBWBWYR'), None)


if __name__ == '__main__':
    unittest.main()
