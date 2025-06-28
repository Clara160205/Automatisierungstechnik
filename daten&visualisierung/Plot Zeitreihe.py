import pandas as pd
import matplotlib.pyplot as plt

# CSV laden
df = pd.read_csv("mqtt_data.csv", parse_dates=["timestamp"])

# Ein Beispiel-Plot für eine einfache Zeitreihe
plt.figure()
df["value"] = df["payload"].str.extract(r"\"value\":\s*([0-9\.]+)")  # wenn JSON-Wert z.B. {"value": 42.3}
df["value"] = pd.to_numeric(df["value"], errors="coerce")
df.dropna(inplace=True)

plt.plot(df["timestamp"], df["value"])
plt.xlabel("Zeit")
plt.ylabel("Messwert")
plt.title("Zeitreihe eines Sensors aus MQTT")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("zeitreihe_plot.png")
plt.show()
