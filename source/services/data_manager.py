
import json

from pathlib import Path

from models.student import Student
from models.subject import Subject


PROJECT_ROOT = Path(__file__).parent.parent


class DataManager:
    def __init__(self):
        self.file_path = (PROJECT_ROOT / "data" / "students.data")
        self.students = []
        self.load_data()

    def load_data(self):
        self.students = []
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
            for student_dict in data.get("students",[]):
                student = self.load_student_object(student_dict)
                self.students.append(student)
        except FileNotFoundError:
            raise FileNotFoundError("students.data file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in students.data")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")
        return self.students


    def load_student_object(self, student_dict):
        enrolled_subjects = []
        for subject_dict in student_dict.get("subjects", []):
            subject = Subject(
                subject_id=subject_dict.get("subject_id"),
                mark=subject_dict.get("marks")
            )
            enrolled_subjects.append(subject)
        student = Student(
            email=student_dict.get("email"),
            password=student_dict.get("password"),
            student_id=student_dict.get("student_id"),
            name=student_dict.get("name"),
            enrolled_subjects=enrolled_subjects
        )
        return student



    def subject_to_dict(self, subject):
        return {
            "subject_id": subject.get_subject_id(),
            "marks": subject.get_marks(),
            "grade": subject.get_grade()
        }



    def get_all_students(self):
        return self.students

    def lookup_student_by_id(self, student_id):
        student_id = str(student_id).strip()
        for student in self.students:
            if (student.get_student_id() == student_id):
                return student
        return None
    
    def lookup_student_by_email(self, email):
        for student in self.students:
            if student.get_email() == email:
                return student
        return None

    def verify_credentials(self, email, password):
        student = self.lookup_student_by_email(email)
        if student is None:
            return None
        if student.get_password() == password:
            return student
        return None
    
    
    def student_to_dict(self, student):
        subjects = []
        for subject in student.get_enrolled_subjects():
            subjects.append(self.subject_to_dict(subject))
        return {
            "student_id": student.get_student_id(),
            "name": student.get_name(),
            "email": student.get_email(),
            "password": student.get_password(),
            "subjects": subjects
        }
        
    def save_data(self):
        data = {"students": []}
        try:
            for student in self.students:
                student_dict = (self.student_to_dict(student))
                data["students"].append(student_dict)
            with open(self.file_path, "w") as f:
                json.dump(data,f,indent=4)
        except Exception as e:
            raise RuntimeError(f"Error saving data: {e}")
        
    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        student = self.lookup_student_by_id(student_id)
        if student is None:
            raise ValueError("Student not found")
        self.students.remove(student)

    def update_student(self, updated_student):
        for index, student in enumerate(self.students):
            if (student.get_student_id()==updated_student.get_student_id()):
                self.students[index] = (updated_student)
                return
        raise ValueError("Student not found")

    def clear_all_data(self):
        self.students = []

