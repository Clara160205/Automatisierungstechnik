import paho.mqtt.client as mqtt
import time 
import random

broker = "158.180.44.197"
port = 1883
topic = "at/house/bulb1"
#payload = "on"
gruppe = "MCI_Students"
namen = "Steiniger, Muther, Wolf"


def random_fill_level():
    return random.uniform(0, 100)

def on_publish(client, userdata, flags, reasonCode, properties):
    print("data published \n")  

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set("bobm", "letmein")              

mqttc.on_publish = on_publish                           


mqttc.connect(broker,port)     

mqttc.publish(f"aut/{gruppe}/$groupsname", gruppe, retain=True)
mqttc.publish(f"aut/{gruppe}/names", namen, retain=True)

try:
    while True:
        
        fill_level = random_fill_level()
        mqttc.publish(f"aut/{gruppe}/fill_level", fill_level, retain=True)
        time.sleep(10)

except KeyboardInterrupt:
    print("Program terminated.")


mqttc.disconnect()
