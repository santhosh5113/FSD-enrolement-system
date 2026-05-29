from models.user import User

class Admin(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.name = "Admin"

    def view_students(self, data_manager):
        return data_manager.students

    def organize_by_grade(self, data_manager):
        grouped_students = {
            "HD": [],
            "D": [],
            "C": [],
            "P": [],
            "Z": []
        }
        students = data_manager.get_all_students()
        for student in students:
            grade = (student.calculate_average_grade())
            grouped_students[grade].append(student)
        return grouped_students

    def categorize_students(self, data_manager):
        categorized_students = {
            "PASS": [],
            "FAIL": []
        }
        students = data_manager.students
        for student in students:
            if student.is_passed():
                categorized_students["PASS"].append(student)
            else:
                categorized_students["FAIL"].append(student)
        return categorized_students

    def remove_student(self, student_id, data_manager):
        data_manager.remove_student(student_id)
        return True

    def clear_all_data(self, data_manager):
        data_manager.clear_all_data()
        return True

    def get_name(self):
        return self.name
