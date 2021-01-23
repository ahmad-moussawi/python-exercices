# 1. tree
# define a function draw_tree(width, character) triangle (like a tree)
# draw_tree(4, "*")
#    *
#   * *
#  * * *
# * * * *

def draw_line(spaces, size, char, alternative_char):
    for j in range(0, spaces):
        print(" ", end="")

    for j in range(0, size):
        if j % 2 == 0:
            print(char, end=" ")
        else:
            print(alternative_char, end=" ")
    print()


def draw_tree(n, char="*", alternative_char="."):
    for i in range(0, n + 1):
        draw_line(n - i + 1, i, char, alternative_char)


# draw_tree(10, "*", "%")


# draw_line(4, 1, "*")
# draw_line(3, 2, "*")
# draw_line(2, 3, "*")
# draw_line(1, 4, "*")


# draw_tree(4, ".")
#    .
#   . .
#  . . .
# . . . .


# 2. draw_rectangle(width, height)
# draw_rectangle(5, 3)
# * * * * *
# * * * * *
# * * * * *


def draw_rectangle(width, height):
    for i in range(0, height):
        draw_line(0, width, "*", "*")


# draw_rectangle(10, 5)

# 3. draw_square(size)
# draw_square(4)
# * * * *
# * * * *
# * * * *
# * * * *


def draw_square(n):
    draw_rectangle(n, n)


# draw_square(10)


# 4. draw_square_outline(size)
# * * * *
# *     *
# *     *
# * * * *

def draw_square_outline(n):
    for x in range(0, n):
        for y in range(0, n):
            is_border = x == 0 or x == n - 1 or y == 0 or y == n - 1

            print("*" if is_border else " ", end=" ")

            # if is_border:
            #     print("*", end=" ")
            # else:
            #     print(" ", end=" ")
        print()


# draw_square_outline(5)

# 5. write a program asks the user what he want to draw
# square, size?
# tree, width?
# rectangle, width? height?

# 6. program should rerun unless the user type "exit"

# > please select an option (rectangle, square, tree, exit): rectangle
# > please enter the width: 4
# > please enter the height: 2
# * * * *
# * * * *
#
# > please select an option (rectangle, square, tree, exit):


is_running = True

while is_running:

    command = input("please select an option (rectangle, square, tree, exit): ")

    if command == "exit":
        is_running = False

    elif command == "rectangle":
        width = int(input("Please enter the width: "))
        height = int(input("Please enter the height: "))
        draw_rectangle(width, height)

    elif command == "square":
        size = int(input("Please enter the size: "))
        is_outline = input("Is outline (1 for yes): ")

        if is_outline == "1":
            draw_square_outline(size)
        else:
            draw_square(size)

    elif command == "tree":
        size = int(input("Please enter the size: "))
        draw_tree(size)
