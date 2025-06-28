import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen mit manuell gesetzten Spaltennamen
df = pd.read_csv("mqtt_data.csv", header=None, names=["timestamp", "payload"])
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Dispenser und Temperatur extrahieren
df["dispenser"] = df["payload"].str.extract(r'"dispenser"\s*:\s*"(\w+)"')
df["temperature_C"] = df["payload"].str.extract(r'"temperature_C"\s*:\s*([0-9.]+)')
df["temperature_C"] = pd.to_numeric(df["temperature_C"], errors="coerce")

# Nur Zeilen mit Dispenser + Temperatur verwenden
df = df.dropna(subset=["temperature_C", "dispenser"])

# Daten für jeden Dispenser filtern
df_red = df[df["dispenser"] == "red"]
df_blue = df[df["dispenser"] == "blue"]
df_green = df[df["dispenser"] == "green"]

# Plot erstellen
plt.figure()
plt.plot(df_red["timestamp"], df_red["temperature_C"], label="Red Dispenser")
plt.plot(df_blue["timestamp"], df_blue["temperature_C"], label="Blue Dispenser")
plt.plot(df_green["timestamp"], df_green["temperature_C"], label="Green Dispenser")
plt.xlabel("Zeit")
plt.ylabel("Temperatur (°C)")
plt.title("Temperatur-Zeitreihen pro Dispenser")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_by_dispenser.png")
plt.show()
