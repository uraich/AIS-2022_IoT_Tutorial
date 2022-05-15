# sine.py: calulates the sine function and prints 30 values
#          The program demonstrates the plot function of thonny
# Copyright (c) U. Raich 4.5.2022
# This program is part of the demos for the IoT tutorial given at
# the African Internet Summit 2022, Mauritius

import math
no_of_points = 30
for i in range(no_of_points):
    print(math.sin(2*math.pi*i/no_of_points)+1) 
          
