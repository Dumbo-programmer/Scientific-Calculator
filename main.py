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
from sympy import symbols, diff, integrate, solve, simplify, series
from sympy.plotting import plot as sympy_plot
from sympy.matrices import Matrix
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# Initialize memory, history, and angle mode
memory = 0
angle_mode = 'RAD'
history = []
exchange_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0}

# RSA encryption/decryption setup
public_key = None
private_key = None

# Quantum Mechanics setup
qubit_state = [1, 0]  # Initial state |0>

# Define symbols for symbolic math
x, y, z = symbols('x y z')

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
                       "subtract_date": subtract_date, "simplify_expr": simplify_expr,
                       "differentiate": differentiate, "integrate": integrate_expr,
                       "solve_equation": solve_equation, "taylor_series": taylor_series,
                       "fourier_transform": fourier_transform, "laplace_transform": laplace_transform,
                       "eigenvalues": eigenvalues, "eigenvectors": eigenvectors,
                       "lu_decomposition": lu_decomposition, "svd": svd,
                       "run_python_code": run_python_code, "visualize_sorting": visualize_sorting,
                       "regex_test": regex_test, "analyze_circuit": analyze_circuit,
                       "projectile_motion": projectile_motion, "thermodynamics": thermodynamics,
                       "schrodinger_solver": schrodinger_solver, "quantum_gates": quantum_gates,
                       "visualize_qubit": visualize_qubit, "mandelbrot_set": mandelbrot_set,
                       "julia_set": julia_set, "lorenz_attractor": lorenz_attractor,
                       "caesar_cipher": caesar_cipher, "rsa_encrypt": rsa_encrypt,
                       "rsa_decrypt": rsa_decrypt, "sha256_hash": sha256_hash})
        history.append(f"{expression} = {result}")
        return result
    except Exception as e:
        return "Error"

# Symbolic Mathematics
def simplify_expr(expr):
    return simplify(expr)

def differentiate(expr, var):
    return diff(expr, var)

def integrate_expr(expr, var):
    return integrate(expr, var)

def solve_equation(eq, var):
    return solve(eq, var)

def taylor_series(expr, var, point=0, order=5):
    return series(expr, var, point, order)

# Fourier and Laplace Transforms
def fourier_transform(expr, var):
    return sp.fourier_transform(expr, var, sp.omega)

def laplace_transform(expr, var):
    return sp.laplace_transform(expr, var, s)

# Matrix Operations
def eigenvalues(matrix):
    return np.linalg.eigvals(matrix)

def eigenvectors(matrix):
    _, v = np.linalg.eig(matrix)
    return v

def lu_decomposition(matrix):
    return sp.Matrix(matrix).LUdecomposition()

def svd(matrix):
    return np.linalg.svd(matrix)

# Cryptography Functions
def caesar_cipher(text, shift, encrypt=True):
    shift = shift if encrypt else -shift
    return ''.join(chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char for char in text)

def rsa_encrypt(text, pub_key):
    return pow(int.from_bytes(text.encode('utf-8'), 'big'), pub_key[0], pub_key[1])

def rsa_decrypt(cipher, priv_key):
    decrypted = pow(cipher, priv_key[0], priv_key[1])
    return decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big').decode('utf-8')

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Quantum Mechanics
def quantum_gates(state, gate):
    gates = {
        'X': np.array([[0, 1], [1, 0]]),
        'H': (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]]),
        'CNOT': np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    }
    return np.dot(gates[gate], state)

def visualize_qubit(state):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    theta = 2 * math.acos(state[0])
    phi = np.angle(state[1])
    ax.quiver(0, 0, 0, math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta))
    plt.show()

# Run the main loop
root.mainloop()
