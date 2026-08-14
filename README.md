# Particle in a box visualisation program
## Intentions
This project is intended to be a simple gui based program that allows the user to choose the number of dimensions the box the particle is contained within has (up to 3 dimensions) and then input the following information:

- The length of the box in each dimension.
- The energy state of the particle in each dimension.

the user can then press a button to generate a graph of the probability density function or wave function of the particle.

I am designing this program as an extension of my 1st year physics module on Quantum Physics.

## Particle in a 1 Dimensional Box

## Particle in a 2 Dimensional Box

## Particle in a 3 Dimensional Box


### Implementation:

The original function for calculating the probability density values used 3 numpy arrays consisting of 1000 values each, as well as using sympy to define the probability density function and calculate the probability density values.

The original function is shown below:

```
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
```

The optimised function for calculating the probability density values uses 3 numpy arrays consisting of 200 values each, as well as still using sympy to define the probability density function and calculate the probability density values.

The optimised function is shown below:

```
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
```

The further optimised function removes the usage of sympy, defining the function using numpy alone, whilst still using 3 arrays of length 200.

The further optimised function is shown below:

```
def calculate3(l_x_val, l_y_val, l_z_val, n_x_val, n_y_val, n_z_val, z_value):

    x_vals = np.linspace(0, l_x_val, 200)
    y_vals = np.linspace(0, l_y_val, 200)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)

    pd_values = (np.sqrt(8 / (l_x_val * l_y_val * l_z_val)) 
                * np.sin((np.pi * n_x_val * x_vals) / l_x_val)
                * np.sin((np.pi * n_y_val * y_vals) / l_y_val)
                * np.sin((np.pi * n_z_val * z_value) / l_z_val))

    return pd_values
```

### Testing:

Using the test script below I tested the time taken for each of these functions to calculate the probability density for each value of x, y and z 10 times, before printing the average amount of time taken to calculate all probability density values once.

```
z_vals = np.linspace(0, 1, 1000)
z_vals_2 = np.linspace(0,1, 200)

t1 = timeit.timeit(
    lambda: [calc3Dim.calculate(1,1,1,4,4,4,z) for z in z_vals],
    number = 10
)

t2 = timeit.timeit(
    lambda: [calc3Dim.calculate2(1,1,1,4,4,4,z) for z in z_vals_2],
    number = 10
)

t3 = timeit.timeit(
    lambda: [calc3Dim.calculate3(1,1,1,4,4,4,z) for z in z_vals_2],
    number = 10
)

print(f"Original: {t1/10:.6f} s")
print(f"Optimised: {t2/10:.6f} s")
print(f"Further Optimised: {t3/10:.6f} s")
print(f"Speedup: {t1/t2:.2f}x")
print(f"Further Speedup: {t2/t3}x")
```

The results of the test script are shown below:

| Method           | Time per full calculation (s)| Performance Improvement (Relative to method above)|
|:-----------------|:----------------------------:|--------------------------------------------------:|
|Original          |29.309580                     |1x                                                 |
|Optimised         |0.390079                      |75.137497x                                         |
|Further Optimised |0.183762                      |2.122745x                                          |


The screenshot below shows the full, unrounded results from the test script.

![alt text](/images/tests/terminal-test-screenshot.png)
