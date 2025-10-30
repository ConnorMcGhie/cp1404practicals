"""
CP1404 - Practical
EST completion: 45 minutes
Actual completion:
"""
CURRENT_YEAR = 2025
VINTAGE_AGE = 50


class Guitar:
    """Represent information related to a Guitar."""

    def __init__(self, name, year, cost):
        """Initialise guitar data."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate age of guitar based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is considered vintage."""
        return self.get_age() >= VINTAGE_AGE
