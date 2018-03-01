import numpy

import numpy as np

inFile = "a_example.in"
h = np.genfromtxt(inFile, max_rows=1)
d = np.genfromtxt(inFile, skip_header=1) 

rows_tot = h[0]
cols_tot = h[1]
vehicles = h[2]
rides = h[3]
bonus = h[4]
sim_time = h[5]


class ride:
    def __init__(self, startX, startY, endX, endY, earliestStart, latestFinish):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.earliest_start = earliestStart
        self.latest_finist = latestFinish
        self.done = False

    def vehicle_dist(vehicleX, vehicleY):
        vehicleDist = abs(vehicleX-self.startX) + abs(vehicleY-self.startY)
        return vehicleDist

    def set_as_done():
        self.done = True

    def is_done():
        return self.done

    def vehicle_time(vehicleX, vehicleY):
        # time to reach starting time is equal to distance from starting point
        vehicleDist = abs(vehicleX-self.startX) + abs(vehicleY-self.startY)
        return vehicleDist

rides = []

for i in range(int(rows_tot)):
    r = ride(d[i,0], d[i,1], d[i,2], d[i,3], d[i,4], d[i,5])
    rides.apped(r)
