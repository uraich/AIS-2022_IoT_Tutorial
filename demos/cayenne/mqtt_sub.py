from machine import Pin
from umqtt.simple import MQTTClient
import network
import time
from wifi_connect import *

# Test publication e.g. with:
# mosquitto_pub -t AIS2021 -m "LED on"

SERVER="192.168.1.36"
TOPIC="AIS2021"

def cmdCallback(topic,payload):
    print(topic,payload)
    if payload == b"LED on":
        userLed.on()
    elif payload == b"LED off":
        userLed.off()    

userLed = Pin(19,Pin.OUT)
connect()

print("Connected, starting MQTTClient")
c = MQTTClient("umqtt_client", SERVER)
c.connect()

c.set_callback(cmdCallback)
c.subscribe(TOPIC)

print("Waiting for messages on topic 'AIS2021' from MQTT broker")
while True:
    c.wait_msg()
