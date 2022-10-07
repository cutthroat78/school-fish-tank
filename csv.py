#!/usr/bin/python3
import time
import os
import sys

from plant_monitor import PlantMonitor
pm = PlantMonitor()

filename = "/home/pi/data/" + sys.argv[1]

f = open(filename, "w")

try:
    with open(filename, 'x') as fp:
        fp.write("time,water level(%),temp(°C),humidity(%)\n")
except:
    print('File already exists')

t = time.strftime("%H:%M:%S", time.localtime())

f.write(t + "," + str(pm.get_wetness()) + "," + str(pm.get_temp()) + "," + str(pm.get_humidity()))
