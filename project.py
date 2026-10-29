from datetime import date, datetime
import os
import csv
from tabulate import tabulate


CSV_FILE = "students.csv"
CSV_HEADERS = ["student", "date", "hours", "rate", "total", "status"]
def main():
    while True:
        print("MY STUDENTS")
        print("1. Add a new lesson")
        print("2. View all lessons")
        print("3. Search for a student")
        print("4. View student's statistics")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Select an option(1-6): ").strip()

        if choice == "1":
            add_session()
        elif choice == "2":
            view_session(CSV_FILE)
        elif choice == "3":
            search_session(CSV_FILE)
        elif choice == "4":
            view_statistics(CSV_FILE)
        elif choice == "5":
            delete_student(CSV_FILE)
        elif choice == "6":
            print("\nGoodbye\n")
            break
        else:
            print("\nInvalid choice\n")


def add_session():
    while True:
        name = input("Name of the student: ")
        try:
            cleaned = clean_name(name)
            break
        except ValueError as e:
            print(f"Error: {e}")
    while True:
        users_date = input("Enter date(YYYY-MM-DD) or press Enter for today: ")
        try:
            lesson_date = date_formatting(users_date)
            break
        except ValueError as e:
            print(f"Error: {e}")


    while True:
        try:
            hours = float(input("Enter duration in hours: "))
            rate = float(input("Enter hourly rate (₴): "))
            total = earnings(hours, rate)
            print(f"Lesson with {cleaned}: {total:.2f}")
            break
        except ValueError as e:
            print(f"Error: {e}")

    status_input = input("Paid? ").strip().lower()
    status = "Paid" if status_input in ["y", "yes", "yup"] else "Unpaid"

    session = {
        "student": cleaned,
        "date": lesson_date,
        "hours": hours,
        "rate": rate,
        "total": f"{total:.2f}",
        "status": status,
    }
    create_session(CSV_FILE, session)
    print(f"\nSaved: {cleaned} on {lesson_date} {total:.2f}₴ [{status}] to {CSV_FILE}\n")

def view_session(my_file):
    if not os.path.exists(my_file):
        print("\nNo lessons recorded yet\n")
        return
    with open(my_file, mode ="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    if not rows:
        print("\nNo lessons recorded yet\n")
        return
    print("\n" + tabulate(rows, headers="keys", tablefmt="grid")+"\n")


def search_session(my_file):
    if not os.path.exists(my_file):
        print("\nNo lessons recorded yet\n")
        return
    with open(my_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    if not rows:
        print("\nNo lessons recorded yet\n")
        return
    student_name= input("Student's name: ").strip()
    if not student_name:
        print("\nYou must enter student's name\n")
        return

    matches = [
        row for row in rows
        if row["student"].casefold() == student_name.casefold()
    ]
    if not matches:
        print(f"\nNo lessons found for {student_name}\n")
        return
    print(f"\nLessons for {student_name}:")
    print(tabulate(matches, headers="keys", tablefmt="grid"))
    print()

def view_statistics(my_file):
    if not os.path.exists(my_file):
        print("\nNo lessons recorded yet\n")
        return
    with open(my_file, mode ="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    if not rows:
        print("\nNo lessons recorded yet\n")
        return
    student_name = input("Enter student's name: ").strip()
    if not student_name:
        print("\nYou must enter a name\n")
        return
    lessons = [
        row for row in rows
        if row["student"].casefold() == student_name.casefold()
    ]

    if not lessons:
        print(f"\nNo lessons found for {student_name}\n")
        return
    total_earnings = 0.0
    paid_amount = 0.0
    unpaid_amount = 0.0

    for lesson in lessons:
        amount = float(lesson["total"])
        total_earnings = total_earnings+amount
        if lesson["status"] == "Paid":
            paid_amount+=amount
        elif lesson["status"] == "Unpaid":
            unpaid_amount+=amount
    print(f"\nStatistics for {lessons[0]['student']}")
    print("-" * 30)
    print(f"Number of lessons: {len(lessons)}")
    print(f"Total lesson value: {total_earnings:.2f} ₴")
    print(f"Already paid: {paid_amount:.2f} ₴")
    print(f"Still owed: {unpaid_amount:.2f} ₴\n")


def delete_student(my_file):
    if not os.path.exists(my_file):
        print("\nNo students found\n")
        return

    with open(my_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    student_name = input("Enter student's name to delete: ").strip()

    if not student_name:
        print("\nStudent's name cannot be empty\n")
        return

    matches = [
        row for row in rows
        if row["student"].casefold() == student_name.casefold()
    ]

    if not matches:
        print(f"\nNo lessons found for {student_name}\n")
        return

    print(f"\nFound {len(matches)} lesson(s) for {matches[0]['student']}.")
    confirm = input("Delete this student and all their lessons? (yes/no): ")

    if confirm.strip().casefold() != "yes":
        print("\nDeletion cancelled\n")
        return

    remaining_rows = [
        row for row in rows
        if row["student"].casefold() != student_name.casefold()
    ]

    with open(my_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(remaining_rows)

    print(f"\nDeleted {matches[0]['student']} and all their lessons\n")


def clean_name(name):
    cleaned =name.strip()
    if not cleaned:
        raise ValueError("You must enter student's name!")
    if not any(char.isalpha() for char in cleaned):
        raise ValueError("Student's name must contain letters")
    return cleaned.title()

#можливий випадок коли плата не стягується з учня. або урок не було проведено = 0 годин
def earnings(hours: float, rate: float) -> float:
    if hours < 0:
        raise ValueError("Lesson duration has to be more than 0")
    if rate < 0:
        raise ValueError("Lesson rate has to be more than 0")
    return round(hours*rate, 2)

def date_formatting(user_date):
    cleaned = user_date.strip()
    if not cleaned:
        return date.today().strftime("%Y-%m-%d")
    try:
        valid_date = datetime.strptime(cleaned, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Use YYYY-MM-DD format")
    return valid_date.strftime("%Y-%m-%d")

def create_session(my_file, session):

    existing_file = os.path.exists(my_file)
    empty_file = existing_file and os.path.getsize(my_file) == 0

    with open(my_file, mode="a", newline="", encoding = "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        if not existing_file or empty_file:
            writer.writeheader()
        writer.writerow(session)





if __name__ == "__main__":
    main()
