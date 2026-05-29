# 🎓 Enrollment System

## 📌 Project Description

A Python-based university enrollment system that allows students to log in, enroll in subjects, and view their results. The system is built using Object-Oriented Programming (OOP) principles with a modular, layered architecture. It supports two interfaces: a Command Line Interface (CLI) and a Graphical User Interface (GUI) built with Tkinter.

---

## 👥 Members

| Name | Student ID |
|------|------------|
| Member 1 | xxxxxxxx |
| Member 2 | xxxxxxxx |
| Member 3 | xxxxxxxx |

> *(Replace with actual names and student IDs)*

---

## 📂 Project Structure

```
Enrollment-System/
│
├── readme.md
├── docs/
│   └── Presentation.pdf
│
└── source/
    ├── cli_main.py              # Entry point for CLI
    ├── gui_main.py              # Entry point for GUI
    │
    ├── cli_app/
    │   └── cli_uni_app.py       # CLI controller
    │
    ├── gui_app/
    │   ├── login_window.py      # Login screen
    │   ├── home_window.py       # Main dashboard with sidebar
    │   ├── enrollment_frame.py  # Subject enrollment view
    │   ├── subjects_frame.py    # Enrolled subjects table
    │   └── exception_window.py  # Error popup dialog
    │
    ├── controllers/
    │   ├── auth_controller.py   # Login and registration logic
    │   ├── student_controller.py
    │   └── admin_controller.py
    │
    ├── models/
    │   ├── user.py              # Abstract base class
    │   ├── student.py
    │   ├── admin.py
    │   └── subject.py
    │
    ├── services/
    │   └── data_manager.py      # File I/O and data persistence
    │
    └── data/
        └── students.data        # JSON data storage
```

---

## ▶️ How to Run

### Prerequisites

- Python 3.x installed
- No additional packages required (uses standard library only)

### CLI Mode

```bash
cd source
python cli_main.py
```

### GUI Mode

```bash
cd source
python gui_main.py
```

> **Note:** The GUI uses Python's built-in `tkinter` library. On macOS, tkinter comes pre-installed with the standard Python distribution from [python.org](https://python.org). If you encounter issues, ensure you are using the official Python installer rather than a Homebrew version.
