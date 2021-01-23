# write a program that asks the user for a input
# and ask them for a character then count this character

# Enter a text: Hello how are you hope you are fine
# Enter a character: l
# there are 2 l in this text
# no matches found for l

text = input("Enter a text: ")
char = input("Enter a character: ")

count = 0

text = text.lower()
char = char.lower()

for i in text:
    if i == char:
        count = count + 1

if count == 0:
    print("There are no matches for", char)
elif count == 1:
    print("There are one match for", char)
else:
    print("There are", count, "matches for", char)
