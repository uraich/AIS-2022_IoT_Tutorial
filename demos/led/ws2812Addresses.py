# ws1812Addresses: controls the ws2812b rgb LED chain
# The program switches on a single led at a time in red color and it prints the corresponding led address
# U. Raich, 19.May 2020
# This program was written for the course on IoT at the University of Cape Coast,Ghana

import machine, neopixel, time

n=7        # number of LEDs

print("Testing the ws2812 rgb LED")
print("The program switches leds on consecutively, allowing to figure out which LED corresponds to which address")
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
    
for i in range(n):
    print("LED address: ",i)
    neoPixel[i] = (0,0,0x1f)
    neoPixel.write()
    time.sleep(1)
    clearChain()
        
clearChain()

