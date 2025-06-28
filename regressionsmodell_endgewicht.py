import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("C:/Users/Nutzer/Downloads/X.csv")

sns.pairplot(df[['vibration_index_green', 'temperature_green', 'fill_level_grams_green']])
plt.show()

y = df['fill_level_grams_green']
X = df.drop(columns=['bottle', 'fill_level_grams_green'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.head())
print(y_train.head())

model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

plt.scatter(y_train, y_train_pred, alpha=0.7)
plt.xlabel("Echte Werte")
plt.ylabel("Vorhergesagte Werte")
plt.title("Trainingsdaten: Prediction vs. Ground Truth")
plt.grid(True)
plt.show()


print(f"\n MSE (Train): {mean_squared_error(y_train, y_train_pred):.2f}")
print(f"MSE (Test): {mean_squared_error(y_test, y_test_pred):.2f}")
print(f"Root MSE:  {mean_squared_error(y_test, y_test_pred)**0.5}")
