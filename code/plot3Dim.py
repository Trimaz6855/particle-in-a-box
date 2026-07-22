import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from matplotlib.widgets import Slider
import numpy as np
import sympy as sp 

def plot_3d_prob_density(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val):

    fig, ax = plt.subplots(figsize=(7,6))
    plt.subplots_adjust(bottom=0.25)
    x_vals = np.arange(0, l_x_val, 0.001)
    y_vals = np.arange(0, l_y_val, 0.001)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    l_x, l_y, l_z, n_x, n_y, n_z, x, y, z = sp.symbols("l_x, l_y, l_z, n_x, n_y, n_z, x, y, z")
    equation = sp.sympify(sp.sqrt(8 / (l_x * l_y * l_z)) * sp.sin((sp.pi * n_x * x) / l_x) * sp.sin((sp.pi * n_y * y) / l_y) * sp.sin((sp.pi * n_z * z) / l_z))
    z_initial = 0.23

    def calculate(z_value):
        prob_density = sp.lambdify([l_x, l_y, l_z, n_x, n_y, n_z, x, y, z], equation ** 2, "numpy")
        return prob_density(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val, x_vals, y_vals, z_value)

    pd_values = calculate(z_initial)
    mesh = ax.pcolormesh(x_vals, y_vals, pd_values, cmap="inferno", vmin=0, vmax=(8/(l_x_val * l_y_val * l_z_val)), shading="auto")
    colourbar = fig.colorbar(mesh, ax=ax, label="Probability Density")
    ax.set_xlabel("x Position")
    ax.set_ylabel("y Position")

    ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03])
    z_slider = Slider(ax=ax_slider, label="z Position", valmin=0, valmax=l_z_val, valstep=0.01)

    def update(val):
        z_current = z_slider.val
        mesh.set_array(calculate(z_current).flatten())
        fig.canvas.draw_idle()

    z_slider.on_changed(update)

    plt.show()

def plot_3d_wave_function():
    pass

if __name__ == "__main__":
    plot_3d_prob_density(1,1,1,4,4,4)