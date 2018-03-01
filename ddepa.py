import numpy

import numpy as np

inFile = "a_example.in"
h = np.genfromtxt(inFile, max_rows=1)
d = np.genfromtxt(inFile, skip_header=1) 

rows_tot = int(h[0])
cols_tot = int(h[1])
vehicles = int(h[2])
rides = int(h[3])
bonus = int(h[4])
sim_time = int(h[5])


class ride:
    def __init__(self, Id, startX, startY, endX, endY, earliestStart, latestFinish):
        self.Id=Id
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
    r = ride(i, int([i,0]), int([i,1]), int([i,2]), int([i,3]), int([i,4]), int([i,5]))
    rides.apped(r)
