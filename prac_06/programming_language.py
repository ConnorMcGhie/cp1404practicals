"""
CP1404 - Practical
EST completion time: 30 minutes
Actual time:
"""


class ProgrammingLanguage:
    """Represent information related to a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Create programming language from given values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"
