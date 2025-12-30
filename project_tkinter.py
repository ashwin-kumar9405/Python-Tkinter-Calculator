import tkinter as tk
from tkinter import ttk

# ------------------ Window Setup ------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("320x460+100+100")
root.resizable(False, False)
root.configure(bg="black")

# Bring window to front briefly
root.attributes("-topmost", True)
root.after(800, lambda: root.attributes("-topmost", False))

# ------------------ Styles ------------------
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Calc.TButton",
    font=("Arial", 14),
    background="#FFA500",
    foreground="black",
    padding=10
)
style.map(
    "Calc.TButton",
    background=[("active", "#FFB733"), ("pressed", "#E69500")]
)

style.configure(
    "Clear.TButton",
    font=("Arial", 14, "bold"),
    background="#FF3B3B",
    foreground="white",
    padding=12
)
style.map(
    "Clear.TButton",
    background=[("active", "#FF6B6B"), ("pressed", "#D92B2B")]
)

style.configure(
    "Calc.TEntry",
    font=("Arial", 22),
    fieldbackground="black",
    foreground="white"
)

# ------------------ Display ------------------
display = ttk.Entry(root, justify="right", style="Calc.TEntry")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=5, padx=5)

# ------------------ Button Logic ------------------
def click(value):
    if value == "C":
        display.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, value)

# ------------------ Buttons ------------------
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        ttk.Button(
            root,
            text=text,
            style="Calc.TButton",
            command=lambda t=text: click(t)
        ).grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

# ------------------ Clear Button (FULL WIDTH BOTTOM) ------------------
clear_btn = ttk.Button(
    root,
    text="CLEAR",
    style="Clear.TButton",
    command=lambda: click("C")
)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# ------------------ Grid Configuration ------------------
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# ------------------ Run App ------------------
root.mainloop()
