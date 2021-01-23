with open("students.txt", "r") as file:
    for i in range(0, 4):
        print("Id:", file.read(4))
        print("Name:", file.read(10))
        print("Grade:", file.read(3))
        print("You are at the position:", file.tell())

