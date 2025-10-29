import random # Used to generate a random ID for each student

class Student:
    def __init__(self, name, email, password):
        # Generate a random 6-digit ID (with leading zeros if needed)
        self.id = f"{random.randint(1, 999999):06d}"

        # Basic student information
        self.name = name
        self.email = email
        self.password = password

        # Initialize subjects list as empty
        self.subjects = []

    def to_dict(self):
        """
        Convert the Student object to a dictionary for easy storage or display.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'subjects': self.subjects
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Student object from a dictionary.
        Handles missing or malformed data using try-except.
        """
        try:
            # Extract necessary fields from dictionary
            student = Student(data['name'], data['email'], data['password'])
            # Override auto-generated ID with existing one from the dictionary
            student.id = data['id']
            # Get subjects list (or empty list if not found)
            student.subjects = data.get('subjects', [])
            return student
        except KeyError as e:
            print(f"Missing key in student data: {e}")
        except Exception as e:
            print(f"Unexpected error during student creation: {str(e)}")
        return None  # Return None if something goes wrong
