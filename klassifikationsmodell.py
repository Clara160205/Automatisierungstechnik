import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

# === 1. Beispielhafte Daten generieren oder laden ===
# Für die Demo: 500 Vibrationswerte + Label is_cracked
def generate_demo_data(n_samples=100):
    np.random.seed(42)
    data = []
    for i in range(n_samples):
        label = np.random.choice([0, 1])  # 0 = intakt, 1 = defekt
        if label == 0:
            vibration = np.random.normal(loc=0, scale=1, size=500)
        else:
            vibration = np.random.normal(loc=0, scale=2.5, size=500)
        data.append(np.concatenate(([label], vibration)))
    columns = ["is_cracked"] + [f"vib_{i}" for i in range(500)]
    return pd.DataFrame(data, columns=columns)

df = generate_demo_data()

# === 2. Merkmale extrahieren ===
df["mean"] = df.iloc[:, 1:].mean(axis=1)
df["std"] = df.iloc[:, 1:].std(axis=1)
df["max"] = df.iloc[:, 1:].max(axis=1)
df["min"] = df.iloc[:, 1:].min(axis=1)
features = ["mean", "std", "max", "min"]
X = df[features]
y = df["is_cracked"]

# === 3. Daten aufteilen ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# === 4. Modell trainieren (kNN und LogReg als Vergleich) ===
models = {
    "kNN": KNeighborsClassifier(n_neighbors=3),
    "LogReg": LogisticRegression()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n🧠 Modell: {name}")
    print(classification_report(y_test, y_pred, digits=3))
    
    # Confusion Matrix anzeigen
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["intakt", "defekt"], yticklabels=["intakt", "defekt"])
    plt.title(f"Confusion Matrix – {name}")
    plt.xlabel("Vorhergesagt")
    plt.ylabel("Tatsächlich")
    plt.tight_layout()
    plt.show()
