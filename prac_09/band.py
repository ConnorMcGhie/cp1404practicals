"""
CP1404 - Practical
Band class
"""


class Band:
    """Band class that stores a collection of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return the results of all musicians playing their first instrument."""
        return "\n".join(musician.play() for musician in self.musicians)
