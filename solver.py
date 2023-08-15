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


#   return


def print_cube_line(cube, side, line):
    for ii in range(3):
        print(cube[side * 9 + line * 3 + ii] + ' ', end='')

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
# fib(1000)
