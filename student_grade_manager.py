"""
Student Grade Manager
----------------------
A simple console app to add students, record their grades,
calculate averages/letter grades, and save/load data to a file.
"""

import json
import os

DATA_FILE = "students_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ Data saved successfully.\n")


def add_student(data):
    name = input("Enter student name: ").strip()
    if name in data:
        print("⚠️ Student already exists.\n")
        return
    data[name] = []
    print(f"✅ Student '{name}' added.\n")


def add_grade(data):
    name = input("Enter student name: ").strip()
    if name not in data:
        print("⚠️ Student not found.\n")
        return
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <= 100:
            data[name].append(grade)
            print(f"✅ Grade {grade} added for {name}.\n")
        else:
            print("⚠️ Grade must be between 0 and 100.\n")
    except ValueError:
        print("⚠️ Invalid number entered.\n")


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def view_report(data):
    if not data:
        print("⚠️ No students found.\n")
        return
    print("\n===== STUDENT REPORT =====")
    for name, grades in data.items():
        avg = calculate_average(grades)
        letter = letter_grade(avg)
        grades_str = ", ".join(str(g) for g in grades) if grades else "No grades yet"
        print(f"Name: {name}")
        print(f"  Grades: {grades_str}")
        print(f"  Average: {avg:.2f}")
        print(f"  Letter Grade: {letter}\n")


def delete_student(data):
    name = input("Enter student name to delete: ").strip()
    if name in data:
        del data[name]
        print(f"✅ Student '{name}' deleted.\n")
    else:
        print("⚠️ Student not found.\n")


def show_menu():
    print("===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Report")
    print("4. Delete Student")
    print("5. Save and Exit")


def main():
    data = load_data()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        print()
        if choice == "1":
            add_student(data)
        elif choice == "2":
            add_grade(data)
        elif choice == "3":
            view_report(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            save_data(data)
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
