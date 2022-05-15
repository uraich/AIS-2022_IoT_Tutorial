from umqtt.simple import MQTTClient
import network
import time
from wifi_connect import *

# Test reception e.g. with:
# mosquitto_sub -t AIS2021

SERVER="192.168.1.36"
TOPIC="AIS2021"
PAYLOAD=b"Welcome to the AIS2021 IoT lecture"

connect()
print("Connected, starting MQTTClient")
c = MQTTClient("umqtt_client", SERVER)
c.connect()
for _ in range(10):
    c.publish(TOPIC,PAYLOAD)
    time.sleep(1)
c.disconnect()
