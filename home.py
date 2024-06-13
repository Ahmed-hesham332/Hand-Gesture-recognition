import tkinter as tk
from tkinter import ttk
from tkinter import font
import optionPage as op


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


def open_option_page():
    root.destroy()
    op.start_option_page()


def start_intro_page():
    global root
    root = tk.Tk()
    root.title("Hand Gesture Recognition")
    root.geometry("900x600+100+100") 
    root.configure(bg="#333333")

    headline_frame = tk.Frame(root, bg="#333333")
    headline_frame.pack(pady=50)

    headline_font = font.Font(family="Helvetica", size=20, weight="bold")
    subheadline_font = font.Font(family="Helvetica", size=14)
    instruction_font = font.Font(family="Helvetica", size=12)

    label = tk.Label(
        headline_frame,
        text="Hand gesture recognition",
        font=headline_font,
        bg="#333333",
        fg="white",
    )
    label.pack()

    sub_label = tk.Label(
        headline_frame,
        text="This system will allow you to control your PC through your camera",
        font=subheadline_font,
        bg="#333333",
        fg="white",
    )
    sub_label.pack(pady=5)

    instructions_frame = tk.Frame(root, bg="#333333")
    instructions_frame.pack(pady=10, padx=25, anchor="w")

    instructions = [
        "Instruction: Stay in a good lighting room and within 60 to 100 cm from your camera",
        "                                    Option one: No cursor function",
        "Increase Volume: Close your fist and raise your index finger",
        "Increase the brightness: Open palm",
        "Decrease the brightness: Fist",
        "Play the video: Thumbs up",
        "Pause the video: Thumbs up",
        "Decrease Volume: Peace sign",
        "Close app: All fingers up without the thumb",
        "                                    Option two: Cursor function",
        "Open palm: Mouse movement",
        "Touch index and thumb: Left-click",
        "Touch middle finger and thumb: Scroll down",
    ]

    for instruction in instructions:
        label = tk.Label(
            instructions_frame,
            text=instruction,
            font=instruction_font,
            bg="#333333",
            fg="white",
        )
        label.pack(anchor="w", padx=50)

    canvas = tk.Canvas(root, width=80, height=40, bg="#333333", highlightthickness=0)
    canvas.pack(side=tk.RIGHT, anchor="se", padx=20, pady=20)
    create_rounded_rectangle(canvas, 0, 0, 80, 40, radius=15, color="#dddddd")

    canvas.bind("<Button-1>", lambda event: open_option_page())

    canvas.create_text(
        40, 20, text="Next", fill="black", font=("Helvetica", 11, "bold")
    )

    root.mainloop()


if __name__ == "__main__":
    start_intro_page()
