# Kristian Wareing
# 07/12/2026
# CSD-325 Module 8 Assignment
# Purpose: Load student records from a JSON file, print them, append a new
#          student to the list, and write the updated list back to the file.

import json
import os

# Build the path to student.json based on where this script lives, so the
# program works no matter which directory it is launched from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(SCRIPT_DIR, "student.json")


def print_students(student_list):
    """Loop through the student list and print each record on one line."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


def main():
    """Read the file, show the original list, append a student, save the file."""

    # Load the JSON file into a Python list of dictionaries.
    with open(FILE_NAME, "r") as input_file:
        students = json.load(input_file)

    # Show the list exactly as it was loaded from the file.
    print("\nOriginal Student list:")
    print_students(students)

    # Add a new student record to the end of the list.
    new_student = {
        "F_Name": "Kristian",
        "L_Name": "Wareing",
        "Student_ID": 45832,
        "Email": "kwareing@my365.bellevue.edu",
    }
    students.append(new_student)

    # Show the list again now that the new record has been added.
    print("\nUpdated Student list:")
    print_students(students)

    # Write the updated list back out to the JSON file.
    with open(FILE_NAME, "w") as output_file:
        json.dump(students, output_file, indent=4)

    print("\nThe student.json file has been updated.")


if __name__ == "__main__":
    main()
