import tkinter as tk
import math

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # Evaluate the expression and update the result
        result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "log": math.log, "exp": math.exp, "pi": math.pi, "e": math.e})
        return result
    except Exception as e:
        return "Error"

# Function to handle button click
def button_click(symbol):
    current_text = str(entry.get())
    if symbol == "=":
        result = evaluate_expression(current_text)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#2e3b4e")

# Define button style
button_style = {
    "bg": "#1e2a38",
    "fg": "#ffffff",
    "font": ("Arial", 14),
    "relief": "flat",
    "borderwidth": 0,
    "padx": 20,
    "pady": 10
}

# Entry widget
entry = tk.Entry(root, width=40, font=("Arial", 16), bd=0, bg="#1e2a38", fg="#ffffff", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button grid layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("sqrt(", "log(", "exp(", ")"),
    ("pi", "e", "(", ")"),
    ("=",)
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(root, text=text, command=lambda t=text: button_click(t), **button_style)
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

# Configure row and column weights for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
