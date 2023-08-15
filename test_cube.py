from unittest import TestCase

from cube import Cube


class TestCube(TestCase):
    def test_U(self):
        cube = Cube()
        cube.U()
        self.assertEqual(cube.get_as_string(), 'Y' * 9 + 'RRR' + 'B' * 6 + 'GGG' + 'R' * 6 + 'OOO' + 'G' * 6 + 'BBB' + 'O' * 6 + 'W' * 9)
        cube.set_as_string('BGGOYYWRWOBRWBROWGBGBBRRYOROORWGYYYBWWYROOYGGOGGBWBWYR')
        cube.U()
        self.assertEqual(cube.get_as_string(), 'WOBRYGWYGBGBWBROWGOORBRRYORWWYWGYYYBOBRROOYGGOGGBWBWYR')
#        self.fail()
