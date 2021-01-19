def draw_five_stars():
    for i in range(0, 5):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


def draw_stars(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


def draw_rectangle(width, height, character="*", color="red"):
    print(f"I will draw a rectangle {width}x{height} using {character} in {color}")


draw_stars(8)
# draw_stars(4)
# draw_stars(10)
# draw_rectangle(10, 6, "$", "red")
# draw_rectangle(10, 6, color="bleu")



# draw_five_stars()