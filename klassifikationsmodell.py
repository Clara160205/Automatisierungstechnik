import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, confusion_matrix
import matplotlib.pyplot as plt

# CSV einlesen
df = pd.read_csv("mqtt_data_structured.csv", converters={"drop_oscillation": str})
df['drop_oscillation'] = df['drop_oscillation'].str.strip()
df = df[df['drop_oscillation'].notna() & (df['drop_oscillation'] != '')]

# Parser-Funktion
def parse_osc_string(entry):
    try:
        entry = entry.strip("[]")
        if entry.strip() == "":
            return np.nan
        parts = entry.split(",")
        floats = [float(p.strip().strip("'").strip('"')) for p in parts if p.strip()]
        return floats if len(floats) >= 5 else np.nan
    except Exception as e:
        print(f"❌ Fehler beim Parsen: {e} → Eintrag: {entry[:50]}...")
        return np.nan

df['osc_list'] = df['drop_oscillation'].apply(parse_osc_string)
df = df[df['osc_list'].apply(lambda x: isinstance(x, list) and len(x) >= 5)]

# Ensure is_cracked exists
df = df[df['is_cracked'].notna()]

# Now extract features
df['osc_mean'] = df['osc_list'].apply(np.mean)
df['osc_std'] = df['osc_list'].apply(np.std)
df['osc_max'] = df['osc_list'].apply(np.max)

# Check the data before proceeding
print("✅ Rows in DataFrame:", len(df))
print(df[['osc_mean', 'osc_std', 'osc_max']].describe())


# Featuresets
X1 = df[['osc_mean']]
X2 = df[['osc_mean', 'osc_std', 'osc_max']]

print("📏 X1 shape:", X1.shape)
print("🔍 First few rows:\n", X1.head())
# Skalierung
scaler1 = StandardScaler().fit(X1)
X1_scaled = scaler1.transform(X1)

scaler2 = StandardScaler().fit(X2)
X2_scaled = scaler2.transform(X2)

# Train-Test-Split
X1_train, X1_test, y_train, y_test = train_test_split(X1_scaled, y, test_size=0.3, random_state=42)
X2_train, X2_test, _, _ = train_test_split(X2_scaled, y, test_size=0.3, random_state=42)

# Modell 1: kNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X1_train, y_train)
f1_knn = f1_score(y_test, knn.predict(X1_test))

# Modell 2: Log. Regression
logreg = LogisticRegression()
logreg.fit(X2_train, y_train)
f1_log = f1_score(y_test, logreg.predict(X2_test))

# Ergebnisse anzeigen
results = pd.DataFrame({
    "Genutzte Features": ["osc_mean", "osc_mean + osc_std + osc_max"],
    "Modell-Typ": ["kNN", "Log. Regression"],
    "F1-Score (Test)": [f1_knn, f1_log]
})
print("\n📊 Klassifikationsergebnisse:")
print(results.to_string(index=False))

# Confusion Matrix zur Log. Regression
print("\nConfusion Matrix für logistische Regression:")
print(confusion_matrix(y_test, logreg.predict(X2_test)))
