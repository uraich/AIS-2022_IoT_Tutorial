# ws1812Addresses: controls the ws2812b rgb LED chain
# The program shows the 7 basic colors on seven LEDs of the LED ring
# U. Raich, 19.May 2020
# This program was written for the course on IoT at the University of Cape Coast,Ghana

import machine, neopixel, time

n=7        # number of LEDs
intensity = 0x02

print("Testing the ws2812 rgb LED")
print("The program shows the 7 basic colors on seven LEDs of the LED ring")
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

neoPixel[0] = (intensity,intensity,intensity)   # white on the middle LED
# colors are:
# LED color
#  1   red
#  2   green
#  3   yellow
#  4   blue
#  5   magenta
#  6   cyan

for color in range(1,n,1):
    if color & 1:
        red = intensity
    else:
        red = 0
        
    if color & 2:
        green = intensity
    else:
        green = 0
        
    if color & 4:
        blue = intensity
    else:
        blue = 0        
    neoPixel[color] = (red,green,blue)
    
neoPixel.write()
time.sleep(5)
clearChain()
        

