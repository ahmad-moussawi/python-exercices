# available operators: +,-,*, and /
# only positive numbers allowed
# i.e. user should enter the first operand, second operand, and the operator

# read a from user and ensure a > 0
a = float(input("Enter 'a': "))
while a < 0:
    a = float(input("Enter 'a' (should be positive): "))

# read b from user and ensure a > 0
b = float(input("Enter 'b': "))
while b < 0:
    b = float(input("Enter 'b' (should be positive): "))

operator = input("Enter operator (+, -, *, /): ")
# operator = input("Enter operator (plus, minus, times, divide): ")

if operator == "+":
    print(f"{a} + {b} =", a + b)

elif operator == "-":
    print(f"{a} - {b} =", a - b)

elif operator == "*":
    print(f"{a} * {b} =", a * b)

elif operator == "/":
    print(f"{a} / {b} =", a / b)

else:  # everything else
    print(f"Unknown operator {operator}.")



