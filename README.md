GUIUniApp / CLIUniApp – Student Enrolment System

A small University application implemented in **Python** with:

* **CLI APP** for **Student** and **Admin**
* **GUI APP** for **registered students**

All data is stored in a local JSON file: `students.data`.

## Project Overview 

* **Student (CLI)**: register (regex-validated), login, **enrol (max 4)**, **remove subject**, **change password**, **show enrolment** (marks, grades, average, PASS/FAIL).
* **Admin (CLI)**: **show all students**, **group by grade**, **partition PASS/FAIL**, **remove by ID**, **clear database**.
* **Data**: `Database` class creates/reads/writes `students.data`.
* **Models**: `Student` (6-digit id; name, email, password, subjects), `Subject` (3-digit id; random mark 25–100; grade computed).
* **GUI (GUIUniApp)**: login for registered students, **enrol (max 4)**, list subjects, show average & PASS/FAIL, messageboxes for invalid input/over-limit.

## System Requirements

* **Python 3.9+**
* **Tkinter** (bundled on Windows/macOS; on Debian/Ubuntu: `sudo apt-get install python3-tk`)
* No third-party packages required

## Installation & Setup

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Clone/download the project into a folder with these files:

```
AdminSystem.py
Colors.py
Database.py
EnrollmentSystem.py
GUI_APP.py
Main.py
StudentModel.py
StudentSystem.py
SubjectModel.py
students.data   # auto-created on first run if missing
```

## Configuration

* **Data path**: `Database(filepath='students.data')` (change if needed).
* **Max subjects**: enforced as **4** in enrol handlers.
* **Regex**: email must end with `@university.com`; password: starts with uppercase, ≥5 letters, then ≥3 digits.

## How to Run

### CLI entry

python Main.py

Follow on-screen menus:

* **University menu** → choose **(A)** Admin, **(S)** Student, **(X)** Exit
* **Student**: (l) login, (r) register, (x) exit
* **Subject Enrolment**: (c) change password, (e) enrol, (r) remove, (s) show, (x) exit
* **Admin**: (s) show, (g) group, (p) partition, (r) remove, (c) clear, (x) exit

### GUI (challenge task)

python GUI_APP.py

* **Login window**: enter registered email/password (from `students.data`).
* **Enrolment window**: **Enrol Subject** (auto id/mark/grade), **View Subjects** (list + average + PASS/FAIL), **Logout**.

## How to Use / Test (quick checklist)

* **Register & login (CLI)** → new student saved to `students.data`.
* **Enrol up to 4** subjects → 5th attempt shows warning.
* **Remove subject by ID**, **change password**, **show enrolment** → average updates, PASS/FAIL at 50.
* **Admin**:

  * Show all students (read from file)
  * Group by grade / Partition PASS vs FAIL
  * Remove a student by ID
  * Clear all data (writes empty list)
    
* **GUI**:

  * Incorrect credentials/empty fields → error dialog
  * Enrol > 4 → warning dialog
  * List shows `ID | Mark | Grade`, average (2 d.p.), PASS/FAIL

## Troubleshooting

* **`tkinter` not found**: install OS package (e.g., `sudo apt-get install python3-tk`).
* **Invalid JSON** in `students.data`: fix the JSON or delete the file (it will be recreated as `[]`).
* **Login fails**: ensure the student exists in `students.data` and password matches (demo uses plaintext).

## File Roles (brief)

* `Main.py` – CLI entry & menu routing
* `GUI_APP.py` – Tkinter UI (login/enrolment)
* `Database.py` – create/read/write/clear `students.data`
* `StudentModel.py` / `SubjectModel.py` – domain models + `to_dict()/from_dict()`
* `StudentSystem.py` / `AdminSystem.py` / `EnrollmentSystem.py` – CLI actions/handlers
* `Colors.py` – console colour codes (optional for CLI output)

