import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("mqtt_data_structured.csv")


df["timestamp"] = pd.to_datetime(df["timestamp"])
zeitwert = "temperature_c" 

plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df[zeitwert], marker='o', linestyle='-')
plt.title(f"{zeitwert} über Zeit")
plt.xlabel("Zeit")
plt.ylabel(zeitwert)
plt.tight_layout()
plt.savefig("zeitreihe_plot.png")
plt.show()
