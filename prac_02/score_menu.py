"""
CP1404/CP5632 - Practical
Menu-driven program to work with scores
"""

import random


def get_valid_score():
    """Prompt the user until they enter a valid score (0–100 inclusive)."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score

def main():

    score = get_valid_score()
    print(score)

main()
