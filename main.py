import tkinter as tk
from tkinter import messagebox
from math import *

root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.configure(bg='#222222')
root.geometry("600x800")
root.resizable(0, 0)

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
        # Add logic for Lie Algebra calculations
        # For demonstration, just taking the factorial of the result
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
        # Add logic for homotopy analysis
        # For demonstration, calculating sin of the result
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
        # Add logic for wavelet transformation
        # For demonstration, just computing the natural logarithm
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
        # Add logic for symmetry group analysis
        # For demonstration, calculating the cosine of the result
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
        # Add logic for stochastic calculus
        # For demonstration, calculating the exponential
        result = exp(result)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        messagebox.showerror("Error", f"Invalid Operation: {e}")

display = tk.Entry(root, font=("Helvetica", 20), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="we")

button_style = {
    'padx': 20,
    'pady': 20,
    'bd': 1,
    'bg': '#333333',
    'fg': 'white',
    'font': ('Helvetica', 18),
    'relief': 'flat'
}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('log', 5, 2), ('!', 5, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, command=calculate, **button_style).grid(row=row, column=col, columnspan=2, sticky="nsew")
    elif text == 'C':
        tk.Button(root, text=text, command=clear_display, **button_style).grid(row=row, column=col, sticky="nsew")
    elif text == '√':
        tk.Button(root, text=text, command=sqrt_func, **button_style).grid(row=row, column=col, sticky="nsew")
    elif text == 'log':
        tk.Button(root, text=text, command=log_func, **button_style).grid(row=row, column=col, sticky="nsew")
    elif text == '!':
        tk.Button(root, text=text, command=factorial_func, **button_style).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, command=lambda txt=text: add_to_display(txt), **button_style).grid(row=row, column=col, sticky="nsew")

advanced_buttons = [
    ("Lie Alg", lie_algebra_calculator, 6, 0),
    ("Homotopy", homotopy_analysis, 6, 1),
    ("Wavelet", wavelet_transform, 6, 2),
    ("Symmetry", symmetry_group_analysis, 6, 3),
    ("Stochastic", stochastic_calculus, 7, 0),
]

for (text, command, row, col) in advanced_buttons:
    tk.Button(root, text=text, command=command, **button_style).grid(row=row, column=col, sticky="nsew")

root.mainloop()
