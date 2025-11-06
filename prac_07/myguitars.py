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

    # Add new guitars
    print("\nAdd new guitars (press Enter to stop):")
    guitars.extend(get_new_guitars())

    # Save all guitars (existing + new) back to file
    save_guitars(filename, guitars)
    print(f"\nGuitars saved to {filename}")


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


def get_new_guitars():
    """Prompt the user to enter new guitars until they enter a blank name."""
    new_guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Write all guitars to the CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


# Run the main function
if __name__ == "__main__":
    main()
