# Import the random module to generate random values for subject ID and marks
import random

# Define a class to represent a subject that a student can be enrolled in
class Subject:
    def __init__(self):
        # Generate a random 3-digit subject ID (e.g., "007", "345")
        self.id = f"{random.randint(1, 999):03d}"
        # Generate a random mark between 25 and 100
        self.mark = random.randint(25, 100)
        # Determine the grade (e.g., HD, D, C, P, F) based on the mark
        self.grade = self.calculate_grade(self.mark)

    # Convert the Subject object to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'mark': self.mark,
            'grade': self.grade
        }

    # String representation of the Subject object
    def __str__(self):
        return f"Subject-{self.id}"

    # Create a Subject object from a dictionary
    @staticmethod
    def from_dict(data):
        try:
            subj = Subject()
            subj.id = data['id']
            subj.mark = data['mark']
            subj.grade = data['grade']
            return subj
        except KeyError as e:
            print(f"Missing field in subject data: {e}")
            return None

    # Static method to calculate a letter grade from a numerical mark
    @staticmethod
    def calculate_grade(mark):
        if mark >= 85:
            return 'HD'
        elif mark >= 75:
            return 'D'
        elif mark >= 65:
            return 'C'
        elif mark >= 50:
            return 'P'
        else:
            return 'F'


'''

To get full mark, you need apply Try Except for Student, Subject, Admin Class
'''