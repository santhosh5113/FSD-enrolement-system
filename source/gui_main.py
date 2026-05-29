import tkinter as tk
from gui_app.login_window import LoginWindow
from controllers.auth_controller import AuthController
from controllers.student_controller import StudentController
from services.data_manager import DataManager
from gui_app.theme import BG


def main():
    root = tk.Tk()
    root.title("Enrollment System")
    root.geometry("860x540")
    root.configure(bg=BG)
    root.resizable(True, True)
    root.minsize(760, 480)

    data_manager = DataManager()
    auth_controller = AuthController(data_manager)
    student_controller = StudentController(data_manager)

    login_window = LoginWindow(root, auth_controller, student_controller)
    login_window.pack(fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
