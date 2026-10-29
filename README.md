# Tutoring tracker
#### Description:
**Tutoring tracker** is a Python-based command-line tool designed to help tutors, mostly freelance tutors, manage their lessons with students, track financial balances, organize tutoring session records efficiently without relying on manual spreadsheets.
## Why I created this project?
Freelance educators frequently manage multiple students with diverse scheduling constraints, custom hourly rates, and inconsistent payment patterns. Many students pay per class, some students settle balances in bulk at the end of a month.

Tutors often use scattered paper notes, messenger chats, complex accounting software, or just memorize everything. This project solves that operational bottleneck and provides a lightweight and robust solution. I created this project to make it easier to organize lessons, calculate their costs, and keep track of unpaid balances without doing these calculations manually. It uses a simple text-based menu, making it easy to operate directly from the terminal.
## Features
The application provides six menu options. The user can add a new lesson by entering the student's name, lesson date, duration, hourly rate, and payment status. If no date is entered, the program automatically uses the current date. The user can also view all recorded lessons in a formatted table or search for lessons by student name.

The statistics feature calculates the total value of a student's lessons, the amount already paid, and the outstanding balance. This makes it easier to identify how much a particular student still owes. The delete feature removes all lesson records associated with a selected student after confirmation. The final menu option allows the user to exit the program.

## Project files
### project.py
Contains the main code of the program.

The `main()` function displays the menu and directs the user's choices to the appropriate functions. `add_session()` collects lesson information, while `clean_name()` validates and formats student names. The `date_formatting()` function validates dates and uses the current date when no date is provided. The `earnings()` function calculates lesson costs based on duration and hourly rate.
The program also includes functions for storing and displaying lesson records. `create_session()` saves lesson data to a CSV file, `view_session()` displays all records, and `search_session()` finds lessons associated with a particular student. `view_statistics()` calculates the total value of a student's lessons, the amount already paid, and the outstanding balance. Finally, `delete_student()` removes all lesson records associated with a selected student after confirmation.

### test_project.py
Contains automated tests written with pytest.

The tests cover `clean_name()`, `earnings()`, and `date_formatting()`. They check valid inputs, expected results, and invalid inputs that should raise `ValueError`. These tests help verify that important parts of the application behave as expected.

### requirements.txt
Lists the external Python packages needed to run the program and its tests, including `tabulate`.

### students.csv
Stores lesson records between program runs. Each record contains the student's name, lesson date, duration, hourly rate, total cost, and payment status. The file is created automatically when the first lesson is saved.
### README.md
Documents the project's purpose, functionality, installation instructions, design choices, and testing process.

## Design choice
I chose a command-line interface because it is straightforward to implement and allows me to focus on Python fundamentals.
I separated the program into functions to make the code easier to understand, maintain, and test. I also used the tabulate library to present lesson records in a readable table.

Payment status is stored separately from lesson cost because a lesson's cost does not indicate whether the student has paid. This distinction allows the program to calculate outstanding balances. The program also asks for confirmation before deleting a student's records to help prevent accidental data loss.

## How to use
- Download the project files and save them in a folder on your computer.
- Open a terminal in the project folder.
- Install the required dependencies:
```bash
python -m pip install -r requirements.txt
```
- Run the program:
```bash
python project.py
```
Follow the menu displayed in the terminal to manage lessons and student records.

**Dates should be entered in YYYY-MM-DD format, or the user can press ***Enter*** to use the current date.**

## Testing
Run the automated tests with:
```bash
pytest test_project.py
```
The tests verify name validation, lesson-cost calculations, and date formatting. They include both valid and invalid inputs, helping ensure that these functions handle common cases correctly.
