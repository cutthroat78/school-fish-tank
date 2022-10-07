#!/usr/bin/python3
import time
import os
import sys

from plant_monitor import PlantMonitor
pm = PlantMonitor()

filename = "/home/pi/data/" + sys.argv[1]

f = open(filename, "w")

if os.stat(filename).st_size == 0:
    f.write("time,water level(%),temp(°C),humidity(%)\n")

t = time.strftime("%H:%M:%S", time.localtime())

f.write(t + "," + str(pm.get_wetness()) + "," + str(pm.get_temp()) + "," + str(pm.get_humidity()))
