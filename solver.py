#BGGOYYWRW.OBRWBROWG.BGBBRRYOR.OORWGYYYB.WWYROOYGG.OGGBWBWYR
#Side 0    Side 1    Side 2    Side 3    Side 4    Side 5
#
#BGG   OYY   WRW
#Line0 Line1 Line2
#
#side * 9 + line * 3 + ii
#
#        B G G
#        O Y Y
#        W R W
# O B R  B G B  O O R  W W Y
# W B R  B R R  W G Y  R O O
# O W G  Y O R  Y Y B  Y G G
#        O G G
#        B W B
#        W Y R
#
#
#
#            0  1  2
#            3  4  5
#            6  7  8
#  9 10 11  18 19 20  27 28 29  36 37 38
# 12 13 14  21 22 23  30 31 32  39 40 41
# 15 16 17  24 25 26  33 34 35  42 43 44
#           45 46 47
#           48 49 50
#           51 52 53





# class CubeSolver():
def display_cube(cube):
    print(cube)
    for i in range(3):
        print('  ' * 3 + ' ', end='')
        print_cube_line(cube, 0, i)
        print()

    for i in range(3):
        for s in range(4):
            print_cube_line(cube, s + 1, i)
            print(' ', end='')
        print()

    for i in range(3):
        print('  ' * 3 + ' ', end='')
        print_cube_line(cube, 5, i)
        print()
    return 7


def print_cube_line(cube, side, line):
    for ii in range(3):
        print(cube[side * 9 + line * 3 + ii] + ' ', end='')
        # printbox(cube[side * 9 + line * 3 + ii])


# Попытка сделать эмодзи цветные квадратики.. Не получилось.
# def printbox(color):
#     if color == "Y":
#         print("\U0001f7e8")
    