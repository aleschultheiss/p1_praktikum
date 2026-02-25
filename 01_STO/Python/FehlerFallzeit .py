import numpy as np
import matplotlib.pyplot as plt

# Messindex
x = np.array([1, 2, 3])

# Zugehörige Höhen
hoehen = [0.53, 0.715, 1.065]

# Theorie- und Messwerte
t_the = np.array([0.3288, 0.3818, 0.4660])
t_mess = np.array([0.343, 0.395, 0.478])

# Messunsicherheit
err_mess = np.array([0.004, 0.004, 0.004])

# Fehler (Differenz)
delta_t = t_mess - t_the

# Lineare Ausgleichsgerade
coef = np.polyfit(x, delta_t, 1)
fit = np.poly1d(coef)

# Plot
plt.figure(figsize=(6,4))

plt.errorbar(x, delta_t, yerr=err_mess, fmt='o', capsize=3,
             label=r'$\Delta t = t_{mess} - t_{the}$')

# Gerade nur zwischen 1 und 3
plt.plot([1,3], fit([1,3]), linestyle='--',
         label='Tendenz')

plt.axhline(0, linestyle=':', linewidth=1)

# Eigene Tick-Beschriftung mit Höhen
labels = [f"{i}\n(h = {h} m)" for i, h in zip(x, hoehen)]
plt.xticks(x, labels)

plt.xlabel("Messindex i")
plt.ylabel("Zeitdifferenz Δt (s)")
plt.title("Abweichung zwischen Messung und Theorie")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("./01_STO/Images/FehlerFallzeit.png")
plt.show()

# Geradengleichung
print("Ausgleichsgerade:")
print(f"Δt(x) = {coef[0]:.6f} * x + {coef[1]:.6f}")