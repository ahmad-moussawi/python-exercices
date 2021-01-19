def sayHello(name):
    print("Hello", name)


def draw_line(space, star):

    # draw spaces
    for j in range(0, space):
        print(" ", end="")

    # draw *
    for j in range(0, star):
        print("*", end=" ")
    print()


def draw_triangle(n):
    for i in range(0, n):
        # print a line of i + 1 stars
        draw_line(star=i + 1, space=n - 1 - i)


def draw_square(n):
    for i in range(0, n):
        draw_line(0, n)

    print()


# draw_triangle(8)
#
# n = 3
# i   s   *
# 0   2   1
# 1   1   2
# 2   0   3
#
# * = i + 1
# s = n - *
# s = n - (i + 1)
# s = n - i - 1
#
#   *
#  * *
# * * *
#
# print()
# print()
#
# draw_square(4)
# draw_square(6)
# draw_square(10)

def double_number(num):
    return num * num


def triple_number(num):
    return num * num * num


a = double_number(1)
b = double_number(2)
c = double_number(4)

print(a, b, c)

a = triple_number(1)
b = triple_number(2)
c = triple_number(4)

print(a, b, c)

