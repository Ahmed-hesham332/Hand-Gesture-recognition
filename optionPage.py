import tkinter as tk
from tkinter import ttk
from tkinter import font
import main as mouseMovement
import Yolo_realTime as yolo
import home as ip


def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, color):
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color, outline="")
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color, outline="")
    canvas.create_arc(
        x1,
        y1,
        x1 + 2 * radius,
        y1 + 2 * radius,
        start=90,
        extent=90,
        fill=color,
        outline="",
    )
    canvas.create_arc(
        x2 - 2 * radius,
        y1,
        x2,
        y1 + 2 * radius,
        start=0,
        extent=90,
        fill=color,
        outline="",
    )
    canvas.create_arc(
        x1,
        y2 - 2 * radius,
        x1 + 2 * radius,
        y2,
        start=180,
        extent=90,
        fill=color,
        outline="",
    )
    canvas.create_arc(
        x2 - 2 * radius,
        y2 - 2 * radius,
        x2,
        y2,
        start=270,
        extent=90,
        fill=color,
        outline="",
    )


def start_option_page():
    def run_cursor_mode():
        mouseMovement.main()

    def run_non_cursor_mode():
        yolo.start_application()

    def back_to_intro_page():
        root.destroy()
        ip.start_intro_page()

    root = tk.Tk()
    root.title("Option Page")
    root.geometry("900x600+100+100")  
    root.configure(bg="#333333")

    headline_frame = tk.Frame(root, bg="#333333")
    headline_frame.pack(pady=50)

    headline_font = font.Font(family="Helvetica", size=20, weight="bold")

    label = tk.Label(
        headline_frame, text="Choose Mode", font=headline_font, bg="#333333", fg="white"
    )
    label.pack()

    button_frame = tk.Frame(root, bg="#333333")
    button_frame.pack(pady=50)

    def create_button(text, command):
        canvas = tk.Canvas(
            button_frame, width=200, height=80, bg="#333333", highlightthickness=0
        )
        create_rounded_rectangle(canvas, 0, 0, 200, 80, radius=15, color="#dddddd")
        canvas.create_text(
            100, 40, text=text, fill="black", font=("Helvetica", 14, "bold")
        )
        canvas.bind("<Button-1>", lambda event: command())
        return canvas
    
    cursor_button = create_button("Cursor Mode", run_cursor_mode)
    cursor_button.grid(row=0, column=0, padx=20, pady=20)

    non_cursor_button = create_button("Non-Cursor Mode", run_non_cursor_mode)
    non_cursor_button.grid(row=0, column=1, padx=20, pady=20)

    canvas = tk.Canvas(root, width=80, height=40, bg="#333333", highlightthickness=0)
    canvas.pack(side=tk.LEFT, anchor="se", padx=20, pady=20)
    create_rounded_rectangle(canvas, 0, 0, 80, 40, radius=15, color="#dddddd")

    canvas.bind("<Button-1>", lambda event: back_to_intro_page())

    canvas.create_text(
        40, 20, text="back", fill="black", font=("Helvetica", 11, "bold")
    )

    root.mainloop()


if __name__ == "__main__":
    start_option_page()
