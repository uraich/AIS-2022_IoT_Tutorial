# reads the analogue value from the slider potentiometer connected to the ADC
# on pin 36 marked A0 on the ESP32 CPU board
# The value is used to control the brightness of the user LED
# Copyright U. Raich 2022
# The program is part of the IoT tutorial during the Africa Internet Summit 2022

from machine import Pin, PWM, ADC
from time import sleep_ms
import os
osVersion=os.uname()

# if there is 'spiram' in the machine name then we are on the T7 V1.4 or V1.5
if osVersion.machine.find('spiram') == -1:
    print("Running on ESP32 WROOM")
    _LED_PIN = 2
else:
    print("Running on an ESP32 WROVER")
    _LED_PIN = 19
    
led = PWM(Pin(_LED_PIN),Pin.OUT)
led.freq(1000)

slider = ADC(Pin(36))  # create ADC object on ADC pin 36
slider.atten(ADC.ATTN_11DB)

while True:
    slider_val = slider.read()
    led.duty(slider_val//4)
    sleep_ms(50)
