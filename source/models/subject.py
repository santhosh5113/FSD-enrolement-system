import random

class Subject:
    def __init__(self, subject_id=None, mark=None):
        self.subject_ID = subject_id or self.generate_subject_id()
        self.mark = mark if mark is not None else self.generate_mark()
        self.grade = self.calculate_grade()
    
    def generate_subject_id(self):
        return str(random.randint(1, 999)).zfill(3)
    
    def generate_mark(self):
        # Generate random mark between 25 and 100
        return random.randint(25, 100)

    def calculate_grade(self):
        # Convert mark to grade (Z, P, C, D, HD)
        if self.mark < 50:
            return "Z"
        elif self.mark < 65:
            return "P"
        elif self.mark < 75:
            return "C"
        elif self.mark < 85:
            return "D"
        else:
            return "HD"
        
    def get_subject_id(self):
        return self.subject_ID

    def get_marks(self):
        return self.mark
    
    def get_grade(self):
        return self.grade
    
    def __str__(self):
        return f"Subject: {self.subject_ID} - Mark: {self.mark} - Grade: {self.grade}"

