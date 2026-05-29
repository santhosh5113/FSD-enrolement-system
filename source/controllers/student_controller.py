class StudentController:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def enroll_subject(self, student):
        if student.check_Subject_limit():
            return {
                "success": False,
                "message":
                    "Students are allowed to enrol in 4 subjects only"
            }
        subject_id = student.enroll_subject()
        self.data_manager.update_student(student)
        self.data_manager.save_data()
        enrolled_subject = student.get_enrolled_subjects()

        return {
                "success": True,
                "message":
                    f"Enrolling in Subject-{subject_id}"
                    f"\nYou are now enrolled in {len(enrolled_subject)} out of 4 subjects"
            }

    def remove_subject(self, student, subject_id):
        removed_subject = student.remove_subject(subject_id)
        if removed_subject is None:
            return {
                "success": False,
                "message":
                    f"You did not enroll in Subject-{subject_id}"
            }
        self.data_manager.update_student(student)
        self.data_manager.save_data()
        enrolled_subject = student.get_enrolled_subjects()
        return {
                "success": True,
                "message":
                    f"Dropping Subject-{subject_id}"
                    f"\nYou are now enrolled in {len(enrolled_subject)} out of 4 subjects"
            }

    def change_password(self, student, new_password):
        success = student.change_password(new_password)
        if success:
            self.data_manager.update_student(student)
            self.data_manager.save_data()
            return {
                "success": success,
                "message": "Password changed successfully"
            }
        return {
                "success": success,
                "message": "Invalid password format"
            }
    
    def show_subjects(self, student):
        return student.get_enrolled_subjects()



