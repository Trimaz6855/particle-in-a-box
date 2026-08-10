import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import cm

def plot_2d_prob_density(l_x_val, l_y_val, n_x_val, n_y_val):
    fig = plt.figure(figsize=plt.figaspect(0.5))
    fig.suptitle("Graph of the probabilty density function for a 2D particle in a box system")
    plt.figtext(0.01, 0.7, f"L_x: {l_x_val}\nL_y: {l_y_val}\nn_x: {n_x_val}\nn_y: {n_y_val}")
    x_vals = np.arange(0, l_x_val, 0.001)
    y_vals = np.arange(0, l_y_val, 0.001)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    prob_density_values = 4 / (l_x_val * l_y_val) * ((np.sin((np.pi * n_x_val * x_vals) / l_x_val) * np.sin((np.pi * n_y_val * y_vals) / l_y_val)) ** 2)
    ax = fig.add_subplot(1, 1, 1, projection="3d")
    ax.plot_surface(x_vals, y_vals, prob_density_values, cmap=cm.inferno)
    ax.set_xlabel("x Position")
    ax.set_ylabel("y Position")
    ax.set_zlabel("Probability Density")
    plt.show()

def plot_2d_wave_function(l_x_val, l_y_val, n_x_val, n_y_val):
    fig = plt.figure(figsize=plt.figaspect(0.5))        
    fig.suptitle("Graph of the wave function for a 2D particle in a box system")
    plt.figtext(0.01, 0.7, f"L_x: {l_x_val}\nL_y: {l_y_val}\nn_x: {n_x_val}\nn_y: {n_y_val}")
    x_vals = np.arange(0, l_x_val, 0.001)
    y_vals = np.arange(0, l_y_val, 0.001)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    wave_function_values = np.sqrt(4 / (l_x_val * l_y_val)) * np.sin((np.pi * n_x_val * x_vals) / l_x_val) * np.sin((np.pi * n_y_val * y_vals) / l_y_val)
    ax = fig.add_subplot(1,1,1, projection="3d")
    ax.plot_surface(x_vals, y_vals, wave_function_values, cmap=cm.inferno)
    ax.set_xlabel("x Position")
    ax.set_ylabel("y Position")
    ax.set_zlabel("Amplitude")
    plt.show()

if __name__ == "__main__":
    plot_2d_wave_function(l_x_val = 1, l_y_val = 1, n_x_val = 4, n_y_val = 4)
    plot_2d_prob_density(l_x_val = 1, l_y_val = 1, n_x_val = 4, n_y_val = 4)
