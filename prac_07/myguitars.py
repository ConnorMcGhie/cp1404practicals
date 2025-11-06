"""
CP1404 - Practical
More Guitars
"""

from guitar import Guitar


def main():
    """Main program to manage guitar data."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are my guitars:")
    display_guitars(guitars)

    # Sort by year (old first)
    guitars.sort()
    print("\nSorted by year (oldest to newest):")
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display all guitars neatly formatted."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_string}")


# Run the main function
if __name__ == "__main__":
    main()
