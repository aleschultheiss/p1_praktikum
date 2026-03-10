import numpy as np
import matplotlib.pyplot as plt

# Unsicherheit
d_err = 0.5   
t_err = 0.2   

# Normale Temp
d_rt = np.array([1.0, 3.0, 1.2, 1.2, 1.3, 1.2, 1.0, 1.1, 0.8, 1.0])
t_rt = np.array([10.44, 2.31, 2.31, 6.37, 5.72, 6.11, 9.94, 5.97, 12.25, 5.97])

# Kalt
d_kalt = np.array([1.0, 0.8, 2.0, 5.0, 1.1, 1.2, 0.8, 1.0, 3.5, 1.2])
t_kalt = np.array([11.35, 14.77, 4.38, 1.20, 8.63, 8.22, 12.64, 10.01, 3.16, 8.39])

# Fehlerarrays
d_rt_err = np.full_like(d_rt, d_err, dtype=float)
t_rt_err = np.full_like(t_rt, t_err, dtype=float)

d_kalt_err = np.full_like(d_kalt, d_err, dtype=float)
t_kalt_err = np.full_like(t_kalt, t_err, dtype=float)

# Plot 1
plt.figure(figsize=(8, 5))
plt.errorbar(
    d_rt, t_rt,
    xerr=d_rt_err, yerr=t_rt_err,
    fmt='o', capsize=4
)
plt.xlabel('Blasendurchmesser d / mm')
plt.ylabel('Aufstiegszeit t / s')
plt.title('TV1: Durchmesser gegen Aufstiegszeit bei Raumtemperatur')
plt.grid(True)
plt.tight_layout()
plt.savefig('TV1_Raumtemperatur_Durchmesser_Zeit.png', dpi=300)
plt.show()

# Plot 2: Kalt
plt.figure(figsize=(8, 5))
plt.errorbar(
    d_kalt, t_kalt,
    xerr=d_kalt_err, yerr=t_kalt_err,
    fmt='o', capsize=4
)
plt.xlabel('Blasendurchmesser d / mm')
plt.ylabel('Aufstiegszeit t / s')
plt.title('TV1: Durchmesser gegen Aufstiegszeit bei niedriger Temperatur')
plt.grid(True)
plt.tight_layout()
plt.savefig('TV1_Kalt_Durchmesser_Zeit.png', dpi=300)
plt.show()