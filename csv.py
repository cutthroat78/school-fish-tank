#!/usr/bin/python3
import time
import os

from plant_monitor import PlantMonitor
pm = PlantMonitor()

filename = "~/data/" + sys.argv[1]

f = open(filename, "w")

t = time.strftime("%H:%M:%S", time.localtime())

if os.stat(filename).st_size == 0:
    f.write("time,water level(%),temp(°C),humidity(%)\n")

f.write(t + "," + str(pm.get_wetness()) + "," + str(pm.get_temp()) + "," + str(pm.get_humidity()))
