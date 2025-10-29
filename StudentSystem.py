# Importing regex module for validating email and password formats
import re
# Importing the Student class which defines student attributes and behaviors
from StudentModel import Student
# Importing the Database class to interact with the student data (load, save, find, add, delete)
from Database import Database
# Importing the SubjectEnrolmentSystem, which manages subject registration after student login
from EnrollmentSystem import SubjectEnrolmentSystem
# Importing predefined color codes used to format terminal output (for visual clarity)
from Colors import  COLORS

# This class manages the main menu and handles student registration, login, and validation
class StudentSystem:
    def __init__(self):
        # Initialize the database handler when system starts
        self.db = Database()

    # Main user interface loop
    def run(self):
        while True:
            # Ask user to choose login (l), register (r), or exit (x)
            choice = input(f"{COLORS['CYAN']}\tStudent System: (l/r/x) : ").lower()

            if choice == 'l':
                # run login process
                self.login()
            elif choice == 'r':
                # run register process
                self.register()
            elif choice == 'x':
                break # Exit the loop and end the program
            else:
                print("\tInvalid option.")

    # Handles new student registration and input validation
    def register(self):
        print(f"{COLORS['GREEN']}\tStudent Sign Up {COLORS['RESET']}")

        # Loop to get valid email and password input
        while True:
            email = input(f"{COLORS['RESET']}\tEmail: ")
            password = input(f"{COLORS['RESET']}\tPassword: ")
            # Check email format using regex
            if not self.validate_email(email):
                print(f"{COLORS['RED']}\tIncorrect email or password format")
                continue
            # Check password format using regex
            if not self.validate_password(password):
                print(f"{COLORS['RED']}\tIncorrect email or password format")
                continue
            break # Input is valid; exit loop

        print(f"{COLORS['YELLOW']}\temail and password formats acceptable")

        # Check if a student with the same email already exists
        existStu = self.db.find_student(email)
        if existStu != None: # if existStu is not None
            print(f"{COLORS['RED']}\tStudent {existStu.name} already exists")
            return # Stop registration if email already in use

        # Prompt for student name and create a new Student object
        name = input(f"{COLORS['RESET']}\tName: ")
        student = Student(name,email, password)
        # Save the new student to the database
        self.db.add_student(student)
        print(f"{COLORS['YELLOW']}\tEnrolling Student {student.name}")

    # Handles login process and launches subject enrollment if credentials are correct
    def login(self):
        print(f"{COLORS['GREEN']}\tStudent Sign In {COLORS['RESET']}")
        while True:
            try:
                # Ask for user input
                email = input(f"{COLORS['RESET']}\tEmail: ")
                password = input(f"{COLORS['RESET']}\tPassword: ")
                # Validate email
                if not self.validate_email(email):
                    print(f"{COLORS['RED']}\tIncorrect email or password format")
                    continue
                # Validate password format
                if not self.validate_password(password):
                    print(f"{COLORS['RED']}\tIncorrect email or password format")
                    continue
                break  # exit input loop when everything is valid
            except Exception as e:
                print(f"{COLORS['RED']}\tUnexpected error: {str(e)}")

        print(f"{COLORS['YELLOW']}\temail and password formats acceptable")

        # Attempt to find student with matching email and password
        student = self.db.find_student(email, password)
        if student:
            # Launch subject enrollment interface if login is successful
            SubjectEnrolmentSystem(student).run()
        else:
             print(f"{COLORS['RED']}\tStudent does not exist")

    # Email validation using regex to enforce pattern like john.doe@university.com
    def validate_email(self, email):
        return re.fullmatch(r'[a-z]+\.[a-z]+@university\.com', email)

    # Password validation using regex:
    # - Must start with an uppercase letter
    # - Followed by at least 4 letters (upper or lower case)
    # - Ends with at least 3 digits
    def validate_password(self, password):
        return re.fullmatch(r'[A-Z][a-zA-Z]{4,}[0-9]{3,}', password)
