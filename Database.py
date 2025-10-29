import os # For checking if data file exists
import json # For reading/writing JSON data
from StudentModel import Student # Student model for conversion

class Database:
    def __init__(self, filepath='students.data'):
        # Set path where student data is stored
        self.filepath = filepath
        # Create empty file if it doesn't exist
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)

    def load_students(self):
        # Load student list from JSON file
        with open(self.filepath, 'r') as f:
            return [Student.from_dict(data) for data in json.load(f)]

    def save_students(self, students):
        # Save list of Student objects to JSON file
        with open(self.filepath, 'w') as f:
            json.dump([s.to_dict() for s in students], f, indent=4)

    def add_student(self, student):
        # Add new student to database
        students = self.load_students()
        students.append(student)
        self.save_students(students)

    def remove_student(self, student_id):
        # Remove student by ID, return True if success
        students = self.load_students()
        found_student = None

        for s in students:
            if s.id == student_id:
                found_student = s
                break
        if found_student:
            students.remove(found_student)
            self.save_students(students)
            return True
        else:
            return False

    def find_student(self, email, password=None):
        # Find student by email and optionally password
        students = self.load_students()
        for s in students:
            if s.email == email and (password is None or s.password == password):
                return s
        return None

    def update_student(self, updated_student):
        # Update existing student info by email
        students = self.load_students()
        for idx, s in enumerate(students):
            if s.email == updated_student.email:
                students[idx] = updated_student
                break
        self.save_students(students)
