#!/usr/bin/python3
import time
import os
import sys

from plant_monitor import PlantMonitor
pm = PlantMonitor()

filename = "~/data/" + sys.argv[1]

if not os.path.exists(file_path):
    with open(filename, 'w') as fp:
        f.write("time,water level(%),temp(°C),humidity(%)\n")

f = open(filename, "w")

t = time.strftime("%H:%M:%S", time.localtime())

f.write(t + "," + str(pm.get_wetness()) + "," + str(pm.get_temp()) + "," + str(pm.get_humidity()))
