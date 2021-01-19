# ask the user for an integer positive number: n
# the program should print the sequence from 0 to n - 1
# the program should print "even" for the even numbers
# and "odd" for the odd ones.
# in addition the program should print "first", "middle", and "last"
# for the first, middle and last number.

n = int(input("Enter a positive number n: "))

# I have repetition: while/for
# I will use the for loop
# since I know the number of repetition

for i in range(0, n):
    print(i)

    if i == 0:
        print("first")

    if i % 2 == 0:
        print("even")
    else:
        print("odd")

    if i == n / 2:
        print("middle")

    if i == n - 1:
        print("last")

    print()



