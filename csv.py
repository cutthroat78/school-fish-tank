#!/usr/bin/python3
import time
import os
import sys

from plant_monitor import PlantMonitor
pm = PlantMonitor()

filename = "/home/pi/data/" + sys.argv[1]

if os.path.exists(filename) = False:
    f = open(filename, "w")
    f.write("time,water level(%),temp(°C),humidity(%)\n")
    f.close()

f = open(filename, "a")

t = time.strftime("%H:%M", time.localtime())

f.write(t + "," + str(pm.get_wetness()) + "," + str(pm.get_temp()) + "," + str(pm.get_humidity()))

f.close()
