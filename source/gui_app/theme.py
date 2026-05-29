"""
Shared theme constants for the Enrollment System GUI.
Dark theme — high contrast, large fonts, macOS-compatible.
"""

# ── Colours ────────────────────────────────────────────────────────────
BG          = "#1a1d2e"   # deep navy  – app / window background
SURFACE     = "#252840"   # slightly lighter navy – cards / panels
SIDEBAR_BG  = "#0f1120"   # darkest – sidebar
BORDER      = "#3a3f6b"   # dividers

ACCENT      = "#6c63ff"   # vivid purple – primary action
ACCENT_DARK = "#574fd6"   # hover
ACCENT_GLOW = "#8b85ff"   # active / label accent

SUCCESS     = "#2dd4a7"   # teal – positive feedback
DANGER      = "#ff5c6c"   # coral red – errors / exit / logout
WARNING     = "#ffb347"   # amber

TEXT_BRIGHT = "#f0f2ff"   # near-white – main text
TEXT_MID    = "#9ba3cc"   # secondary labels
TEXT_DIM    = "#5a6180"   # dim / placeholder

ENTRY_BG    = "#2e3250"   # input field background
ENTRY_FG    = "#f0f2ff"   # input field text

GRADE_COLOURS = {
    "HD": "#2dd4a7",
    "D":  "#6c63ff",
    "C":  "#60a5fa",
    "P":  "#ffb347",
    "Z":  "#ff5c6c",
}

# ── Typography ─────────────────────────────────────────────────────────
FONT     = "Arial"

SZ_TITLE   = 24
SZ_HEADING = 16
SZ_BODY    = 13
SZ_SMALL   = 11
SZ_BTN     = 13
SZ_INPUT   = 13


# ── macOS-safe button factory ──────────────────────────────────────────
def make_btn(parent, text, bg, fg, command, font_size=SZ_BTN,
             bold=True, padx=24, pady=12, width=None):
    """
    A tk.Label styled as a button.
    tk.Button ignores bg/fg on macOS (Aqua theme overrides them).
    tk.Label has no such restriction, so we bind click events instead.
    """
    weight = "bold" if bold else "normal"
    kw = dict(
        text=text,
        font=(FONT, font_size, weight),
        fg=fg,
        bg=bg,
        cursor="hand2",
        padx=padx,
        pady=pady,
        relief="flat",
    )
    if width:
        kw["width"] = width

    lbl = tk.Label(parent, **kw)

    # Hover: darken background slightly
    def on_enter(e):
        lbl.config(bg=_darken(bg))
    def on_leave(e):
        lbl.config(bg=bg)
    def on_click(e):
        command()

    lbl.bind("<Enter>",   on_enter)
    lbl.bind("<Leave>",   on_leave)
    lbl.bind("<Button-1>", on_click)
    return lbl


def _darken(hex_color, factor=0.85):
    """Return a slightly darker shade of a hex colour."""
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = (int(c * factor) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


# Import tk here so make_btn can use it (imported once, shared)
import tkinter as tk
