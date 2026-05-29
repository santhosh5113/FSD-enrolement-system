import tkinter as tk
from gui_app.enrollment_frame import EnrollmentFrame
from gui_app.subjects_frame import SubjectsFrame
from gui_app.theme import *


def _nav_label(parent, text, active, command):
    """Sidebar nav item — Label-based for macOS colour fidelity."""
    bg = ACCENT      if active else SIDEBAR_BG
    fg = TEXT_BRIGHT if active else TEXT_MID
    weight = "bold"  if active else "normal"

    lbl = tk.Label(
        parent, text=text,
        font=(FONT, SZ_BODY, weight),
        fg=fg, bg=bg,
        cursor="hand2",
        padx=20, pady=14,
        anchor="w"
    )

    def on_enter(e):
        if lbl.cget("bg") != ACCENT:
            lbl.config(bg=SURFACE)
    def on_leave(e):
        if lbl.cget("bg") != ACCENT:
            lbl.config(bg=SIDEBAR_BG)
    def on_click(e):
        command()

    lbl.bind("<Enter>",    on_enter)
    lbl.bind("<Leave>",    on_leave)
    lbl.bind("<Button-1>", on_click)
    return lbl


class HomeWindow(tk.Frame):
    def __init__(self, master, student, student_controller):
        super().__init__(master, bg=BG)
        self.student = student
        self.student_controller = student_controller

        # ── Sidebar ────────────────────────────────────────────────────
        self.sidebar = tk.Frame(self, bg=SIDEBAR_BG, width=240)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo row
        logo = tk.Frame(self.sidebar, bg=SIDEBAR_BG)
        logo.pack(fill="x", padx=20, pady=(30, 0))
        tk.Label(logo, text="🎓", font=(FONT, 20),
                 fg=ACCENT_GLOW, bg=SIDEBAR_BG
                 ).pack(side="left", padx=(0, 8))
        tk.Label(logo, text="Enrollment",
                 font=(FONT, SZ_HEADING, "bold"),
                 fg=TEXT_BRIGHT, bg=SIDEBAR_BG
                 ).pack(side="left")

        tk.Frame(self.sidebar, bg=BORDER, height=1
                 ).pack(fill="x", padx=20, pady=(16, 16))

        # User info
        info = tk.Frame(self.sidebar, bg=SURFACE, padx=16, pady=14)
        info.pack(fill="x", padx=12, pady=(0, 20))
        tk.Label(info, text="SIGNED IN AS",
                 font=(FONT, 9, "bold"), fg=TEXT_DIM, bg=SURFACE
                 ).pack(anchor="w")
        tk.Label(info, text=student.get_name(),
                 font=(FONT, SZ_BODY, "bold"),
                 fg=TEXT_BRIGHT, bg=SURFACE,
                 wraplength=180, justify="left"
                 ).pack(anchor="w", pady=(4, 0))

        # Nav items
        self.nav_enrollment = _nav_label(
            self.sidebar, "📋   Enrollment", True, self.show_enrollment)
        self.nav_enrollment.pack(fill="x", padx=8, pady=(0, 2))

        self.nav_subjects = _nav_label(
            self.sidebar, "📊   My Subjects", False, self.show_subjects)
        self.nav_subjects.pack(fill="x", padx=8, pady=(0, 2))

        # Logout at bottom
        tk.Frame(self.sidebar, bg=BORDER, height=1
                 ).pack(fill="x", padx=20, side="bottom", pady=0)

        logout_lbl = tk.Label(
            self.sidebar, text="⏻   Logout",
            font=(FONT, SZ_BODY), fg=DANGER,
            bg=SIDEBAR_BG, cursor="hand2",
            padx=20, pady=14, anchor="w"
        )
        logout_lbl.pack(side="bottom", fill="x", padx=8, pady=(0, 8))
        logout_lbl.bind("<Button-1>", lambda e: self.logout())
        logout_lbl.bind("<Enter>",    lambda e: logout_lbl.config(bg=SURFACE))
        logout_lbl.bind("<Leave>",    lambda e: logout_lbl.config(bg=SIDEBAR_BG))

        # ── Content area ───────────────────────────────────────────────
        self.content_frame = tk.Frame(self, bg=BG)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.show_enrollment()

    # ── Helpers ────────────────────────────────────────────────────────
    def _set_active(self, active, inactive):
        active.config(bg=ACCENT,     fg=TEXT_BRIGHT,
                      font=(FONT, SZ_BODY, "bold"))
        inactive.config(bg=SIDEBAR_BG, fg=TEXT_MID,
                        font=(FONT, SZ_BODY, "normal"))

    def clear_content(self):
        for w in self.content_frame.winfo_children():
            w.destroy()

    def show_enrollment(self):
        self._set_active(self.nav_enrollment, self.nav_subjects)
        self.clear_content()
        EnrollmentFrame(self.content_frame, self.student,
                        self.student_controller).pack(fill="both", expand=True)

    def show_subjects(self):
        self._set_active(self.nav_subjects, self.nav_enrollment)
        self.clear_content()
        SubjectsFrame(self.content_frame, self.student,
                      self.student_controller).pack(fill="both", expand=True)

    def logout(self):
        self.master.destroy()
