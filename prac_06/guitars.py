"""
CP1404 - Practical
Guitar program.
"""
from prac_06.guitar import Guitar


def main():
    """Guitar program that asks user to input guitar information and uses Guitar class to display data."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars to display.")


main()
