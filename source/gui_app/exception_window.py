import tkinter as tk
from gui_app.theme import *


class ExceptionWindow(tk.Toplevel):
    def __init__(self, master, title, message, color=None):
        super().__init__(master)
        if color is None:
            color = DANGER
        self.title(title)
        self.geometry("440x210")
        self.resizable(False, False)
        self.configure(bg=SURFACE)

        # Centre over parent
        self.update_idletasks()
        try:
            px = master.winfo_rootx()
            py = master.winfo_rooty()
            pw = master.winfo_width()
            ph = master.winfo_height()
            x  = px + (pw - 440) // 2
            y  = py + (ph - 210) // 2
            self.geometry(f"+{x}+{y}")
        except Exception:
            pass

        # Coloured top stripe
        tk.Frame(self, bg=color, height=5).pack(fill="x")

        body = tk.Frame(self, bg=SURFACE, padx=28, pady=20)
        body.pack(fill="both", expand=True)

        tk.Label(body, text=f"⚠   {title}",
                 font=(FONT, SZ_HEADING, "bold"), fg=color, bg=SURFACE
                 ).pack(anchor="w", pady=(0, 10))

        tk.Label(body, text=message,
                 font=(FONT, SZ_BODY), fg=TEXT_BRIGHT, bg=SURFACE,
                 wraplength=380, justify="left"
                 ).pack(anchor="w")

        # Close — Label-based button for macOS
        close_btn = make_btn(
            body, "  Close  ",
            bg=color, fg=TEXT_BRIGHT,
            command=self.destroy,
            pady=8
        )
        close_btn.pack(side="bottom", anchor="e", pady=(16, 0))

        self.grab_set()
