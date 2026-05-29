import tkinter as tk
from gui_app.exception_window import ExceptionWindow
from gui_app.theme import *


class EnrollmentFrame(tk.Frame):
    def __init__(self, master, student, student_controller):
        super().__init__(master, bg=BG)
        self.student = student
        self.student_controller = student_controller

        # ── Header ─────────────────────────────────────────────────────
        hdr = tk.Frame(self, bg=BG)
        hdr.pack(fill="x", padx=40, pady=(36, 0))

        tk.Label(hdr, text="Subject Enrollment",
                 font=(FONT, SZ_TITLE, "bold"),
                 fg=TEXT_BRIGHT, bg=BG
                 ).pack(anchor="w")
        tk.Label(hdr,
                 text="You may enrol in up to 4 subjects. "
                      "Each enrolment assigns a subject automatically.",
                 font=(FONT, SZ_BODY), fg=TEXT_MID, bg=BG
                 ).pack(anchor="w", pady=(6, 0))

        tk.Frame(self, bg=BORDER, height=1
                 ).pack(fill="x", padx=40, pady=(20, 28))

        # ── Counter card ───────────────────────────────────────────────
        count     = len(student.get_enrolled_subjects())
        remaining = 4 - count
        bar_col   = SUCCESS if count < 4 else DANGER

        card = tk.Frame(self, bg=SURFACE, padx=32, pady=28)
        card.pack(fill="x", padx=40, pady=(0, 28))

        # coloured top stripe
        tk.Frame(card, bg=bar_col, height=4
                 ).grid(row=0, column=0, columnspan=3,
                        sticky="ew", pady=(0, 20))

        # big counter number
        tk.Label(card, text=str(count),
                 font=(FONT, 56, "bold"), fg=bar_col, bg=SURFACE
                 ).grid(row=1, column=0, sticky="w", padx=(0, 4))
        tk.Label(card, text="/ 4",
                 font=(FONT, 28), fg=TEXT_MID, bg=SURFACE
                 ).grid(row=1, column=1, sticky="sw", pady=(0, 8))

        tk.Label(card, text="subjects enrolled",
                 font=(FONT, SZ_BODY), fg=TEXT_MID, bg=SURFACE
                 ).grid(row=2, column=0, columnspan=2, sticky="w",
                        pady=(0, 8))

        badge = (f"{remaining} slot{'s' if remaining != 1 else ''} remaining"
                 if remaining > 0 else "All slots filled")
        tk.Label(card, text=badge,
                 font=(FONT, SZ_SMALL, "bold"), fg=bar_col, bg=SURFACE
                 ).grid(row=3, column=0, columnspan=2, sticky="w",
                        pady=(0, 24))

        # Enrol button — Label-based for macOS
        if remaining > 0:
            enrol_btn = make_btn(
                card, "  +   Enrol in a Subject  ",
                bg=ACCENT, fg=TEXT_BRIGHT,
                command=self.enroll_subject,
                pady=14
            )
        else:
            enrol_btn = tk.Label(
                card, text="  Slots Full  ",
                font=(FONT, SZ_BTN, "bold"),
                fg=TEXT_DIM, bg=BORDER,
                padx=24, pady=14
            )
        enrol_btn.grid(row=4, column=0, columnspan=2, sticky="w")

        # ── Status ─────────────────────────────────────────────────────
        self.status_label = tk.Label(
            self, text="", fg=SUCCESS, bg=BG,
            font=(FONT, SZ_BODY, "bold"), wraplength=520
        )
        self.status_label.pack(padx=40, pady=(0, 0), anchor="w")

    def enroll_subject(self):
        result = self.student_controller.enroll_subject(self.student)
        if not result["success"]:
            ExceptionWindow(self, "Enrolment Error", result["message"])
            return
        self.status_label.config(text="✔  " + result["message"])
        # Rebuild frame so counter refreshes
        for w in self.master.winfo_children():
            w.destroy()
        EnrollmentFrame(self.master, self.student,
                        self.student_controller).pack(fill="both", expand=True)
