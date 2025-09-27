"""
CP1404 - Practical
Print number of asterisks equal to the length of the users password
"""

min_password_length = 8

password = input("Enter a password: ")
while len(password) < min_password_length:
    print(f"Password must be at least {min_password_length} characters long.")
    password = input("Enter a password: ")

# Print asterisks equal to the length of the password
print('*' * len(password))

