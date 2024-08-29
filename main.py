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
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# Initialize memory, history, and angle mode
memory = 0
angle_mode = 'RAD'
history = []
exchange_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}

# Function to evaluate the expression
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
                       "polynomial_roots": polynomial_roots, "calculate_date_difference": calculate_date_difference,
                       "matrix_inverse": matrix_inverse, "matrix_determinant": matrix_determinant,
                       "matrix_multiply": matrix_multiply, "matrix_transpose": matrix_transpose,
                       "polar_to_rectangular": polar_to_rectangular, "rectangular_to_polar": rectangular_to_polar,
                       "complex_conjugate": complex_conjugate, "linear_regression": linear_regression,
                       "correlation_coefficient": correlation_coefficient, "variance": variance,
                       "std_dev": std_dev, "loan_amortization": loan_amortization,
                       "npv": npv, "irr": irr, "plot_3d": plot_3d, "parametric_plot": parametric_plot,
                       "convert_temperature": convert_temperature, "convert_length": convert_length,
                       "convert_mass": convert_mass, "bitwise_and": bitwise_and, "bitwise_or": bitwise_or,
                       "bitwise_xor": bitwise_xor, "left_shift": left_shift, "right_shift": right_shift,
                       "binary_to_decimal": binary_to_decimal, "decimal_to_binary": decimal_to_binary,
                       "hex_to_decimal": hex_to_decimal, "decimal_to_hex": decimal_to_hex,
                       "concat_strings": concat_strings, "string_length": string_length,
                       "substring": substring, "day_of_week": day_of_week, "add_date": add_date,
                       "subtract_date": subtract_date})
        history.append(f"{expression} = {result}")
        return result
    except Exception as e:
        return "Error"

# Matrix operations
def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

def matrix_determinant(matrix):
    return np.linalg.det(matrix)

def matrix_multiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def matrix_transpose(matrix):
    return np.transpose(matrix)

# Complex number operations
def polar_to_rectangular(r, theta):
    return cmath.rect(r, theta)

def rectangular_to_polar(z):
    return cmath.polar(z)

def complex_conjugate(z):
    return z.conjugate()

# Advanced statistical functions
def linear_regression(x, y):
    return np.polyfit(x, y, 1)

def correlation_coefficient(x, y):
    return np.corrcoef(x, y)[0, 1]

def variance(data):
    return np.var(data)

def std_dev(data):
    return np.std(data)

# Financial functions
def loan_amortization(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return payment

def npv(rate, cash_flows):
    return np.npv(rate, cash_flows)

def irr(cash_flows):
    return np.irr(cash_flows)

# Graphing enhancements
def plot_3d(expression):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = eval(expression, {"__builtins__": None, "np": np, "X": X, "Y": Y})
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap="viridis")
    plt.show()

def parametric_plot(x_expression, y_expression):
    t = np.linspace(0, 2 * np.pi, 400)
    x = eval(x_expression, {"__builtins__": None, "np": np, "t": t})
    y = eval(y_expression, {"__builtins__": None, "np": np, "t": t})
    plt.plot(x, y)
    plt.show()

# Unit conversions
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return value * 9/5 + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    else:
        return "Invalid conversion"

def convert_length(value, from_unit, to_unit):
    conversions = {'m': 1.0, 'ft': 3.28084, 'in': 39.3701, 'cm': 100.0}
    return value * conversions[to_unit] / conversions[from_unit]

def convert_mass(value, from_unit, to_unit):
    conversions = {'kg': 1.0, 'lb': 2.20462, 'g': 1000.0}
    return value * conversions[to_unit] / conversions[from_unit]

# Logical and bitwise operations
def bitwise_and(a, b):
    return a & b

def bitwise_or(a, b):
    return a | b

def bitwise_xor(a, b):
    return a ^ b

def left_shift(a, n):
    return a << n

def right_shift(a, n):
    return a >> n

# Base conversions
def binary_to_decimal(b):
    return int(b, 2)

def decimal_to_binary(d):
    return bin(d)

def hex_to_decimal(h):
    return int(h, 16)

def decimal_to_hex(d):
    return hex(d)

# String manipulation
def concat_strings(*args):
    return ''.join(args)

def string_length(s):
    return len(s)

def substring(s, start, end=None):
    return s[start:end]

# Calendar functions
def day_of_week(year, month, day):
    return datetime.date(year, month, day).strftime('%A')

def add_date(year, month, day, days=0, months=0, years=0):
    return datetime.date(year, month, day) + datetime.timedelta(days=days) + datetime.timedelta(days=months*30) + datetime.timedelta(days=years*365)

def subtract_date(year, month, day, days=0, months=0, years=0):
    return datetime.date(year, month, day) - datetime.timedelta(days=days) - datetime.timedelta(days=months*30) - datetime.timedelta(days=years*365)

# Implement the rest of the UI, main loop, and button bindings
# ...

root.mainloop()
