from solver import display_cube


class Cube:
    cube_as_str = 'Y'*9 + 'B'*9 + 'R'*9 + 'G'*9 + 'O'*9 + 'W'*9

    def __init__(self):
        pass

    def get_as_string(self):
        return self.cube_as_str

    def set_as_string(self, str):
        self.cube_as_str = str

    def print(self):
        display_cube(self.cube_as_str)

    # вращение верха по часовой
    def U(self):
        c = list(self.cube_as_str)

        c[0], c[1], c[2], c[3], c[5], c[6], c[7], c[8] = c[6], c[3], c[0], c[7], c[1], c[8], c[5], c[2]
        for i in range(3):
            c[9+i], c[18+i], c[27+i], c[36+i] = c[18+i], c[27+i], c[36+i], c[9+i]

        self.cube_as_str = ''.join(c)
