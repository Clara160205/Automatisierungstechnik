1. MQTT_Client für SPS

Der MQTT_Client verbindet sich mit einem MQTT-Broker und sendet Daten an ein Topic sendet. Der Client sendet periodisch Füllstandsdaten für eine Flasche, die zufällig generiert werden.  Der Client bleibt aktiv, bis er manuell beendet wird.    

2. Datenspeicherung und Visualisierung

Zunächst werden die  Daten aus dem Topic iot1/teaching_factory in einer csv. Datei gespeichert. 
Hier werden die Daten  noch nicht sortiert, sondern werden nur nach ihrem Erstellungsdatum sortiert.  Diese einfache Speicherung ermöglicht eine spätere flexible Sortierung und Verarbeitung der Daten. Anschließend wird diese csv. Datei anhand der verschiedenen Kategorie sortiert, um die spätere Visualisierung zu erleichtern. Da während des Speichervorgangs die Verbindung zum Topic abgebrochen ist, werden in der sortierten csv. nur noch die Daten nach dem Wiederaufbau der Verbindung gespeichert. Dabei wird der .json Payload in ein Dictionary umgewandelt und in eine Liste von Dictionaries gespeichert. 

Um den Verlauf der Daten zu verfolgen, werden Zeitreihen der Temperatur pro Dispenser geplottet. 

![Temperatur-Plot](temperature_by_dispenser.png) 

Ausserdem wird der Füllstand der Flaschen geplottet. 

![Füllstand-Plot](filllevel_by_dispenser.png)


3. Regressionsmodell für Endgewicht

Das Regressionsmodell wird verwendet, um das Endgewicht der Flaschen basierend auf dem Füllstand und der Temperatur vorherzusagen. Das Endgewicht wird als Summe der Füllstände der drei Flaschen berechnet. Das Modell verwendet verschiedene Kombinationen von Füllstand- und Temperaturdaten, um die beste Vorhersagegenauigkeit zu erreichen. Zudem werden verschiedene Regressionsmodelle wie Lineare Regression, Gradient Boosting und Random Forest verwendet. Die Modelle werden auf den skalierten Daten trainiert und die Mean Squared Error (MSE) Werte für Training und Test werden berechnet, um die Leistung der Modelle zu bewerten. Je kürzer der MSE-Wert, desto besser ist die Vorhersage des Modells. Der Random Forrest erstellt viele Entscheidungsbäume mit zufällig ausgewählten Daten und Merkmalen. Die Vorhersagen der Bäume werden aggregiert (bei Regression der Durchschnitt), um genauere Ergebnisse zu erzielen und Überanpassung zu vermeiden. Der Gradient Boosting Algorithmus erstellt sequentiell Entscheidungsbäume, wobei jeder Baum die Fehler des vorherigen Baums korrigiert. Dadurch wird die Genauigkeit der Vorhersage verbessert. 

                                     Genutzte Spalten         Modell-Typ  MSE-Wert (Training)  MSE-Wert (Test)
0   fill_level_grams_red, fill_level_grams_red, f...  Linear Regression             83168.93         71675.19
1   fill_level_grams_red, fill_level_grams_red, f...  Gradient Boosting             28211.19         61033.80
2   fill_level_grams_red, fill_level_grams_red, f...      Random Forest             24630.55         67982.43
3   fill_level_grams_blue, fill_level_grams_blue,...  Linear Regression             68410.10         74259.43
4   fill_level_grams_blue, fill_level_grams_blue,...  Gradient Boosting               448.70          1690.17
5   fill_level_grams_blue, fill_level_grams_blue,...      Random Forest              1598.18          1973.10
6   fill_level_grams_green, fill_level_grams_gree...  Linear Regression             60004.15         65893.45
7   fill_level_grams_green, fill_level_grams_gree...  Gradient Boosting             21855.52         33883.83
8   fill_level_grams_green, fill_level_grams_gree...      Random Forest             18068.11         38709.77
9   temperature_red, temperature_blue, temperatur...  Linear Regression             83310.42         83005.42
10  temperature_red, temperature_blue, temperatur...  Gradient Boosting             22618.45        121705.03
11  temperature_red, temperature_blue, temperatur...      Random Forest             12832.02        108534.18
12  fill_level_grams_red, fill_level_grams_blue, ...  Linear Regression                 0.00             0.00
13  fill_level_grams_red, fill_level_grams_blue, ...  Gradient Boosting                59.03           551.46
14  fill_level_grams_red, fill_level_grams_blue, ...      Random Forest                82.53           487.63
15  fill_level_grams_red, temperature_red, fill_l...  Linear Regression                 0.00             0.00
16  fill_level_grams_red, temperature_red, fill_l...  Gradient Boosting                53.49           632.63
17  fill_level_grams_red, temperature_red, fill_l...      Random Forest               225.17          1297.46

Es fällt auf, dass die Mean Squared Error relativ hoch ist, was darauf hindeutet, dass die Modelle nicht optimal trainiert wurden.  Das könnte an unzureichender Merkmalsauswahl oder nicht optimierten Modellen liegen. 

4. Klassifikationsmodell für defekte Flaschen

