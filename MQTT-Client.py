import paho.mqtt.client as mqtt
import time 
broker = "158.180.44.197"
port = 1883
topic = "at/house/bulb1"
payload = "on"
gruppe = "MCI_Students"
namen = "Steiniger, Muther, Wolf"

# create function for callback
def on_publish(client, userdata, flags, reasonCode, properties):
    print("data published \n")  

# create client object
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set("bobm", "letmein")              

# assign function to callback
mqttc.on_publish = on_publish                           

# establish connection
mqttc.connect(broker,port)     

mqttc.publish(f"aut/{gruppe}/$groupsname", gruppe, retain=True)
mqttc.publish(f"aut/{gruppe}/names", namen, retain=True)

return_code = mqttc.publish(topic, payload)
return_code = mqttc.publish(f"aut/{gruppe}/$groupsname", gruppe, retain=True)
return_code = mqttc.publish(f"aut/{gruppe}/names", namen, retain=True)

mqttc.disconnect()
