1. MQTT_Client für SPS
    

2. Datenspeicherung und Visualisierung

Zunächst werden die  Daten aus dem Topic iot1/teaching_factory in einer csv. Datei gespeichert. 
Hier werden die Daten  noch nicht sortiert, sondern werden nur nach ihrem Erstellungsdatum sortiert. So können die Daten später flexibler verwendet und sortiert werden. Anschließend wird diese csv. Datei anhand der verschiedenen Kategorie sortiert, um die spätere Visualisierung zu erleichtern. Da während des Speichervorgangs die Verbindung zum Topic abgebrochen ist, werden in der sortierten csv. nur noch die Daten nach dem Verbindungsabbruch gespeichert. Dabei wird der json.Payload in ein Dictionary umgewandelt und in eine Liste von Dictionaries gespeichert. Um den Verlauf der Daten zu verfolgen, werden Zeitreihen der Temperatur pro Dispenser geplottet. 

![Temperatur-Plot](temperature_by_dispenser.png) 

Ausserdem wird der Füllstand der Flaschen geplottet. Alle Nulldaten werden entfernt, da diese nicht für die Visualisierung benötigt werden.

![Füllstand-Plot](filllevel_by_dispenser.png)


3. Regressionsmodell für Endgewicht

Das Regressionsmodell wird verwendet, um das Endgewicht der Flaschen basierend auf dem Füllstand und der Temperatur vorherzusagen. Hierbei werden die Daten aus der sortierten CSV-Datei verwendet, um ein Modell zu trainieren, das die Beziehung zwischen den Eingangsvariablen (Füllstand und Temperatur) und der Zielvariable (Endgewicht) erlernt. Das Modell wird dann evaluiert, um die Genauigkeit der Vorhersagen zu überprüfen.

4. Klassifikationsmodell für defekte Flaschen