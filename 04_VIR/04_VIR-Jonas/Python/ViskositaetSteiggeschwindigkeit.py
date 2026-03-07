import numpy as np

# ---------------------------
# Messwerte (nur Zahlen!)
# ---------------------------

radius = np.array([2.1, 3.8, 2.8, 2.7, 1.8, 5.8, 2.5, 4.6, 6.6, 2.2])  # mm
_radius = radius * 0.001
time = np.array([68.9, 11.9, 36.9, 14.0, 59.4, 10.8, 35.9, 12.7, 7.5, 88.6])  # s
distance = np.array([8, 4, 8, 4, 8, 4, 4, 4, 4, 8]) #cm
velocity = np.zeros(10)  # cm/s
viscosity = np.zeros(10)
for i in range(10):
    velocity[i] = (distance[i]/time[i])
    _velocity = velocity * 0.01
    viscosity[i] = ((2*9.81*_radius[i]*_radius[i])/(9*_velocity[i])*1000)
print(velocity)
# viscosity = np.array([5.28, 4.44, 3.74, 3.71, 4.21, 3.36, 3.95, 3.88, 2.76, 3.10])  # Pa s

# ---------------------------
# konstante Unsicherheiten
# ---------------------------

radius_err = 0.5   # mm
time_err = 0.3     # s

# ---------------------------
# Latex Tabelle erzeugen
# ---------------------------

print(r"""\begin{table}[H]
    \centering
    \caption{Aufstiegsgeschwindigkeiten der Luftblasen bei Raumtemperatur}
    \label{tab:AufstiegLuftblasenRT}
    \begin{tabular}{c c c c}
        \hline
        Radius der Luftblase($r_k$) & Aufstiegszeit ($t_{steig}$) & Steiggeschwindigkeit ($v_{steig}$) & Viskosität ($\eta$) \\
        \hline""")

for r, t, v, eta in zip(radius, time, velocity, viscosity):

    radius_str = f"({r:.1f} \\pm {radius_err})mm"
    time_str = f"({t:.1f} \\pm {time_err})s"

    print(
        f"        ${radius_str}$ & ${time_str}$ & "
        f"${v:.3f} \\si{{\\cm}} / \\si{{\\s}}$  & "
        f"${eta:.2f} \\si{{\\Pa}} \\cdot \\si{{\\s}}$\\\\"
    )

print(r"""        \hline
    \end{tabular}
\end{table}""")