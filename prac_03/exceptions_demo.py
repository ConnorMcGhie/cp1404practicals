"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError occurs when the user enters something that cannot be converted to an integer like "no"

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError occurs when the user enters 0 for the denominator, since division by zero is not possible.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, by checking that the denominator is not 0 before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Avoid ZeroDivisionError by checking denominator
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
