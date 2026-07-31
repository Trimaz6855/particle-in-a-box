import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from matplotlib.widgets import Slider
import numpy as np
import sympy as sp 

def plot_3d_prob_density(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val):

    fig, ax = plt.subplots(figsize=(7,6))
    plt.subplots_adjust(bottom=0.25)
    x_vals = np.linspace(0, l_x_val, 200)
    y_vals = np.linspace(0, l_y_val, 200)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)
    z_initial = l_z_val / 2
   
    def calculate(z_value):
        return (np.sqrt(8 / (l_x_val * l_y_val * l_z_val)) 
                * np.sin((np.pi * n_x_val * x_vals) / l_x_val)
                * np.sin((np.pi * n_y_val * y_vals) / l_y_val)
                * np.sin((np.pi * n_z_val * z_value) / l_z_val))
    
    pd_values = calculate(z_initial)
    im = plt.imshow(pd_values, cmap="inferno", vmin=0, vmax=(np.sqrt(8 / l_x_val * l_y_val * l_z_val)), extent=[0, l_x_val, 0, l_y_val], interpolation="nearest", origin="lower")
    plt.colorbar(im)
    ax.set_xlabel("x Position")
    ax.set_ylabel("y Position")

    ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03])
    z_slider = Slider(ax=ax_slider, label="z Position", valmin=0, valmax=l_z_val, valstep=0.01)

    def update(val):
        z_current = z_slider.val
        im.set_data(calculate(z_current))
        fig.canvas.draw_idle()

    z_slider.on_changed(update)
    plt.show()

def plot_3d_wave_function():
    pass

if __name__ == "__main__":
    plot_3d_prob_density(1,1,1,4,4,4)