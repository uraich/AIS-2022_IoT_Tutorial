from machine import Pin,PWM
from utime import sleep_ms

led = PWM(Pin(19))
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
