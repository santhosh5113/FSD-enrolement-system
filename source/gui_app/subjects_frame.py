import tkinter as tk
from tkinter import ttk
from gui_app.theme import *


class SubjectsFrame(tk.Frame):
    def __init__(self, master, student, student_controller):
        super().__init__(master, bg=BG)
        self.student = student
        self.student_controller = student_controller

        # ── Header ─────────────────────────────────────────────────────
        hdr = tk.Frame(self, bg=BG)
        hdr.pack(fill="x", padx=40, pady=(36, 0))

        tk.Label(hdr, text="My Subjects",
                 font=(FONT, SZ_TITLE, "bold"),
                 fg=TEXT_BRIGHT, bg=BG
                 ).pack(anchor="w")
        tk.Label(hdr, text="Your enrolled subjects, marks, and grades.",
                 font=(FONT, SZ_BODY), fg=TEXT_MID, bg=BG
                 ).pack(anchor="w", pady=(6, 0))

        tk.Frame(self, bg=BORDER, height=1
                 ).pack(fill="x", padx=40, pady=(20, 20))

        # ── Summary badges ─────────────────────────────────────────────
        subjects = self.student_controller.show_subjects(self.student)
        avg = (sum(s.get_marks() for s in subjects) / len(subjects)
               if subjects else 0)
        def grade_from_avg(m):
            return ('HD' if m>=85 else 'D' if m>=75 else
                    'C'  if m>=65 else 'P' if m>=50 else 'Z')
        avg_grade  = grade_from_avg(avg)
        avg_colour = GRADE_COLOURS.get(avg_grade, TEXT_MID)

        badges = tk.Frame(self, bg=BG)
        badges.pack(fill="x", padx=40, pady=(0, 20))

        for label, value, colour in [
            ("SUBJECTS",      str(len(subjects)), ACCENT_GLOW),
            ("AVERAGE MARK",  f"{avg:.1f}",       avg_colour),
            ("AVERAGE GRADE", avg_grade,           avg_colour),
        ]:
            b = tk.Frame(badges, bg=SURFACE, padx=20, pady=14)
            b.pack(side="left", padx=(0, 12))
            tk.Label(b, text=label,
                     font=(FONT, 9, "bold"), fg=TEXT_DIM, bg=SURFACE
                     ).pack(anchor="w")
            tk.Label(b, text=value,
                     font=(FONT, 22, "bold"), fg=colour, bg=SURFACE
                     ).pack(anchor="w", pady=(4, 0))

        # ── Table ──────────────────────────────────────────────────────
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Dark.Treeview",
                        background=SURFACE,
                        foreground=TEXT_BRIGHT,
                        fieldbackground=SURFACE,
                        rowheight=44,
                        font=(FONT, SZ_BODY),
                        borderwidth=0)
        style.configure("Dark.Treeview.Heading",
                        background=SIDEBAR_BG,
                        foreground=ACCENT_GLOW,
                        font=(FONT, SZ_SMALL, "bold"),
                        relief="flat",
                        padding=(12, 10))
        style.map("Dark.Treeview",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", TEXT_BRIGHT)])

        tbl = tk.Frame(self, bg=BG)
        tbl.pack(fill="both", expand=True, padx=40, pady=(0, 20))

        columns = ("Subject ID", "Mark", "Grade")
        self.tree = ttk.Treeview(
            tbl, columns=columns, show="headings",
            style="Dark.Treeview", selectmode="browse"
        )
        for col, width in [("Subject ID", 200), ("Mark", 180), ("Grade", 180)]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center", minwidth=100)

        sb = ttk.Scrollbar(tbl, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="left", fill="y")

        for grade, colour in GRADE_COLOURS.items():
            self.tree.tag_configure(
                grade, foreground=colour,
                font=(FONT, SZ_BODY, "bold")
            )

        for s in subjects:
            grade = s.get_grade()
            self.tree.insert("", "end",
                             values=(s.get_subject_id(), s.get_marks(), grade),
                             tags=(grade,))
