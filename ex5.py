# define a function that takes two parameters
# and returns the maximum
# num_max(a, b)

# num_max(1, 5)  -> 5
# num_max(-10, 0) -> 0
# num_max(1, 1) -> 1

def num_max(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input('Enter a: '))
b = int(input('Enter b: '))

print(num_max(a, b))


# I can call a function inside another function to restructure my code
# I can pass the arguments name, draw_stars(star=4, space=2)
# Functions can return a value using the `return` keyword
# Anything after the `return` keyword is ignored inside a function
