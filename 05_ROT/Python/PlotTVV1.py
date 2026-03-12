import numpy as np
import matplotlib.pyplot as plt


h_cm = np.array([81.5, 75.5, 70.0, 65.5, 61.5, 59.0, 55.0, 52.0, 50.0, 47.5, 49.0, 43.5])
T_s  = np.array([10.42, 9.22, 9.90, 8.72, 8.39, 8.59, 7.53, 7.58, 7.38, 6.78, 6.18, 6.50])


h_err = np.full(len(h_cm), 0.2)  # in cm


T2 = T_s**2


a, b = np.polyfit(T2, h_cm, 1)


x_fit = np.linspace(T2.min()*0.95, T2.max()*1.05, 200)
y_fit = a * x_fit + b


plt.figure(figsize=(7,5))
plt.errorbar(T2, h_cm, yerr=h_err, fmt='o', capsize=4, label="Messwerte mit Fehler")
plt.plot(x_fit, y_fit, label=f"Linearer Fit: h = {a:.3f}·T² + {b:.3f}")

plt.xlabel(r"$T_n^2$ / s$^2$")
plt.ylabel(r"$h_n$ / cm")
plt.title(r"Maxwellsches Rad: $h_n$ gegen $T_n^2$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Fit-Parameter ausgeben
print(f"Steigung a = {a:.6f} cm/s²")
print(f"Achsenabschnitt b = {b:.6f} cm")