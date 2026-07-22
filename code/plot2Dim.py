import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sympy as sp 
from matplotlib import cm

def plot_2d_prob_density(l_x_val, l_y_val, n_x_val, n_y_val):
    fig = plt.figure(figsize=plt.figaspect(0.5))
    fig.suptitle("Graph of the probabilty density function for a 2D particle in a box system")
    plt.figtext(0.01, 0.5, f"L_x: {l_x_val}\nL_y: {l_y_val}\nn_x: {n_x_val}\nn_y: {n_y_val}")
    l_x, l_y, n_x, n_y, x, y = sp.symbols("l_x, l_y, n_x, n_y, x, y")
    equation = sp.sympify(sp.sqrt(4/(l_x * l_y)) * sp.sin((np.pi * n_x * x) / (l_x)) * sp.sin((np.pi * n_y * y) / (l_y)))
    x_vals = np.arange(0, l_x_val, 0.001)
    y_vals = np.arange(0, l_y_val, 0.001)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    prob_density = sp.lambdify([l_x, l_y, n_x, n_y, x, y], equation ** 2, "numpy")
    prob_density_values = prob_density(l_x_val, l_y_val, n_x_val, n_y_val, x_vals, y_vals)
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    ax.plot_surface(x_vals, y_vals, prob_density_values, cmap=cm.inferno)
    plt.show()

def plot_2d_wave_function(l_x_val, l_y_val, n_x_val, n_y_val):
    fig = plt.figure(figsize=plt.figaspect(0.5))        
    fig.suptitle("Graph of the wave function for a 2D particle in a box system")
    plt.figtext(0.01, 0.5, f"L_x: {l_x_val}\nL_y: {l_y_val}\nn_x: {n_x_val}\nn_y: {n_y_val}")
    l_x, l_y, n_x, n_y, x, y = sp.symbols("l_x, l_y, n_x, n_y, x, y")
    equation = sp.sympify(sp.sqrt(4/(l_x * l_y)) * sp.sin((np.pi * n_x * x) / (l_x)) * sp.sin((np.pi * n_y * y) / (l_y)))
    x_vals = np.arange(0, l_x_val, 0.001)
    y_vals = np.arange(0, l_y_val, 0.001)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    wave_function = sp.lambdify([l_x, l_y, n_x, n_y, x, y], equation, "numpy")
    wave_function_values = wave_function(l_x_val, l_y_val, n_x_val, n_y_val, x_vals, y_vals)
    ax = fig.add_subplot(1,1,1, projection="3d")
    ax.plot_surface(x_vals, y_vals, wave_function_values, cmap=cm.inferno)
    plt.show()

if __name__ == "__main__":
    plot_2d_wave_function(l_x_val = 1, l_y_val = 1, n_x_val = 4, n_y_val = 4)
    plot_2d_prob_density(l_x_val = 1, l_y_val = 1, n_x_val = 4, n_y_val = 4)
