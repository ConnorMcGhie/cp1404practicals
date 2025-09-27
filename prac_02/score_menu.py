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


def show_stars(score):
    """Print stars equal to the score (rounded to nearest int)."""
    print("*" * int(score))


def main():
    MENU = """\n(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_status(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell! Thanks for using the program.")



main()
