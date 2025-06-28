import paho.mqtt.client as mqtt
import requests
import csv
import os
import time
from datetime import datetime

my_data = {
    "contact": {
        "id": "1",
        "firstName": "Günther",
        "secondName": "Andre",
        "thirdName": "Clara",
        "group": "gruppeA"
    }
}

broker = "158.180.44.197"
port = 1883
topic_sub = "iot1/teaching_factory/#"
csv_file = "mqtt_data.csv"


names = f"{my_data['contact']['firstName']}_{my_data['contact']['secondName']}_{my_data['contact']['thirdName']}".replace(" ", "_")
topic_pub = f"MC1Student/Namen/{names}"
payload = '{"status": "on", "group": "gruppeA"}'

# CSV vorbereiten
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "payload"])

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    client.subscribe(topic_sub)

def on_message(client, userdata, msg):
    ts = datetime.now().isoformat()
    with open(csv_file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([ts, msg.payload.decode()])
    print(f"[{ts}] {msg.topic}: {msg.payload.decode()}")

def on_publish(client, userdata, flags, reasonCode, properties):
    print("Data published to:", topic_pub)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set("bobm", "letmein")
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.connect(broker, port)

mqttc.publish(topic_pub, payload)

mqttc.loop_start()
print("Beginne Datenerfassung für 15 Minuten...")
time.sleep(3 * 60)
mqttc.loop_stop()
mqttc.disconnect()
print("Beendet.")
