# AIS-2022_IoT_Tutorial
## Everything that is needed to re-create the IoT system, shown during the AIS-2022 tutorial on IoT
This repository contains everything that is needed to recreate the IoT system demonstrated during the 2022 session of the African Internet Summit.
The following hardware is required: (cost ~ 25 Euros)
* WeMos D1 mini ESP32 CPU card, e.g. LoLin T7 V1.5
* WeMos D1 mini Triple base: This is a bus card with 3 slots for WeMos D1 mini shields
* SHT30 shield (I2C Temperature and Humidity Sensor)
* LoLin RGB LED with 7 WS28212 addressable RGD LEDs
* a 10 kOhms potentiometer
* a micro USB cable for flashing and for communication between the ESP32 and a PC

The repository contains:
* The slides presented during the IoT tutorial
* A binary version of the MicroPython Interpreter that can be flashed onto the ESP32 CPU
* Bash scripts erase the ESP32 flash and to write the ESP32 flash with the MicroPython Interpreter
* The source code of the SHT30 driver. The driver is already included in the MicroPython interpreter and can be used directly. The sources
are provided for reference only.
* All demo programs.
