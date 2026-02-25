import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch
from math import sqrt

mode = "korrigiert"  # "korrigiert" oder "unkorrigiert"


x_p = [0, 4, 4.9, 7, 9.8, 11.8, 11.9, 10.5, 9.3, 7, 5]
y_p = [-2, 0.9, -0.7, 0.6, 3.4, 7.4, 12.5, 15.7, 17.7, 19.9, 21.3]
unsicherheit1 = [0, 0.4, 0.3, 0.3, 0.3, 0.4, 0.4, 0.3, 0.4, 0.3, 0.3]

x_t = [0, -4, -5.4, -7.8, -11.0, -13.3, -13.9, -13.2, -12, -9.7, -7.6]
y_t = [26.7, 26.3, 25.9, 24.8, 21.7, 17.7, 12.3, 8.5, 6.1, 3.7, 0.5]
unsicherheit2 = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.3, 0.4]

b = [0, 0.3, 0.4, 0.6, 0.9, 1.2, 1.5, 1.7, 1.8, 1.9, 1.95]
a = []
for i in b:
    a.append(sqrt(2*2 - i*i))

y_p_corr = [y_p[i] + a[i] for i in range(len(y_p))]
x_t_corr = [x_t[i] + b[i] for i in range(len(x_t))]

fig, ax = plt.subplots()

if mode == "korrigiert":
    ax.scatter(x_p, y_p_corr, marker='+', color='blue', zorder=3)
    ax.scatter(x_t_corr, y_t, marker='+', color='red', zorder=3)
    filename = "LandepunkteStossUndKorrektur.png"
    alphaOrig = 0.3
else:
    alphaOrig = 1
    filename = "LandepunkteStoss.png"

ax.scatter(0, 0, marker='o', color='black', zorder=4, label='Ursprung',)
ax.annotate('O', (0, 0), textcoords="offset points", xytext=(10,10), ha='center')
ax.scatter(0, 25.7/2, marker='o', color='black', zorder=4, label='M')
ax.annotate('M', (0, 25.7/2), textcoords="offset points", xytext=(10,10), ha='center')
ax.scatter(0, 23.2, marker='o', color='black', zorder=4, label='Flugweite ohne Stoß')
ax.annotate('Flugweite ohne Stoß', (0, 23.2), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=6)
ax.scatter(0, 25.7, marker='o', color='black', zorder=4, label='Korrigierte Flugweite')
ax.annotate('Korrigierte Flugweite', (0, 25.7), textcoords="offset points", xytext=(0,-10), ha='center', fontsize=6)
kreis_m = Circle((0, 25.7/2), 25.7/2,
                 edgecolor='black',
                 facecolor='none',
                 alpha=0.6,
                 linewidth=1)
ax.add_patch(kreis_m)

ax.scatter(x_p, y_p, marker='x', color='blue', zorder=3, alpha=alphaOrig)
ax.scatter(x_t, y_t, marker='x', color='red', zorder=3, alpha=alphaOrig)



# Unsicherheitskreise für Datensatz 1
for xi, yi, r, bi in zip(x_p, y_p, unsicherheit1, b):
    if r > 0:  # keine Kreise bei Radius 0
        kreis = Circle((xi, yi), r,
                       edgecolor='blue',
                       facecolor='none',
                       alpha=alphaOrig,
                       linewidth=1)
        ax.add_patch(kreis)
    ax.annotate(f"b={bi}",
                (xi, yi),
                backgroundcolor='white',
                bbox=dict(
                    facecolor='white',
                    alpha=0.7,
                    edgecolor='none',
                    boxstyle='square,pad=0.05',
                ),
                zorder=5,
                textcoords="offset points",
                xytext=(3, -10),
                fontsize=6,
                color='blue',
                ha = 'center')

# Unsicherheitskreise für Datensatz 2
for xi, yi, r, bi in zip(x_t, y_t, unsicherheit2, b):
    kreis = Circle((xi, yi), r,
                   edgecolor='red',
                   facecolor='none',
                   alpha=alphaOrig,
                   linewidth=1)
    ax.add_patch(kreis)
    ax.annotate(f"b={bi}",
                (xi, yi),
                backgroundcolor='white',
                bbox=dict(
                    facecolor='white',
                    alpha=0.7,
                    edgecolor='none',
                    boxstyle='square,pad=0.05',
                ),
                zorder=5,
                textcoords="offset points",
                xytext=(3, -10),
                fontsize=6,
                color='red',
                ha = 'center')


# Bemaßung zwischen ohne Stoß und korrigiert
y1 = 23.2
y2 = 25.7
x_dim = 4  # etwas links neben der y-Achse

ax.annotate(
    "",
    xy=(x_dim, y1),
    xytext=(x_dim, y2),
    arrowprops=dict(arrowstyle="<->")
)

ax.plot([0, x_dim], [y1, y1], color='black', linewidth=0.8, linestyle='dashed')
ax.plot([0, x_dim], [y2, y2], color='black', linewidth=0.8, linestyle='dashed')

# Maßtext
ax.text(
    x_dim + 1.3,
    (y1 + y2) / 2,
    f"{y2 - y1:.1f} cm",
    rotation=-90,
    va="center",
    ha="right"
)

# Unsicherheitskreise für Datensatz 1 + b-Wert beschriften

# Achsenbeschriftung
ax.set_xlabel("X-Position (cm)")
ax.set_ylabel("Y-Position (cm)")
ax.set_title("Landepunkte der Kugeln")

# Gleich skalierte Achsen (wichtig für echte Kreise!)
ax.set_aspect('equal', 'box')

# Gitter
ax.grid(True)

red_patch = Patch(color='red', label='Targetkugel')
blue_patch = Patch(color='blue', label='Projektilkugel')
plt.legend(handles=[red_patch, blue_patch, Patch(color='black', label='Theorie')], loc='upper right', fontsize=6)

# plt.show()
plt.savefig(f"./01_STO/Images/{filename}", dpi=1000, bbox_inches='tight')