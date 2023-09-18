# clearPixel.py: switches the ws2812 LED off
# U. Raich, 13. September 2023
# This program was written for the course on IoT at the University of Cape Coast,Ghana

import machine, neopixel, time

n=1        # number of LEDs

print("Testing the ws2812 rgb LED")
print("The program switches the ws2812 LED off")
print("Program written for the course on IoT at the")
print("University of Cape Coast,Ghana")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

def clearChain():
    neoPixel[0] = (0, 0, 0)
    neoPixel.write()

        
pin = 21   # connected to GPIO 21 on esp32
    
neoPixel = neopixel.NeoPixel(machine.Pin(pin), n)

clearChain()
        

