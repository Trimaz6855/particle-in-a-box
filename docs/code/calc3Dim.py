import numpy as np
import sympy as sp 

def calculate(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val, z_value):

    x_vals = np.arange(0, l_x_val, 0.001)
    y_vals = np.arange(0, l_y_val, 0.001)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    l_x, l_y, l_z, n_x, n_y, n_z, x, y, z = sp.symbols("l_x, l_y, l_z, n_x, n_y, n_z, x, y, z")
    equation = sp.sympify(sp.sqrt(8 / (l_x * l_y * l_z)) * sp.sin((sp.pi * n_x * x) / l_x) * sp.sin((sp.pi * n_y * y) / l_y) * sp.sin((sp.pi * n_z * z) / l_z))
    z_initial = 0.23
    prob_density = sp.lambdify([l_x, l_y, l_z, n_x, n_y, n_z, x, y, z], equation ** 2, "numpy")

    pd_values = prob_density(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val, x_vals, y_vals, z_value)

    return pd_values

def calculate2(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val, z_value):

    x_vals = np.linspace(0, l_x_val, 200)
    y_vals = np.linspace(0, l_y_val, 200)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    l_x, l_y, l_z, n_x, n_y, n_z, x, y, z = sp.symbols("l_x, l_y, l_z, n_x, n_y, n_z, x, y, z")
    equation = sp.sympify(sp.sqrt(8 / (l_x * l_y * l_z)) * sp.sin((sp.pi * n_x * x) / l_x) * sp.sin((sp.pi * n_y * y) / l_y) * sp.sin((sp.pi * n_z * z) / l_z))
    z_initial = 0.23
    prob_density = sp.lambdify([l_x, l_y, l_z, n_x, n_y, n_z, x, y, z], equation ** 2, "numpy")

    pd_values = prob_density(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val, x_vals, y_vals, z_value)

    return pd_values

def calculate3(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val, z_value):

    x_vals = np.linspace(0, l_x_val, 200)
    y_vals = np.linspace(0, l_y_val, 200)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)

    pd_values = (np.sqrt(8 / (l_x_val * l_y_val * l_z_val)) 
                * np.sin((np.pi * n_x_val * x_vals) / l_x_val)
                * np.sin((np.pi * n_y_val * y_vals) / l_y_val)
                * np.sin((np.pi * n_z_val * z_value) / l_z_val))

    return pd_values