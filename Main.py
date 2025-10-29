# Import necessary modules/classes
from StudentSystem import StudentSystem  # For managing student-related actions
from AdminSystem import AdminSystem # For managing admin-related actions
from Colors import  COLORS # For applying color styles in terminal output


# Define the main function which will control the whole system
def main():
    # Create instances for student and admin systems
    student_system = StudentSystem()
    admin_system = AdminSystem()

    # Main loop to keep the system running until user exits
    while True:
        # Prompt user to choose a system: Admin, Student, or Exit
        option = input(f"{COLORS['CYAN']}University System: (A)dmin, (S)tudent, or X: ").upper()
        if option == "A":
            # If user chooses Admin, run admin system
            admin_system.run()
        elif option == "S":
            # If user chooses Student, run student system
            student_system.run()
        elif option == "X":
            # If user chooses X, print a thank you message and exit the loop
            print(f"{COLORS['YELLOW']}Thank you")
            return
        else:
            # If the input is invalid (not A/S/X), show an error message
            print("\tInvalid choice.")


# Ensure this main function runs only when this file is executed directly
if __name__ == "__main__":
    main()
