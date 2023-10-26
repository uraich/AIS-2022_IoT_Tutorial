# esp32_mqtt_pub.py: Reads temperature and humidity from the SHT30 temperature and humidity sensor.
# Uses temperature and humidity readings to calibrate the SGP30 air quality sensor.
# Reads the PM1.0, PM2.5 and PM10 dust concentration from the plantower device.
# Transmits all the readings to the ThingsBoard dash board for display.
# Copyright (c) U. Raich September 2023
# This program has been written for the Seminar on Air Quality and IoT-based Sensor Nov. 2023
# It is released under the MIT license

from umqtt.simple import MQTTClient
from machine import Pin
import network
import time,sys
from wifi_connect import connect
import os
import json
osVersion=os.uname()

# import the SHT3X class
from sht3x import SHT3X,SHT3XError

BROKER="192.168.0.39"
PORT="1885"
ACCESS_TOKEN="jLSpHb7QzZUWyjKkHVtF"
TOPIC="v1/devices/me/telemetry"
RPC_REQUEST="v1/devices/me/rpc/request/+"

def cmdCallback(topic,payload):
    topic_string = topic.decode()
    payload_string = payload.decode()
    print("topic: {:s}, payload: {:s}".format(topic_string, payload_string))
    dict = json.loads(payload)
    # The setValue method
    if dict["method"] == "setValue":
        if dict["params"]:
            userLed.on()
        else:
            userLed.off()
        ledState = userLed.value()
        if ledState:
            ledResponse = "true"
        else:
            ledResponse = "false"
        indicator_topic = "{value:" + ledResponse + "}"
        print("indicator topic: {}".format(indicator_topic))
        c.publish(TOPIC,indicator_topic)
        
# connect to the SHT30
try:
    sht30 = SHT3X()
except SHT3XError as exception:
    if exception.error_code == SHT3XError.BUS_ERROR:
        print("SHT30 module not found on the I2C bus, please connect it")
        sys.exit(-1)
    else:
         raise exception
     
# if there is 'spiram' in the machine name then we are on the T7 V1.4 or V1.5
if osVersion.machine.find('spiram') == -1:
    _LED_PIN = 2
else:
    print("Running on an ESP32 WROVER")
    _LED_PIN = 19

userLed = Pin(_LED_PIN, Pin.OUT)

# connect to WiFi
connect()

print("Connected, starting MQTTClient")
c = MQTTClient("umqtt_client", BROKER,port=PORT,user=ACCESS_TOKEN,password="")

try:
    c.connect()
except:
    print("Cannot connect, please check server IP and username and password")
    sys.exit()

print("Successfully connected to the ThingsBoard MQTT broker")

# subscribe to the switch
c.set_callback(cmdCallback)
c.subscribe(RPC_REQUEST)
print("Waiting for messages on topic 'ThingsBoard' from MQTT broker")

try:
    while True:
        # read temperature and humidity and publish the result
        tempC, humi = sht30.getTempAndHumi(clockStretching=SHT3X.CLOCK_STRETCH,repeatability=SHT3X.REP_S_HIGH)
        PAYLOAD="{" + "temperature: {:8.4f}, humidity: {:8.4f}".format(tempC,humi) + "}"
        print("PAYLOAD SHT30: ",PAYLOAD)
        c.publish(TOPIC,PAYLOAD)
        for i in range(30):
            c.check_msg()
            time.sleep_ms(100)
        
except KeyboardInterrupt:
    c.disconnect()
    print("Stopping data transmission to the ThingsBoard MQTT broker")
