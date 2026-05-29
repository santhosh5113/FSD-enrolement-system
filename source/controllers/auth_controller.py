from models.student import Student
from models.admin import Admin

class AuthController:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def register_student(self, name, email, password):
        student = Student(
            email=email,
            password=password,
            name=name
        )
        if not student.validate_email() or not student.validate_password():
            return { 
                    "success": False,
                    "message": f"Invalid email or password format" }
        if not student.validate_name(name):
            return {
                    "success": False,
                    "message": "Invalid name format (at least 2 letters, letters and spaces only)" }
        existing_student = self.data_manager.lookup_student_by_email(email)
        if existing_student: 
            return { 
                    "success": False,
                    "message": f"Student {existing_student.get_name()} already exists" }
        self.data_manager.add_student(student)
        self.data_manager.save_data()
        return {
                "success": True,
                "message":
                    f"\nEnrolling Student {student.get_name()}"
            }


    def login(self, email, password): 
        temp_student = Student(email=email, password=password, name="temp" ) 
        if not temp_student.validate_email() or not temp_student.validate_password(): 
            return { 
                    "success": False,  
                    "message": "Invalid email or password format" } 
        student = self.data_manager.verify_credentials(email, password)
        if student is None: 
            return { 
                    "success": False, 
                    "message": "Student does not exist" } 
        return { 
                "success": True, 
                "message": f"Email and password format acceptable\nWelcome {student.get_name()}", 
                "student": student 
                }

