# subject_data_v2.py
"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects_data = load_data(FILENAME)
    display_subject_details(subjects_data)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects_data):
    """Display each subject’s details neatly."""
    for subject in subjects_data:
        print("{} is taught by {:12} and has {:3} students".format(*subject))

main()
