# ws1812Addresses: controls the ws2812b rgb LED chain
# Switches all LEDs in the ring off
# U. Raich, 19.May 2020
# This program was written for the course on IoT at the University of Cape Coast,Ghana

import machine, neopixel, time

n=7        # number of LEDs

print("Testing the ws2812 rgb LED")
print("The program switches all seven LEDs of the LED ring off")
print("Program written for the course on IoT at the")
print("University of Cape Coast,Ghana")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

def clearChain():
    for i in range(n):
        neoPixel[i] = (0, 0, 0)
    neoPixel.write()

        
pin = 26   # connected to GPIO 21 on esp32
    
neoPixel = neopixel.NeoPixel(machine.Pin(pin), n)

clearChain()
        

