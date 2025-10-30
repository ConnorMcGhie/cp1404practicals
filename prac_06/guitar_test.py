"""
CP1404 - Practical
Guitar tests
"""
from prac_06.guitar import Guitar
CURRENT_YEAR = 2025


def run_tests():
    """Tests get_age and is_vintage methods in guitar class."""
    name = "Martin OM-28"
    year = 1931
    cost = 57478.30

    guitar = Guitar(name, year, cost)

    print(f"{guitar.name} get_age() - Expected {94}. Got {guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()
