import tkinter as tk # GUI library for building windows and forms
from tkinter import messagebox # Tkinter popup dialogs
from Database import Database # Custom database module for storing student data
from SubjectModel import Subject # Subject class for handling subject-related logic

class GUIUniApp:
    def __init__(self):
        # Initialize database and GUI root window
        self.db = Database()
        self.current_student = None
        self.root = tk.Tk()
        self.root.title("GUIUniApp - Login")
        self.create_login_window()
        self.root.mainloop()

    def create_login_window(self):
        self.clear_window() # Clear previous widgets
        # Display login form
        tk.Label(self.root, text="Student Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Email:").pack()
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack()

        # Login button
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        # Retrieve and clean input
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        # Attempt to find student in database
        student = self.db.find_student(email, password)
        if student:
            self.current_student = student
            self.create_enrolment_window()
        else:
            messagebox.showerror("Login Failed", "Incorrect email or password.")

    def create_enrolment_window(self):
        self.clear_window()
        self.root.title("Subject Enrolment")
        # Welcome label
        tk.Label(self.root, text=f"Welcome, {self.current_student.name}", font=("Arial", 14)).pack(pady=10)
        # Subject name entry field
        self.subject_name_entry = tk.Entry(self.root, width=30)
        self.subject_name_entry.pack()
        self.subject_name_entry.insert(0, "Enter subject name...")
        # Buttons for enrolment and subject display
        tk.Button(self.root, text="Enrol Subject", command=self.enrol_subject).pack(pady=5)
        tk.Button(self.root, text="View Subjects", command=self.show_subjects).pack(pady=5)
        # Display area
        self.subject_display = tk.Text(self.root, height=10, width=50)
        self.subject_display.pack(pady=10)
        # Logout button
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=5)

    def enrol_subject(self):
        # Prevent enrolling in more than 4 subjects
        if len(self.current_student.subjects) >= 4:
            messagebox.showwarning("Limit Reached", "You can only enrol in 4 subjects.")
            return
        # Validate subject name input
        name = self.subject_name_entry.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Subject name cannot be empty.")
            return

        # Create and save subject
        subject = Subject()
        self.current_student.subjects.append(subject.to_dict())
        self.db.update_student(self.current_student)

        messagebox.showinfo("Success", f"Enrolled in {name} (Mark: {subject.mark}, Grade: {subject.grade})")
        self.show_subjects()

    def show_subjects(self):
        self.subject_display.delete("1.0", tk.END)
        if not self.current_student.subjects:
            self.subject_display.insert(tk.END, "No subjects enrolled yet.\n")
            return

        total = 0
        for subj in self.current_student.subjects:
            line = f"{subj['id']} |  Mark: {subj['mark']} | Grade: {subj['grade']}\n"
            self.subject_display.insert(tk.END, line)
            total += subj['mark']
        # Show average and pass/fail
        avg = total / len(self.current_student.subjects)
        self.subject_display.insert(tk.END, f"\nAverage Mark: {avg:.2f}\n")
        self.subject_display.insert(tk.END, "Status: PASS\n" if avg >= 50 else "Status: FAIL\n")

    def logout(self):
        self.current_student = None
        self.root.title("GUIUniApp - Login")
        self.create_login_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    GUIUniApp()
