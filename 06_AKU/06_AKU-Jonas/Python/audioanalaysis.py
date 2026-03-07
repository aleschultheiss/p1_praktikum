import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.widgets import Slider
import numpy as np

# Datei laden
file_path = "MitRohr.csv"
file_path_control = "OhneRohr.csv"

df = pd.read_csv(file_path)
df.columns = ["frequency", "time", "fft_mag"]

mean_fft = df.groupby("frequency")["fft_mag"].mean().reset_index()

df2 = pd.read_csv(file_path_control)
df2.columns = ["frequency", "time", "fft_mag"]

mean_fft2 = df2.groupby("frequency")["fft_mag"].mean().reset_index()

# Differenz berechnen
merged = pd.merge(mean_fft, mean_fft2, on="frequency", suffixes=("_1", "_2"))
merged["difference"] = merged["fft_mag_1"] - merged["fft_mag_2"]

# Peaks im Differenzspektrum
peaks, properties = find_peaks(merged["difference"], prominence=5)

peak_freqs = merged["frequency"].iloc[peaks]
peak_values = merged["difference"].iloc[peaks]

print("Gefundene Resonanzfrequenzen:")
for f, v in zip(peak_freqs, peak_values):
    print(f"{f:.2f} Hz  ->  {v:.2f}")

# Plot
fig, ax = plt.subplots(figsize=(10,5))
plt.subplots_adjust(bottom=0.25)

ax.plot(mean_fft["frequency"], mean_fft["fft_mag"],
        color="blue", linestyle=":", label="Mit Rohr")

ax.plot(mean_fft2["frequency"], mean_fft2["fft_mag"],
        color="green", linestyle=":", label="Ohne Rohr")

ax.plot(merged["frequency"], merged["difference"],
        color="red", label="Differenz")

ax.scatter(peak_freqs, peak_values,
           color="black", zorder=3, label="Maxima (Differenz)")

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Mean FFT Magnitude (arb. unit)")
ax.set_title("Zeitlich gemitteltes FFT-Spektrum")
ax.grid(True)

# Slider Achse
ax_slider = plt.axes([0.2, 0.03, 0.6, 0.03])
slider = Slider(ax_slider, "Grundfrequenz (Hz)", 400, 600, valinit=400)

# Liste der Linien
harmonic_lines = []

def update(val):
    global harmonic_lines
    
    # alte Linien entfernen
    for line in harmonic_lines:
        line.remove()
    harmonic_lines = []

    f0 = slider.val
    max_freq = merged["frequency"].max()

    n_max = int(max_freq // f0)

    for n in range(1, n_max+1):
        line = ax.axvline(n*f0, color="purple", linestyle="--", alpha=0.6)
        harmonic_lines.append(line)

    fig.canvas.draw_idle()

slider.on_changed(update)

# initiale Linien
update(slider.val)

ax.legend()

plt.tight_layout()
plt.show()