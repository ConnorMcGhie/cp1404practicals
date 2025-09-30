"""
CP1404/CP5632 - Practical
Files
"""

# 1. Write user's name to a file using open and close
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# 2. Read the name from the file and print greeting using open and close
file = open("name.txt", "r")
name_from_file = file.read()  # read the contents of the file
file.close()
print(f"Hi {name_from_file}!")

# 3. Read first two numbers from numbers.txt, add and print result using 'with'
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
print(result)

# 4. Read all numbers from numbers.txt, compute total using 'with' and 'for line in file'
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())  # remove any newline characters
print(total)
