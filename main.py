import tkinter as tk
import math
import cmath 
import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt  
from scipy.fftpack import fft  
from scipy.integrate import odeint  
from scipy.optimize import minimize  
import datetime  
import hashlib 
from tkinter import messagebox

memory = 0
angle_mode = 'RAD'  
history = []
exchange_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}  # Sample rates

def evaluate_expression(expression):
    try:
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
                       "complex": complex, "np": np, "sp": sp, "fft": fft, "odeint": odeint,
                       "hashlib": hashlib, "datetime": datetime, "minimize": minimize,
                       "plot": plot_function, "solve_ode": solve_ode, "prime_factors": prime_factors,
                       "is_prime": is_prime, "list_primes": list_primes, "currency_convert": currency_convert,
                       "polynomial_roots": polynomial_roots, "calculate_date_difference": calculate_date_difference})
        history.append(f"{expression} = {result}")
        return result
    except Exception as e:
        return "Error"

def fourier_transform(signal):
    return fft(signal)

def solve_ode(func, y0, t):
    return odeint(func, y0, t)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def list_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def polynomial_roots(coeffs):
    return np.roots(coeffs)

def currency_convert(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        return amount * exchange_rates[to_currency] / exchange_rates[from_currency]
    else:
        return "Unknown currency"

def calculate_date_difference(date1, date2):
    return abs((date2 - date1).days)

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

def toggle_angle_mode():
    global angle_mode
    angle_mode = 'DEG' if angle_mode == 'RAD' else 'RAD'
    angle_button.config(text=f"{angle_mode}/RAD")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Calculation History")
    history_text = tk.Text(history_window, width=50, height=20, bg="#1e2a38", fg="white")
    history_text.pack(padx=10, pady=10)
    for item in history:
        history_text.insert(tk.END, item + "\n")

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

def switch_theme():
    if root["bg"] == "#2e3b4e":
        root.configure(bg="#f0f0f0")
        entry.configure(bg="#ffffff", fg="#000000", insertbackground="black")
        for btn in root.winfo_children():
            if isinstance(btn, tk.Button):
                btn.configure(bg="#e0e0e0", fg="#000000")
    else:
        root.configure(bg="#2e3b4e")
        entry.configure(bg="#1e2a38", fg="#ffffff", insertbackground="white")
        for btn in root.winfo_children():
            if isinstance(btn, tk.Button):
                btn.configure(bg="#1e2a38", fg="#ffffff")

root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.configure(bg="#2e3b4e")

button_style = {
    "bg": "#1e2a38",
    "fg": "#ffffff",
    "font": ("Arial", 14),
    "relief": "flat",
    "borderwidth": 0,
    "padx": 20,
    "pady": 10
}

entry = tk.Entry(root, width=40, font=("Arial", 16), bd=0, bg="#1e2a38", fg="#ffffff", insertbackground="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("7", "8", "9", "/", "C"),
    ("4", "5", "6", "*", "^"),
    ("1", "2", "3", "-", "log10("),
    ("0", ".", "(", ")", "+"),
    ("sin(", "cos(", "tan(", "!", "="),
    ("asin(", "acos(", "atan(", "sqrt(", "exp("),
    ("pi", "e", "M+", "M-", "MS"),
    ("MR", "MC", "DEG/RAD", "Hist", "Graph")
]

for i, row in enumerate(buttons):
    for j, symbol in enumerate(row):
        button = tk.Button(root, text=symbol, **button_style, command=lambda s=symbol: button_click(s))
        button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

angle_button = tk.Button(root, text=f"{angle_mode}/RAD", **button_style, command=toggle_angle_mode)
angle_button.grid(row=8, column=3, columnspan=2, padx=5, pady=5, sticky="nsew")

theme_button = tk.Button(root, text="Switch Theme", **button_style, command=switch_theme)
theme_button.grid(row=9, column=0, columnspan=5, padx=5, pady=10, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
for i in range(1, 10):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
