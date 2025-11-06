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
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")

        choice = get_menu_choice()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
    if save_choice.startswith("y"):
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def get_menu_choice():
    """Display menu and get user choice."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
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


def save_projects(filename, projects):
    """Save projects to a tab-delimited text file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion}", file=out_file)


def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.starts_after(filter_date)]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(project)


def add_new_project(projects):
    """Prompt the user to add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    new_project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)


def update_project(projects):
    """Allow the user to update a project's completion or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_completion:
        project.completion = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
