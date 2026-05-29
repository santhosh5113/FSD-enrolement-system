import tkinter as tk
from gui_app.home_window import HomeWindow
from gui_app.theme import *


class LoginWindow(tk.Frame):
    def __init__(self, master, auth_controller, student_controller):
        super().__init__(master, bg=BG)
        self.master = master
        self.auth_controller = auth_controller
        self.student_controller = student_controller

        # ── Centred card ───────────────────────────────────────────────
        card = tk.Frame(self, bg=SURFACE, padx=48, pady=44)
        card.place(relx=0.5, rely=0.5, anchor="center")

        # Accent bar at top
        tk.Frame(card, bg=ACCENT, height=5
                 ).grid(row=0, column=0, columnspan=2, sticky="ew",
                        pady=(0, 28))

        # Title
        tk.Label(card, text="Enrollment System",
                 font=(FONT, SZ_TITLE, "bold"),
                 fg=TEXT_BRIGHT, bg=SURFACE
                 ).grid(row=1, column=0, columnspan=2, pady=(0, 6))

        tk.Label(card, text="Sign in to your student account",
                 font=(FONT, SZ_BODY), fg=TEXT_MID, bg=SURFACE
                 ).grid(row=2, column=0, columnspan=2, pady=(0, 28))

        # ── Email ──────────────────────────────────────────────────────
        tk.Label(card, text="EMAIL ADDRESS",
                 font=(FONT, SZ_SMALL, "bold"),
                 fg=ACCENT_GLOW, bg=SURFACE, anchor="w"
                 ).grid(row=3, column=0, columnspan=2, sticky="w",
                        pady=(0, 6))

        self.email_entry = tk.Entry(
            card, width=36,
            font=(FONT, SZ_INPUT),
            bg=ENTRY_BG, fg=ENTRY_FG,
            insertbackground=TEXT_BRIGHT,
            relief="flat", bd=0,
            highlightthickness=2,
            highlightbackground=BORDER,
            highlightcolor=ACCENT
        )
        self.email_entry.grid(row=4, column=0, columnspan=2,
                              ipady=10, pady=(0, 18), sticky="ew")

        # ── Password ───────────────────────────────────────────────────
        tk.Label(card, text="PASSWORD",
                 font=(FONT, SZ_SMALL, "bold"),
                 fg=ACCENT_GLOW, bg=SURFACE, anchor="w"
                 ).grid(row=5, column=0, columnspan=2, sticky="w",
                        pady=(0, 6))

        self.password_entry = tk.Entry(
            card, width=36,
            font=(FONT, SZ_INPUT),
            bg=ENTRY_BG, fg=ENTRY_FG,
            insertbackground=TEXT_BRIGHT,
            relief="flat", bd=0,
            highlightthickness=2,
            highlightbackground=BORDER,
            highlightcolor=ACCENT,
            show="●"
        )
        self.password_entry.grid(row=6, column=0, columnspan=2,
                                 ipady=10, pady=(0, 8), sticky="ew")

        # Error message
        self.message_label = tk.Label(
            card, text="",
            fg=DANGER, bg=SURFACE,
            font=(FONT, SZ_SMALL), wraplength=340
        )
        self.message_label.grid(row=7, column=0, columnspan=2,
                                pady=(0, 20))

        # ── Buttons (Label-based for macOS colour support) ─────────────
        btn_row = tk.Frame(card, bg=SURFACE)
        btn_row.grid(row=8, column=0, columnspan=2, sticky="ew")
        btn_row.columnconfigure(0, weight=3)
        btn_row.columnconfigure(1, weight=1)

        make_btn(btn_row, "Sign In",
                 bg=ACCENT, fg=TEXT_BRIGHT,
                 command=self.login_action,
                 pady=13
                 ).grid(row=0, column=0, padx=(0, 10), sticky="ew")

        make_btn(btn_row, "Exit",
                 bg=BORDER, fg=TEXT_BRIGHT,
                 command=self.master.destroy,
                 bold=False, pady=13
                 ).grid(row=0, column=1, sticky="ew")

        # Enter key submits
        self.email_entry.bind("<Return>",   lambda e: self.login_action())
        self.password_entry.bind("<Return>", lambda e: self.login_action())
        self.email_entry.focus_set()

    def login_action(self):
        email    = self.email_entry.get().strip()
        password = self.password_entry.get()
        result   = self.auth_controller.login(email, password)
        if not result["success"]:
            self.message_label.config(text="⚠  " + result["message"])
            return
        self.destroy()
        HomeWindow(self.master, result["student"],
                   self.student_controller).pack(fill="both", expand=True)
