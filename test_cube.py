import unittest

from cube import Cube
from solver import display_cube


class TestCube(unittest.TestCase):
    def test_U(self):
        cube = Cube()
        display_cube(cube.get_as_string())
        cube.U()
        display_cube(cube.get_as_string())
        self.assertEqual(cube.get_as_string(), 'Y' * 9 + 'RRR' + 'B' * 6 + 'GGG' + 'R' * 6 + 'OOO' + 'G' * 6 + 'BBB' + 'O' * 6 + 'W' * 9)
        cube.set_as_string('BGGOYYWRWOBRWBROWGBGBBRRYOROORWGYYYBWWYROOYGGOGGBWBWYR')
        cube.U()
        self.assertEqual(cube.get_as_string(), 'WOBRYGWYGBGBWBROWGOORBRRYORWWYWGYYYBOBRROOYGGOGGBWBWYR')
#        self.fail()


if __name__ == '__main__':
    unittest.main()
