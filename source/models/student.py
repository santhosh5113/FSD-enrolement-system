from models.user import User
from models.subject import Subject

import random


class Student(User):
    def __init__(self, email, password, name, student_id=None, enrolled_subjects=None):
        super().__init__(email, password)
        self.name = name
        self.student_id = student_id if student_id is not None else self.autogenerate_student_id()
        if enrolled_subjects is None:
            self.enrolled_subjects = []  
        else:
            self.enrolled_subjects = enrolled_subjects
    
    def autogenerate_student_id(self):
            return str(random.randint(1, 999999)).zfill(6)
    
    def enroll_subject(self, subject=None): 
        if self.check_Subject_limit(): 
            return None 
        if subject is None: 
            subject = Subject() 
        self.enrolled_subjects.append(subject) 
        return subject.get_subject_id()
    
    def lookup_subject(self, subject_id):
        for subject in self.enrolled_subjects:
            if subject.get_subject_id() == subject_id:
                return subject
        return None
    
    def remove_subject(self, subject_id): 
        subject = self.lookup_subject(subject_id) 
        if subject is None: 
            return None 
        self.enrolled_subjects.remove(subject) 
        return subject
    
    def check_Subject_limit(self):
        if len(self.enrolled_subjects) >= 4:
            return True
        return False
    
    def change_password(self, new_password):
        old_password = self._password 
        self._password = new_password 
        if self.validate_password(): 
            return True 
        self._password = old_password 
        return False
    
    def calculate_average_mark(self): 
        if not self.enrolled_subjects: 
            return 0 
        total = 0 
        for subject in self.enrolled_subjects: 
            total += subject.get_marks() 
        return total / len(self.enrolled_subjects) 
    
    def calculate_average_grade(self):
        average = self.calculate_average_mark()
        if average < 50:
            return "Z"
        elif average < 65:
            return "P"
        elif average < 75:
            return "C"
        elif average < 85:
            return "D"
        return "HD"
    
    def is_passed(self): 
        if self.calculate_average_mark() < 50: 
                return False 
        return True
    
    def __str__(self):
        subjects = ""
        for subject in self.enrolled_subjects:
            subjects += f"\n  - {subject}"
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self._email}, Enrolled Subjects: {subjects}"
    
    # getters
    def get_name(self):
        return self.name
    
    def get_student_id(self):
        return self.student_id
    
    def get_email(self):
        return self._email
    
    def get_password(self):
        return self._password
    
    def get_enrolled_subjects(self): 
        return self.enrolled_subjects