import pandas as pd
import matplotlib.pyplot as plt

# Datei einlesen
file_path = "data.csv"

df = pd.read_csv(file_path)

# Spalten extrahieren
frequency = df["Frequency (Hz)"]
amplitude = df["Absolute Amplitude (a.u.)"]

# Plot erstellen
plt.figure(figsize=(10, 5))
plt.plot(frequency, amplitude)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Absolute Amplitude (a.u.)")
plt.title("Frequency Spectrum")
plt.grid(True)

plt.tight_layout()
plt.show()