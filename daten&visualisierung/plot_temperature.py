import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("mqtt_data_structured.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["temperature_c"] = pd.to_numeric(df["temperature_c"], errors="coerce")

df = df.dropna(subset=["timestamp", "dispenser", "temperature_c"])

df_red = df[df["dispenser"] == "red"]
df_blue = df[df["dispenser"] == "blue"]
df_green = df[df["dispenser"] == "green"]

plt.figure(figsize=(10, 5))
plt.plot(df_red["timestamp"], df_red["temperature_c"], label="Red Dispenser")
plt.plot(df_blue["timestamp"], df_blue["temperature_c"], label="Blue Dispenser")
plt.plot(df_green["timestamp"], df_green["temperature_c"], label="Green Dispenser")

plt.xlabel("Zeit")
plt.ylabel("Temperatur (°C)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_by_dispenser.png")
plt.show()
