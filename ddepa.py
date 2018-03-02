import numpy as np
import macchina as mc
import sbuffo as sb

inFile = "a_example.in"
outFile = inFile.replace('.in', '.out')
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
    r = ride(i, int(d[i,0]), int(d[i,1]), int(d[i,2]), int(d[i,3]), int(d[i,4]), int(d[i,5]))
    rides.append(r)
    
cars = [mc.Macchina() for iv in range(0, vehicles)]


out = open(outFile, 'w')
for icars in cars:
  rides_per_car = []
  line = ""
  
  for irides in rides:
    if(icars.actual_time < sim_time):
      id_ride = sb.sort_rides_and_take_first(rides, icars)
      rides_per_car.append(id_ride)
      line = "%s %d" %(line, id_ride)
      icars.give_me_a_ride_object(rides[id_ride])
      rides[id_ride].set_as_done()
      
  out.write(line + "\n")
    

