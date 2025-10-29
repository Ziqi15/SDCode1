import re
from Colors import  COLORS
from SubjectModel import Subject # Subject class for subject creation
from Database import Database # Database handler for saving student info

class SubjectEnrolmentSystem:
    def __init__(self, student):
        """
        Constructor for SubjectEnrolmentSystem.
        Assigns a student object and initializes a database connection.
        """
        self.student = student
        self.db = Database()

    def run(self):
        """
        Runs the main interaction loop for the student menu.
        Accepts user choices and calls relevant functions.
        """
        while True:
            choice = input(f"{COLORS['CYAN']}\t\tStudent Course Menu (c/e/r/s/x): ").lower()

            if choice == 'c': # run change password
                self.change_password()
            elif choice == 'e': # run enrol subject
                self.enrol_subject()
            elif choice == 'r': # run remove subject
                self.remove_subject()
            elif choice == 's': # run show enrolled subjects
                self.show_subjects()
            elif choice == 'x': # exit the system
                self.db.update_student(self.student)
                break
            else:
                print("Invalid choice.")

    def change_password(self):
        """
        Handles the process of updating a student’s password
        including input, validation, confirmation, and saving.
        """
        print(f"{COLORS['YELLOW']}\t\tUpdating password")

        while True:
            # Step 1: Ask for new password
            new_pass = input(f"{COLORS['RESET']}\t\tNew password: ")

            if not self.validate_password(new_pass):
                print(f"{COLORS['RED']}\t\tIncorrect password format. Please try again.")
                continue  # Go back to ask for a new password

            # Step 2: Confirm password (only after format is correct)
            while True:
                confirm_pass = input(f"{COLORS['RESET']}\t\tConfirm password: ")

                if new_pass != confirm_pass:
                    print(f"{COLORS['RED']}\t\tPasswords do not match - try again.")
                    continue  # Only repeat confirm step
                else:
                    break  # Passwords match, proceed

            break  # Exit both loops

        # Step 3: Update student password
        self.student.password = new_pass
        self.db.update_student(self.student)
        print(f"{COLORS['YELLOW']}\t\tPassword updated successfully.")

    def validate_password(self, password):
        """
        Validates the format of the password:
        At least 1 uppercase, 4+ lowercase letters, and 3+ digits.
        """
        return re.fullmatch(r'[A-Z][a-zA-Z]{4,}[0-9]{3,}', password)

    def enrol_subject(self):
        """
        Allows a student to enroll in a subject.
        Prevents enrollment if already enrolled in 4 subjects.
        Handles errors using try-except.
        """
        if len(self.student.subjects) >= 4:
            print(f"{COLORS['RED']}\t\tStudent are allowed to enrol in 4 subjects only")
            return

        try:
            new_subject = Subject()  # Create a new Subject instance
            self.student.subjects.append(new_subject.to_dict())  # Add to student's subject list
            print(f"{COLORS['YELLOW']}\t\tEnrolled in {new_subject}")
            print(f"{COLORS['YELLOW']}\t\tYou are now enrolled in {len(self.student.subjects)} out of 4 subjects")
            self.db.update_student(self.student)  # Save updated student to DB
        except Exception as e:
            print(f"{COLORS['RED']}\t\tError enrolling subject: {e}")

    def remove_subject(self):
        """
        Allows a student to remove a subject using subject ID.
        If subject ID is not found, shows error message.
        """
        if not self.student.subjects:
            print(f"{COLORS['RED']}\t\tNo subjects to remove.")
            return

        subj_id = input(f"{COLORS['RESET']}\t\tRemove subject by ID: ")
        found_subject = None

        for subject in self.student.subjects:
            if subject["id"] == subj_id:
                found_subject = subject
                break

        if found_subject is not None:
            print(f"{COLORS['YELLOW']}\t\tDropping Subject-{found_subject['id']}")
            self.student.subjects.remove(found_subject)
            self.db.update_student(self.student)
            print(f"{COLORS['YELLOW']}\t\tYou are now enrolled in {len(self.student.subjects)} out of 4 subjects")
        else:
            print(f"{COLORS['RED']}\t\tSubject ID not found.")

    def show_subjects(self):
        """
        Displays all subjects a student is currently enrolled in.
        """
        print(f"{COLORS['YELLOW']}\t\tShowing {len(self.student.subjects)} subjects")
        for s in self.student.subjects:
            print(f"{COLORS['RESET']}\t\t[Subject::{s['id']} -- mark = {s['mark']} -- grade = {s['grade']}]")

