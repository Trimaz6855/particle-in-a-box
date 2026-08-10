import timeit
import numpy as np
import calc3Dim

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
print(f"Speedup: {t1/t2:.6f}x")
print(f"Further Speedup: {t2/t3:.6f}x")