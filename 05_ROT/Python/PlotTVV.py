import numpy as np
import matplotlib.pyplot as plt

# Daten
I = np.array([8.61, 5.18, 2.76, 1.366]) * 1e-3
dI = np.array([0.06, 0.05, 0.03, 0.012]) * 1e-3

a = np.array([100.45, 74.35, 49.45, 26.45])  # mm
da = np.array([0.05, 0.05, 0.05, 0.05])

# Umrechnung in Meter
a = a * 1e-3
da = da * 1e-3

# a^2 und Fehler
a2 = a**2
da2 = 2 * a * da

# Gewichteter linearer Fit (Gewichte = 1/σ)
p, cov = np.polyfit(a2, I, 1, w=1/dI, cov=True)

m, b = p
dm, db = np.sqrt(np.diag(cov))

# Fitlinie
x_fit = np.linspace(min(a2)*0.9, max(a2)*1.1, 100)
y_fit = m * x_fit + b

# Plot
plt.errorbar(a2, I, xerr=da2, yerr=dI, fmt='o', capsize=4, label="Messdaten")

plt.plot(
    x_fit,
    y_fit,
    label=rf"Fit: $I=( {m:.3e})a^2 + ({b:.3e})$"
)

plt.xlabel(r"$a^2\ (\mathrm{m}^2)$")
plt.ylabel("I (kg*m²)")
plt.title(r"$I$ gegen $a^2$")
plt.grid(True)
plt.legend()

plt.savefig("./Images/PlotIV.png", dpi=500)
# plt.show()

print(f"m = ({m:.3e} ± {dm:.3e}) kg")
print(f"b = ({b:.3e} ± {db:.3e}) kg m²")