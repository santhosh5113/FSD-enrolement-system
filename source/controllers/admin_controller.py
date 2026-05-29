class AdminController:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        
    def view_students(self, admin):
        students = admin.view_students(self.data_manager ) 
        result = [] 
        for student in students: 
            result.append({ 
                           "name": student.get_name(),
                           "id": student.get_student_id(),
                           "email": student.get_email() }) 
        return result

    def organize_by_grade(self, admin): 
        grouped_students = admin.organize_by_grade(self.data_manager)
        result = {} 
        for grade, students in grouped_students.items():
            result[grade] = [] 
            for student in students: 
                result[grade].append({ 
                                      "name": student.get_name(), 
                                      "id": student.get_student_id(), 
                                      "grade": student.calculate_average_grade(), 
                                      "mark": student.calculate_average_mark() }) 
        return result
    
    def categorize_students(self, admin):
        categorized_students = admin.categorize_students(self.data_manager)
        result = {} 
        for grade, students in categorized_students.items():
            result[grade] = [] 
            for student in students: 
                result[grade].append({ 
                                      "name": student.get_name(), 
                                      "id": student.get_student_id(), 
                                      "grade": student.calculate_average_grade(), 
                                      "mark": student.calculate_average_mark() }) 
        return result
    
    def remove_student(self, admin, student_id):
        student = self.data_manager.lookup_student_by_id(student_id)
        if student is None: 
            return { 
                    "success": False,
                    "message": "Student not found" 
                    } 
        admin.remove_student(student_id, self.data_manager) 
        self.data_manager.save_data() 
        return { 
                "success": True, 
                "message": f"Removed student {student.get_name()} :: {student.get_student_id()}" }

    def clear_all_data(self, admin):
        students = self.data_manager.get_all_students()
        total_students = len(students)
        admin.clear_all_data(self.data_manager)
        self.data_manager.save_data()
        return { 
                "success": True,
                "message": f"Cleared database ({total_students} students removed)" }
