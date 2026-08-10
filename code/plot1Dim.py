import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import cm

def plot_1d_prob_density(l_x_val, n_x_val):
    fig = plt.figure(figsize=plt.figaspect(0.5))
    fig.suptitle("Graph of the probability density function for a 1D particle in a box system")
    plt.figtext(0.01, 0.9, f"L_x: {l_x_val}\nN_x: {n_x_val}")
    x_vals = np.arange(0, l_x_val, 0.001)
    prob_vals = (2 / l_x_val) * (np.sin((np.pi * n_x_val * x_vals) / l_x_val) ** 2)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_vals, prob_vals)
    fig.supxlabel("x Position")
    fig.supylabel("Probability Density")
    plt.show()

def plot_1d_wave_function(l_x_val, n_x_val):
    fig = plt.figure(figsize=plt.figaspect(0.5))
    fig.suptitle("Graph of the wave function for a 1D particle in a box system")
    plt.figtext(0.01, 0.9, f"L_x: {l_x_val}\nN_x: {n_x_val}")
    x_vals = np.arange(0, l_x_val, 0.001)
    wave_vals = np.sqrt(2 / l_x_val) * np.sin((np.pi * n_x_val * x_vals) / l_x_val)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x_vals, wave_vals)
    fig.supxlabel("x Position")
    fig.supylabel("Amplitude")
    plt.show()

if __name__ == "__main__":
    plot_1d_prob_density(1, 4)
    plot_1d_wave_function(1, 4)