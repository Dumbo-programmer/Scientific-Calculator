import tkinter as tk
from tkinter import ttk, messagebox
from math import *

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("600x800")
root.resizable(True, True)  # Make the window resizable

# Load the azure.tcl theme file
root.tk.call("source", "azure.tcl")  # Ensure azure.tcl is in the same directory or provide the correct path
root.tk.call("set_theme", "dark")  # Set the theme to dark mode

# Define styles for ttk buttons and entry using the azure theme
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 18), padding=10, relief="flat")
style.configure("TEntry", font=("Segoe UI", 20), padding=10)

def add_to_display(text):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + text)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def clear_display():
    display.delete(0, tk.END)

def factorial_func():
    try:
        result = factorial(int(display.get()))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def sqrt_func():
    try:
        result = sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def log_func():
    try:
        result = log10(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def lie_algebra_calculator():
    try:
        result = eval(display.get())
        result = factorial(int(result))
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def homotopy_analysis():
    try:
        result = eval(display.get())
        result = sin(result)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def wavelet_transform():
    try:
        result = eval(display.get())
        result = log(result)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def symmetry_group_analysis():
    try:
        result = eval(display.get())
        result = cos(result)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

def stochastic_calculus():
    try:
        result = eval(display.get())
        result = exp(result)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

display = ttk.Entry(root, style="TEntry")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=20, sticky="we")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('log', 5, 2), ('!', 5, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        ttk.Button(root, text=text, command=calculate, style="TButton").grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
    elif text == 'C':
        ttk.Button(root, text=text, command=clear_display, style="TButton").grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    elif text == '√':
        ttk.Button(root, text=text, command=sqrt_func, style="TButton").grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    elif text == 'log':
        ttk.Button(root, text=text, command=log_func, style="TButton").grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    elif text == '!':
        ttk.Button(root, text=text, command=factorial_func, style="TButton").grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    else:
        ttk.Button(root, text=text, command=lambda txt=text: add_to_display(txt), style="TButton").grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

advanced_buttons = [
    ("Lie Alg", lie_algebra_calculator, 6, 0),
    ("Homotopy", homotopy_analysis, 6, 1),
    ("Wavelet", wavelet_transform, 6, 2),
    ("Symmetry", symmetry_group_analysis, 6, 3),
    ("Stochastic", stochastic_calculus, 7, 0),
]

for (text, command, row, col) in advanced_buttons:
    ttk.Button(root, text=text, command=command, style="TButton").grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

root.mainloop()

