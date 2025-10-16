"""
Wimbledon champions data processor
"""

FILEDATA = "wimbledon.csv"


def main():
    """Read Wimbledon data and display champions and countries."""
    records = load_data(FILEDATA)
    champion_to_wins, countries = process_data(records)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read the Wimbledon CSV file and return a list of lists of its data."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_data(records):
    """
    Process the list of records to count champion wins and collect unique countries.
    Returns a dictionary {champion: wins} and a set of countries.
    """
    champion_to_wins = {}
    countries = set()
    for record in records:
        champion = record[2]
        country = record[1]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
        countries.add(country)
    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display champions with win counts and a sorted list of countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion:20} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
