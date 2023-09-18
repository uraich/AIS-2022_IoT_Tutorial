# ws1812.py: shows all the basic colors on the LED
# U. Raich, 13. September 2023
# This program was written for the course on IoT at the University of Cape Coast,Ghana

import machine, neopixel, time

n=1
intensity = 0x1f

print("Testing the ws2812 rgb LED")
print("Switches the LED to red for 1 s and switches it off again")
print("Program written for the course on IoT at the")
print("University of Cape Coast,Ghana")
print("Copyright: U.Raich")
print("Released under the Gnu Public License")

def clearPixel():
    neoPixel[0] = (0,0,0)
    neoPixel.write()

pin = machine.Pin(21) # connected to D2, which corresponds to GPIO 21

neoPixel = neopixel.NeoPixel(machine.Pin(pin), n)

for color in range(1,7,1):
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
        
    neoPixel[0] = (green,red,blue)
    neoPixel.write()
    time.sleep(2)
    
clearPixel()

