"""
Project Management - Project class
"""


class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is complete (100%)."""
        return self.completion == 100

    def starts_after(self, check_date):
        """Return True if the project starts after the given date."""
        return self.start_date > check_date
