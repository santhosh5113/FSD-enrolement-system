
from services.data_manager import DataManager

from controllers.auth_controller import AuthController
from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController

from models.admin import Admin


class CLIUniApp:
    def __init__(self):
        self.data_manager = DataManager()
        self.auth_controller = AuthController(self.data_manager)
        self.student_controller = StudentController(self.data_manager)
        self.admin_controller = AdminController(self.data_manager)
        self.current_user = None

    def start(self):
        while True:
            print("\n\033[34mUniversity System")
            print("(A) Admin")
            print("(S) Student")
            print("(X) Exit")
            choice = input("Enter your choice: \033[0m").lower()
            match choice:
                case "a":
                    self.admin_menu()
                case "s":
                    self.student_menu()
                case "x":
                    print("\033[33mThank you!\033[0m")
                    break
                case _:
                    print("Invalid option.")

    def student_menu(self):
        while True:
            print("\n\033[34mStudent System")
            print("(l) login")
            print("(r) register")
            print("(x) exit")
            choice = input("Enter your choice: \033[0m").lower()
            match choice:
                case "l": self.handle_login()
                case "r": self.handle_register()
                case "x": break
                case _: print("Invalid option.")

    def handle_register(self):
        print("\nStudent Sign Up")
        while True:
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            result = self.auth_controller.register_student(name,email,password)
            if result["success"]:
                print(f"\033[33m{result['message']}\033[0m")
                break
            else:
                print(f"\033[31m{result['message']}\033[0m")


    def handle_login(self):
        print("\n\033[32mStudent Sign In\033[0m")
        while True:
            email = input("Email: ")
            password = input("Password: ")
            result = self.auth_controller.login(email,password)
            if not result["success"]:
                print(f"\033[31m{result['message']}\033[0m")
                continue
            self.current_user  = result["student"]
            print(f"\033[33m{result['message']}\033[0m")
            self.subject_enrolment_menu()
            break

    def subject_enrolment_menu(self):
        while True:
            print("\n\033[34mSubject Enrolment System")
            print("(c) change password")
            print("(e) enrol subject")
            print("(r) remove subject")
            print("(s) show subjects")
            print("(x) exit")
            choice = input("Enter your choice: \033[0m").lower()
            match choice:
                case "c": self.change_password()
                case "e": self.enrol_subject()
                case "r": self.remove_subject()
                case "s": self.show_subjects()
                case "x": 
                    self.current_user = None
                    break
                case _: print("Invalid option.")

    def enrol_subject(self):
        result = self.student_controller.enroll_subject(self.current_user)
        if result["success"]:
            print(f"\033[33m{result['message']}\033[0m")
        else:
            print(f"\033[31m{result['message']}\033[0m")
            
    def remove_subject(self):
        input_subject_id = input("Remove Subject by ID: ")
        result = self.student_controller.remove_subject(self.current_user, input_subject_id)
        if result["success"]:
            print(f"\033[33m{result['message']}\033[0m")
        else:
            print(f"\033[31m{result['message']}\033[0m")
            
    def show_subjects(self):
        subjects = self.student_controller.show_subjects(self.current_user)
        if not subjects:
            print("\033[33mShowing 0 subjects.\033[0m")
            return
        print(f"\n\033[33mShowing {len(subjects)} subjects.\033[0m")
        for subject in subjects:
            print(subject)

    def change_password(self):
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm password: ")
        while new_password != confirm_password:
            print(f"\033[31mPassword does not match - Try again\033[0m")
            confirm_password = input("Confirm password: ")
        result = self.student_controller.change_password(self.current_user,new_password)
        if result["success"]:
            print(f"\033[33m{result['message']} \033[0m")
        else:
            print(f"\033[31m{result['message']} \033[0m")
        

    def admin_menu(self):
        admin = Admin(
            email="admin@university.com",
            password="Admin123"
        )
        while True:
            print("\n\033[34mAdmin System")
            print("(c) clear database")
            print("(g) group students")
            print("(p) partition students")
            print("(r) remove student")
            print("(s) show students")
            print("(x) exit")
            choice = input("Enter your choice: \033[0m").lower()
            match choice:
                case "c": self.clear_database(admin)
                case "g": self.group_students(admin)
                case "p": self.partition_students(admin)
                case "r": self.remove_student(admin)
                case "s": self.show_students(admin)
                case "x": break
                case _: print("Invalid option.")

    def show_students(self, admin):
        students = self.admin_controller.view_students(admin)
        if not students:
            print("\033[31mNo students found.\033[0m")
            return
        print("\033[33mStudents List.\033[0m")
        for student in students:
            print(f"{student['name']} :: {student['id']} --> Email: {student['email']}")


    def group_students(self, admin):
        grouped_students = self.admin_controller.organize_by_grade(admin)
        print("\n\033[33mGrouped Students\033[0m")
        for grade, students in grouped_students.items():
            print(f"\n{grade}:")
            if not students:
                print("No students found.")
                continue
            for student in students:
                print(f"{student['name']} :: {student['id']} --> Grade: {student['grade']} - Mark: {student['mark']:.2f}")




    def partition_students(self, admin):
        partitioned_students = self.admin_controller.categorize_students(admin)
        print("\n\033[33mPASS/FAIL Partition\033[0m")
        for group, students in partitioned_students.items():
            print(f"\n{group}:")
            if not students:
                print("No students found.")
                continue
            for student in students:
                print(f"{student['name']} :: {student['id']} --> Grade: {student['grade']} - Mark: {student['mark']:.2f}")


    def remove_student(self, admin):
        student_id = input("Enter student ID: ")
        result = self.admin_controller.remove_student(admin,student_id)   
        if result["success"]:
            print(f"\033[33m{result['message']} \033[0m")
        else:
            print(f"\033[31m{result['message']} \033[0m")
        

    def clear_database(self, admin):
        confirm = input("\033[31mAre you sure you want to clear all data? (y/n): \033[0m").lower()
        if confirm != "y":
            print(f"\033[33mDatabase clear cancelled\033[0m")
            return
        result = self.admin_controller.clear_all_data(admin)
        print(f"\033[31m{result['message']} \033[0m")

