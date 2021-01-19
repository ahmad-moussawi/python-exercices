# the application should ask the user for the following:
# - name
# - age
# the age should be > 18 and <= 50
# if valid it should print True, and False otherwise

name = input("Please enter your name: ")
age = float(input("Please enter your age: "))

print(f"Hello {name}!, your age is {age}")

# age = < 18, or > 20
is_allowed = (age > 18) and (age <= 50)

print("Driving allowed: ", is_allowed)
