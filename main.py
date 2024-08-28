import tkinter as tk
import math
import cmath  # For complex numbers
import numpy as np  # For matrix and vector operations
import sympy as sp  # For calculus and solving equations
import matplotlib.pyplot as plt  # For graphing functions
from tkinter import messagebox

# Initialize memory, history, and angle mode
memory = 0
angle_mode = 'RAD'  # Default to radians
history = []

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # Evaluate the expression and update the result
        result = eval(expression, {"__builtins__": None},
                      {"sqrt": math.sqrt, "log": math.log, "log10": math.log10,
                       "exp": math.exp, "pi": math.pi, "e": math.e, "sin": math.sin,
                       "cos": math.cos, "tan": math.tan, "asin": math.asin,
                       "acos": math.acos, "atan": math.atan, "radians": math.radians,
                       "degrees": math.degrees, "factorial": math.factorial, "pow": math.pow,
                       "abs": abs, "floor": math.floor, "ceil": math.ceil,
                       "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
                       "asinh": math.asinh, "acosh": math.acosh, "atanh": math.atanh,
                       "tau": math.tau, "inf": math.inf, "nan": math.nan,
                       "complex": complex, "np": np, "sp": sp, "plot": plot_function})
        history.append(f"{expression} = {result}")
        return result
    except Exception as e:
        return "Error"

# Function to handle button click
def button_click(symbol):
    global memory
    current_text = str(entry.get())
    
    if symbol == "=":
        result = evaluate_expression(current_text)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "MR":
        entry.insert(tk.END, memory)
    elif symbol == "MC":
        memory = 0
    elif symbol == "M+":
        memory += evaluate_expression(current_text)
        entry.delete(0, tk.END)
    elif symbol == "M-":
        memory -= evaluate_expression(current_text)
        entry.delete(0, tk.END)
    elif symbol == "MS":
        memory = evaluate_expression(current_text)
        entry.delete(0, tk.END)
    elif symbol == "DEG/RAD":
        toggle_angle_mode()
    elif symbol == "Hist":
        show_history()
    elif symbol == "Graph":
        plot_function(current_text)
    else:
        entry.insert(tk.END, symbol)

# Toggle angle mode between degrees and radians
def toggle_angle_mode():
    global angle_mode
    angle_mode = 'DEG' if angle_mode == 'RAD' else 'RAD'
    angle_button.config(text=f"{angle_mode}/RAD")

# Function to show history
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_text = tk.Text(history_window, width=50, height=20, bg="#1e2a38", fg="white")
    history_text.pack(padx=10, pady=10)
    for item in history:
        history_text.insert(tk.END, item + "\n")

# Function to plot a mathematical function
def plot_function(expression):
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(expression, {"__builtins__": None, "np": np, "x": x})
        plt.plot(x, y)
        plt.title(f"Graph of {expression}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression for graphing!")

# Create the main window
root = tk.Tk()
root.title("Advanced Scientific Calculator")
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
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Button grid layout
buttons = [
    ("7", "8", "9", "/", "C"),
    ("4", "5", "6", "*", "^"),
    ("1", "2", "3", "-", "log10("),
    ("0", ".", "(", ")", "+"),
    ("sin(", "cos(", "tan(", "!", "="),
    ("asin(", "acos(", "atan(", "sqrt(", "exp("),
    ("pi", "e", "MR", "MC", "M+"),
    ("M-", "MS", "(", ")", "Hist"),
    ("sinh(", "cosh(", "tanh(", "abs(", "floor("),
    ("asinh(", "acosh(", "atanh(", "ceil(", "tau"),
    ("x^2", "x^3", "DEG/RAD", "mod", "inf"),
    ("nan", "**", "(", ")", "Graph"),
    ("sp.diff(", "sp.integrate(", "sp.solve(", "np.matrix(", "np.dot("),
    ("np.cross(", "complex(", "bin(", "oct(", "hex("),
]

# Create buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "x^2":
            button = tk.Button(root, text=text, command=lambda: button_click("**2"), **button_style)
        elif text == "x^3":
            button = tk.Button(root, text=text, command=lambda: button_click("**3"), **button_style)
        elif text == "mod":
            button = tk.Button(root, text=text, command=lambda: button_click("%"), **button_style)
        elif text == "Hist":
            button = tk.Button(root, text=text, command=show_history, **button_style)
        elif text == "Graph":
            button = tk.Button(root, text=text, command=lambda: plot_function(entry.get()), **button_style)
        else:
            button = tk.Button(root, text=text, command=lambda t=text: button_click(t), **button_style)
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

# Angle mode button
angle_button = tk.Button(root, text="RAD/DEG", command=toggle_angle_mode, **button_style)
angle_button.grid(row=len(buttons)+1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Configure row and column weights for resizing
for i in range(len(buttons)+2):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
