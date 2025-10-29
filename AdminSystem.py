# Import necessary classes and modules
from SubjectModel import Subject # For grade calculation
from Database import Database # To interact with student data
from Colors import  COLORS # For colorful terminal output

class AdminSystem:
    def __init__(self):
        # Initialize the Admin System with a Database instance
        self.db = Database()

    def run(self):
        # Main loop to continuously accept user input until exit
        while True:

            choice = input(f"{COLORS['CYAN']}\tAdmin System (c/g/p/r/s/x) : ").lower()

            if choice == 's': # run show all students
                self.show_all_students()
            elif choice == 'r': # run remove students
                self.remove_student()
            elif choice == 'g': # run group students by grade
                self.group_students()
            elif choice == 'p': # run group students by pass and fail
                self.partition_students()
            elif choice == 'c': # run clear all student data
                self.clear_all_data()
            elif choice == 'x': # exit the system
                break
            else:
                print("Invalid option.")

    def show_all_students(self):
        """
        Display all students from the database.
        If there is an error (e.g., data corruption), handle it gracefully.
        """
        try:
            students = self.db.load_students()
            print(f"{COLORS['YELLOW']}\tStudent List")
            if not students:
                print(f"{COLORS['RESET']}\t\t<Nothing to Display>")
                return
            for s in students:
                print(f"{COLORS['RESET']}\t{s.name} :: {s.id} --> Email: {s.email}")
        except Exception as e:
            print(f"{COLORS['RED']}\tUnexpected error in show_all_students(): {str(e)}")

    def remove_student(self):
        """
        Ask for student ID and remove the student from the database if exists.
        """
        student_id = input(f"{COLORS['RESET']}\tRemove student by ID: ")
        if self.db.remove_student(student_id):
            print(f"{COLORS['YELLOW']}\tRemoving Student {student_id} Account{COLORS['RESET']}")
        else:
            print(f"{COLORS['RED']}\tStudent {student_id} does not exist{COLORS['RESET']}")

    def group_students(self):
        """
        Group students based on calculated average grade into HD, D, C, P, or F.
        """
        students = self.db.load_students()
        print(f"{COLORS['YELLOW']}\tGrade Grouping")
        if not students:
            print(f"{COLORS['RESET']}\t\t\t<Nothing to Display>")
            return
        # Setup grade groups
        grade_groups = {'HD': [], 'D': [], 'C': [], 'P': [], 'F': []}
        # Process each student
        for s in students:
            marks = [float(subj['mark']) for subj in s.subjects]
            if not marks:
                continue  # Skip students with no subjects
            avg_mark = sum(marks) / len(marks)
            grade = Subject.calculate_grade(avg_mark)
            grade_groups[grade].append((s.name, s.id, grade, avg_mark))
        # Display grouped students
        for grade, entries in grade_groups.items():
            if entries:
                for name, student_id, grade_letter, mark in entries:
                    print(
                        f"{COLORS['RESET']}\t{grade}  --> [{name} :: {student_id} --> GRADE:  {grade_letter} - MARK: {mark:.2f}]{COLORS['RESET']}")

    def partition_students(self):
        """
        Separate students into PASS (avg >= 50) and FAIL groups.
        """
        print(f"{COLORS['YELLOW']}\tPASS/FAIL Partition")
        students = self.db.load_students()
        pass_list = []
        fail_list = []

        for s in students:
            if not s.subjects:
                continue
            avg = sum(subj['mark'] for subj in s.subjects) / len(s.subjects)
            grade = Subject.calculate_grade(avg)
            if avg >= 50:
                pass_list.append(f"{s.name} :: {s.id} --> GRADE:  {grade} - MARK: {avg:.2f}]")
            else:
                fail_list.append(
                    f"{s.name} :: {s.id} --> GRADE:  {grade} - MARK: {avg:.2f}]")

        print(f"{COLORS['RESET']}\tFAIL --> ", end='')
        print(fail_list)

        print(f"{COLORS['RESET']}\tPASS --> ", end='')
        print(pass_list)


    def clear_all_data(self):
        """
        Clear all student data in the database after user confirmation.
        """
        print(f"{COLORS['YELLOW']}\tClearing students database")
        confirm = input(f"{COLORS['RED']}\tAre you sure you want to clear the database (Y)ES/(N)O: ")
        if confirm.upper() == 'Y':
            print(f"{COLORS['YELLOW']}\tStudents data cleared")
            self.db.load_students()
            self.db.save_students([])
        else:
            return
