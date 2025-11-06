"""
Project Management Program
Estimated time: 1.5 hours
"""


from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"


def main():
    """Main program for managing projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = get_menu_choice()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "D":
            display_projects(projects)
        else:
            print("Invalid choice")

        choice = get_menu_choice()
    print("Thank you for using custom-built project management software.")


def get_menu_choice():
    """Display menu and get user choice."""
    print("- (L)oad projects")
    print("- (D)isplay projects")
    print("- (Q)uit")
    return input(">>> ").upper()


def load_projects(filename):
    """Load projects from a tab-delimited text file."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            if len(parts) < 5:
                continue
            name, start_date_str, priority, cost_estimate, completion = parts
            start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
            projects.append(project)
    return projects


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


if __name__ == "__main__":
    main()
