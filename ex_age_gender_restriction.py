# male -> (age > 18 & age <= 50)
# female -> between 21 and 45
# name, age, gender

# name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
gender = input("Please enter your gender (m/f): ")
is_male = gender == "m"
is_female = gender == "f"

is_male_allowed = is_male and (age > 18) and (age <= 50)
is_female_allowed = is_female and (age > 21) and (age <= 45)

is_allowed = is_male_allowed or is_female_allowed
print("Is allowed", is_allowed)

