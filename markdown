1. MQTT_Client für SPS

Der MQTT_Client verbindet sich mit einem MQTT-Broker und sendet Daten an ein Topic sendet. Der Client sendet periodisch Füllstandsdaten für eine Flasche, die zufällig generiert werden.  Der Client bleibt aktiv, bis er manuell beendet wird.    

2. Datenspeicherung und Visualisierung

Zunächst werden die  Daten aus dem Topic iot1/teaching_factory in einer csv. Datei gespeichert. 
Hier werden die Daten  noch nicht sortiert, sondern werden nur nach ihrem Erstellungsdatum sortiert. Diese Speicherung ermöglicht eine spätere flexible Sortierung und Verarbeitung der Daten. Anschließend wird diese csv. Datei anhand der verschiedenen Kategorie sortiert, um die Visualisierung und Analsyse der Daten zu erleichtern. Da während des Speichervorgangs die Verbindung zum Topic abgebrochen ist, werden in der sortierten csv. nur noch die Daten nach dem Wiederaufbau der Verbindung gespeichert. Dabei wird der .json Payload in ein Dictionary umgewandelt und in eine Liste von Dictionaries gespeichert. 

Um den Verlauf der Daten zu verfolgen, werden Zeitreihen der Temperatur pro Dispenser geplottet. 

![Temperatur-Plot](temperature_by_dispenser.png) 

Ausserdem wird der Füllstand der Flaschen geplottet. 

![Füllstand-Plot](filllevel_by_dispenser.png)


3. Regressionsmodell für Endgewicht

Das Regressionsmodell wird verwendet, um das Endgewicht der Flaschen basierend auf dem Füllstand und der Temperatur vorherzusagen. Das Endgewicht wird als Summe der Füllstände der drei Flaschen berechnet. Das Modell verwendet verschiedene Kombinationen von Füllstand- und Temperaturdaten, um die beste Vorhersagegenauigkeit zu erreichen. Zudem werden verschiedene Regressionsmodelle wie Lineare Regression, Gradient Boosting und Random Forest verwendet. Die Modelle werden auf den skalierten Daten trainiert und die Mean Squared Error (MSE) Werte für Training und Test werden berechnet, um die Leistung der Modelle zu bewerten. Je kürzer der MSE-Wert, desto besser ist die Vorhersage des Modells. Der Random Forrest erstellt viele Entscheidungsbäume mit zufällig ausgewählten Daten und Merkmalen. Die Vorhersagen der Bäume werden aggregiert (bei Regression der Durchschnitt), um genauere Ergebnisse zu erzielen und Überanpassung zu vermeiden. Der Gradient Boosting Algorithmus erstellt sequentiell Entscheidungsbäume, wobei jeder Baum die Fehler des vorherigen Baums korrigiert. Dadurch wird die Genauigkeit der Vorhersage verbessert. 
Die Mean Squard Erros sind verhältnismäßig hoch, die absoluten Fahler hingen relativ gering. Das kann darauf hindeuten, dass das Modell in den meisten Fällen gut vorhersagt, aber gelegentlich große Fehler bei einzelnen Datenpunkten macht. Der MSE ist empfindlicher gegenüber großen Fehlern, da er diese quadriert, wodurch einzelne Ausreißer den MSE stark beeinflussen. Der absolute Fehler gibt die absolute Abweichung an und ist weniger von Ausreißern betroffen. Eine Datenanalyse hilft, diese Ausreißer zu identifizieren und ggf. das Modell anzupassen.
