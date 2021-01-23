import pickle

# reading example
# with open('students.txt') as students_file:
#     # for line in students_file:
#     #     print(line, end="")
#
#     all_contents = students_file.read()
#     print(all_contents)


# read() -> read all file
# read(n) -> read the first n char from the current position
# tell() -> get the cursor position
# seek(n) -> set the cursor position


# writing example
with open("students.txt", "w") as file:
    file.write("new content here\n")


# modes
# r => open for reading (default)
# w => open for writing, and overwrite if exists, create if doesn't exist
# x => open for writing, error if exists, create if doesn't exist
# a => open for writing, append if exists, create if doesn't exist
# t => text mode (default)
# b => binary mode

list = ["ahmad", "ali", "c", "d"]

with open("data.txt", "wb") as data:
    pickle.dump(list, data)

with open("data.txt", "rb") as data:
    new_list = pickle.load(data)
    print(new_list)
