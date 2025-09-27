"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def get_score_status(score):
    """Return the status string for the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    result = get_score_status(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.uniform(0, 100)
    print(f"\nRandom score: {random_score:.2f}")
    print(get_score_status(random_score))

main()
