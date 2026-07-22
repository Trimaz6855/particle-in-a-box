import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sympy as sp 
from matplotlib import cm

def plot_1d_prob_density(l_x_val, n_x_val):
    fig = plt.figure(figsize=plt.figaspect(0.5))
    fig.suptitle("Graph of the probability density function for a 1D particle in a box system")
    plt.figtext(0.01, 0.5, f"L_x: {l_x_val}\nN_x: {n_x_val}")
    l_x, n_x, x = sp.symbols("l_x, n_x, x")
    equation = sp.sympify(sp.sqrt(2/l_x) * sp.sin((n_x * sp.pi * x) / l_x))
    x_vals = np.arange(0, l_x_val, 0.001)
    prob_density = sp.lambdify([l_x, n_x, x], equation ** 2, "numpy")
    prob_vals = prob_density(l_x_val, n_x_val, x_vals)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_vals, prob_vals)
    plt.show()

def plot_1d_wave_function(l_x, n_x):
    pass

if __name__ == "__main__":
    plot_1d_prob_density(1, 4)
    plot_1d_wave_function(1, 4)