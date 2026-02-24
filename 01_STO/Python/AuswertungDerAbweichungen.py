import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

x_p = [0, 4, 4.9, 7, 9.8, 11.8, 11.9, 10.5, 9.3, 7, 5]
y_p = [-2, 0.9, -0.7, 0.6, 3.4, 7.4, 12.5, 15.7, 17.7, 19.9, 21.3]
unsicherheit1 = [0, 0.4, 0.3, 0.3, 0.3, 0.4, 0.4, 0.3, 0.4, 0.3, 0.3]

x_t = [0, -4, -5.4, -7.8, -11.0, -13.3, -13.9, -13.2, -12, -9.7, -7.6]
y_t = [26.7, 26.3, 25.9, 24.8, 21.7, 17.7, 12.3, 8.5, 6.1, 3.7, 0.5]
unsicherheit2 = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.3, 0.4]

b = [0, 0.3, 0.4, 0.6, 0.9, 1.2, 1.5, 1.7, 1.8, 1.9, 1.95]
a = [sqrt(4 - i**2) for i in b]

y_p_corr = [y_p[i] + a[i] for i in range(len(y_p))]
x_t_corr = [x_t[i] + b[i] for i in range(len(x_t))]

xc, yc = 0, 25.7/2
R = 25.7/2

# Projektilkugel (korrigiert)
x_proj = np.array(x_p)
y_proj = np.array(y_p_corr)
b_proj = np.array(b)
uns_proj = np.array(unsicherheit1)

# Targetkugel (korrigiert)
x_targ = np.array(x_t_corr)
y_targ = np.array(y_t)
b_targ = np.array(b)
uns_targ = np.array(unsicherheit2)

# Abweichungen vom Kreisradius
dev_proj = np.abs(np.sqrt((x_proj - xc)**2 + (y_proj - yc)**2) - R)
dev_targ = np.abs(np.sqrt((x_targ - xc)**2 + (y_targ - yc)**2) - R)

# Neues Diagramm erstellen
fig2, ax2 = plt.subplots(figsize=(6,4))

# Projektilkugel mit Fehlerbalken
ax2.errorbar(b_proj, dev_proj, yerr=uns_proj, fmt='o', color='blue',
             ecolor='lightblue', elinewidth=1, capsize=3, label='Projektilkugel')

# Targetkugel mit Fehlerbalken
ax2.errorbar(b_targ, dev_targ, yerr=uns_targ, fmt='o', color='red',
             ecolor='lightcoral', elinewidth=1, capsize=3, label='Targetkugel')

# Optional: Verbindungslinien
ax2.plot(b_proj, dev_proj, color='blue', linestyle='--', alpha=0.5)
ax2.plot(b_targ, dev_targ, color='red', linestyle='--', alpha=0.5)

# Achsen und Titel
ax2.set_xlabel("b (cm)")
ax2.set_ylabel("Abweichung vom Kreis Δ (cm)")
ax2.set_title("Abweichung vom Kreis in Abhängigkeit von b")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("./01_STO/Images/AbweichungenKorrigierteLandepunkte.png", dpi=1000, bbox_inches='tight')
plt.show()