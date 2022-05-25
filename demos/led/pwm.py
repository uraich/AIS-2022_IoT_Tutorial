from machine import Pin,PWM
from utime import sleep_ms
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

try:
    while True:
        for i in range(1024):
            led.duty(i)
            sleep_ms(1)
        for i in range(1023,-1,-1):
            led.duty(i)
            sleep_ms(1)
except KeyboardInterrupt:
    led.deinit()
