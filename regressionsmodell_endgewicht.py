import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("X.csv")
y = df['fill_level_grams_red'] + df['fill_level_grams_blue'] + df['fill_level_grams_green']

features_list = [
    ['fill_level_grams_red'],
    ['fill_level_grams_blue'],
    ['fill_level_grams_green'],
    ['temperature_red', 'temperature_blue', 'temperature_green'],
    ['fill_level_grams_red', 'fill_level_grams_blue', 'fill_level_grams_green'],
    ['fill_level_grams_red', 'fill_level_grams_blue', 'temperature_green'],
    ['fill_level_grams_red', 'fill_level_grams_blue'],
    ['fill_level_grams_red', 'temperature_red', 'fill_level_grams_blue', 'temperature_blue', 'fill_level_grams_green', 'temperature_green']
]

results = []
for features in features_list:
    X = df[features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    mse_train = mean_squared_error(y_train, y_train_pred)
    mse_test = mean_squared_error(y_test, y_test_pred)
    results.append({
        "Genutzte Spalten": features,
        "Modell-Typ": "Linear",
        "MSE-Wert (Training)": round(mse_train, 2),
        "MSE-Wert (Test)": round(mse_test, 2)
    })

y_hat = model.predict(X)
output = pd.DataFrame({
    "Flaschen ID": df['bottle'],
    "y_hat": y_hat
})
output.to_csv("reg_52315895-52216154.csv", index=False)    

results_df = pd.DataFrame(results)
print(results_df)
