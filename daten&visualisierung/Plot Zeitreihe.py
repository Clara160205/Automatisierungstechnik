import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("mqtt_data_structured.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["fill_level_grams"] = pd.to_numeric(df["fill_level_grams"], errors="coerce")

df = df.dropna(subset=["timestamp", "dispenser", "fill_level_grams"])

df_red = df[df["dispenser"] == "red"]
df_blue = df[df["dispenser"] == "blue"]
df_green = df[df["dispenser"] == "green"]

plt.figure(figsize=(10, 5))
plt.plot(df_red["timestamp"], df_red["fill_level_grams"], label="Red Dispenser")
plt.plot(df_blue["timestamp"], df_blue["fill_level_grams"], label="Blue Dispenser")
plt.plot(df_green["timestamp"], df_green["fill_level_grams"], label="Green Dispenser")

plt.xlabel("Zeit")
plt.ylabel("Füllstand ")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("filllevel_by_dispenser.png")
plt.show()