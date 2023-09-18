# reads the analogue value from the slider potentiometer connected to the ADC
# on pin 36 marked A0 on the ESP32 CPU board
# The value is used to control the color of the user rgb LED
# Copyright U. Raich 2022
# The program is part of the IoT tutorial during the Africa Internet Summit 2022

from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep_ms
import os

NEOPIXEL_PIN = 21
MAX_INTENSITY = 0x1f
NEOPIXEL_NO_OF_LEDS = 1

# calculate the color from the angle on the color wheel

def colors(pos):
    if pos<60:
        red=MAX_INTENSITY
        green=int(MAX_INTENSITY*pos/60)
        blue=0
    elif pos >=60 and pos < 120:
        red=MAX_INTENSITY-int(MAX_INTENSITY*(pos-60)/60)
        green = MAX_INTENSITY
        blue = 0
    elif pos >=120 and pos < 180:
        red = 0
        blue = int(MAX_INTENSITY*(pos-120)/60)
        green = MAX_INTENSITY
    elif pos >= 180 and pos < 240:
        red = 0
        green = MAX_INTENSITY-int(MAX_INTENSITY*(pos-180)/60)
        blue = MAX_INTENSITY
    elif pos >= 240 and pos < 300:
        red = int(MAX_INTENSITY*(pos-240)/60)
        green = 0
        blue = MAX_INTENSITY
    else:
        red = MAX_INTENSITY
        green = 0
        blue = MAX_INTENSITY - int(MAX_INTENSITY*(pos-300)/60)

    return (red,green,blue)

osVersion=os.uname()

# if there is 'spiram' in the machine name then we are on the T7 V1.4 or V1.5
if osVersion.machine.find('spiram') == -1:
    print("Running on ESP32 WROOM")
    _LED_PIN = 2
else:
    print("Running on an ESP32 WROVER")
    _LED_PIN = 19

neopixel = NeoPixel(Pin(NEOPIXEL_PIN),NEOPIXEL_NO_OF_LEDS)

slider = ADC(Pin(36))  # create ADC object on ADC pin 36
slider.atten(ADC.ATTN_11DB)
old_angle = -1

try:
    while True:
        slider_val = slider.read()
        angle = int(slider_val*360/4095)
        # update only if the pot value has changed
        if angle != old_angle:
            old_angle = angle
            color = colors(angle)
            print("angle: {:d}".format(angle))
            print("color, red: {:d}, green: {:d}, blue: {:d}".format(color[0],color[1],color[2]))
            neopixel[0] = (color[1],color[0],color[2])
            neopixel.write()
        sleep_ms(50)
except KeyboardInterrupt:
    print("Stopping the program and switchin the LED off")
    neopixel[0] = (0,0,0)
    neopixel.write()
