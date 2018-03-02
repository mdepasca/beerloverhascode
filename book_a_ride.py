import numpy as np
import os

# ==============================================================================
# ride class
class ride:
    # a: startX; b: startY; x: endX; y: endY:, s: earliestStart; f: latestFinish
    def __init__(self, Id, a, b, x, y, s, f):
        self.Id = Id
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.done = False # False: not done; True: done

    def set_as_done(self):
        self.done = True

# ==============================================================================
# car class
class car:
    def __init__(self):
        self.actual_x = 0
        self.actual_y = 0
        self.actual_time = 0
        self.points = 0
        self.rides = []

    def give_me_a_ride_object(self, ride, B):
        # time taken by the car to go to the starting point of the ride
        d_from_actual_to_start = np.abs(ride.a-self.actual_x) + np.abs(ride.b-self.actual_y)

        # the internal time of the car is updated to take into account the travel time
        self.actual_time += d_from_actual_to_start

        #time/distance of the ride
        d_from_start_to_end = np.abs(ride.a-ride.x) + np.abs(ride.b-ride.y)

        if self.actual_time  == ride.s:
            self.points += d_from_start_to_end
        # the car has arrived to the starting point, but it is still to early to start the ride
        if ride.s > self.actual_time:
            # move the time of the car to the starting time of the ride
            self.actual_time = ride.s


        # update the position and time of the car to
        self.actual_x = ride.x
        self.actual_y = ride.y

        self.actual_time += d_from_start_to_end

        if self.actual_time < ride.f:
            self.points += (ride.f  - self.actual_time)*B

        self.rides.append(ride.Id)

    	return

# # ==============================================================================
# # function to sort rides by:
# # 1) starting distance from actual position of the car
# # 2) earliest start time - actual car time >= distance
# def sort_rides_and_take_first_v1(rides_in, car_in):
#
#     # rides == list of rides
#     # car == macchina con posizione tempo etc
#     rides = [r for r in rides_in if r.done == False]
#
#     nrides = len(rides)
#
#     # by default id_ride is None
#     id_ride = None
#
#     if(nrides > 0):
#
#         idr = np.arange(0, nrides)
#         # 1)
#         dist = [np.abs(car_in.actual_x - r.a) + np.abs(car_in.actual_y - r.b) for r in rides]
#         print 'DISTANCE CAR FROM RIDES: ', dist
#
#         # 2)
#         delta_time = [r.s - car_in.actual_time for r in rides]
#         print 'TIME CAR FROM RIDES: ', delta_time
#
#         # combine 1) and 2)
#         cond = [delta_time[i] - dist[i] for i in range(nrides)]
#         print 'TIME - DISTANCE CAR FROM RIDES: ', cond
#         # cond must be >= 0
#         ge0 = [c >= 0 for c in cond]
#         if(int(np.sum(ge0)) > 0):
#             # print '>= 0: ', ge0
#             idge0 = idr[ge0]
#             # print 'id(>=0) = ', idge0
#
#             idx = np.argmin(np.array(cond)[ge0])
#             # print 'idx = ', idx
#             id_ride = rides[idge0[idx]].Id
#             print 'BEST RIDE TO PICK: ', id_ride
#
#     return id_ride

def sort_rides_and_take_first_v2(rides_in, car_in, B):

    rides = [r for r in rides_in if r.done == False and car_in.actual_time < r.f]

    nrides = len(rides)

    # by default id_ride is None
    id_ride = None

    if(nrides > 0):
        # compute actual time - earliest start, sort and keep only >= 0
        dts = np.array([np.abs(car_in.actual_time - r.s) for r in rides]).astype(int)
        # print 'dts: ', dts

        # compute distance car and starting point of rides
        d_car_ride = np.array([np.abs(car_in.actual_x-r.a)+np.abs(car_in.actual_y-r.b) for r in rides]).astype(int)
        # print 'd_car_ride: ', d_car_ride
        # 1 - TEST ** BEST **
        time_dist = dts + d_car_ride
        # print 'time_dist: ', time_dist
        id_idr1 = np.argmin(time_dist)

        # 2 - TEST ** WORST **
        # d_ride = np.array([np.abs(r.x-r.a)+np.abs(r.y-r.b) for r in rides]).astype(int)
        # dft = np.array([r.f-car_in.actual_time for r in rides]).astype(int)
        # id_idr1 = np.argmax(dft - (d_car_ride+d_ride))


        id_ride = rides[id_idr1].Id
        # print '**id_ride = ', id_ride

    return id_ride

# ==============================================================================
def book_rides_one_input(inFolder, inFile, outFile):

    # header: first line of input file:
    # 0 R: rows;
    # 1 C: cols;
    # 2 F: number of vehicles per fleet;
    # 3 N: number of rides;
    # 4 B: bonus per ride;
    # 5 T: number of steps in the simulation
    h = np.genfromtxt(os.path.join(inFolder, inFile), max_rows=1)
    R = int(h[0])
    C = int(h[1])
    F = int(h[2])
    N = int(h[3])
    B = int(h[4])
    T = int(h[5])
    # data: input files with each row as a ride and cols:
    # 0: a; 1: b; 2: x; 3: y; 4: s; 5: f
    inRides = np.genfromtxt(os.path.join(inFolder, inFile), skip_header=1)

    print 'READ INPUTFILE: %s' %(os.path.join(inFolder, inFile))

    # init rides
    rides = [ride(i,
            inRides[i,0], inRides[i,1], # a b
            inRides[i,2], inRides[i,3], # x y
            inRides[i,4], inRides[i,5]  # s f
            ) for i in range(0, N)]
    print 'INIT ALL AVAILABLE RIDES'
    n_rides_left = N

    # init cars
    cars = [car() for i in range(0, F)]
    print 'TURN ON ALL THE CARS'

    print 'OPEN OUTPUT FILE: %s' %(os.path.join(inFolder, outFile))
    out = open(os.path.join(inFolder, outFile), 'w')

    cntcar = 0
    for icars in cars:
        print 'CAR ID %d GO (actual_time = %d)' %(cntcar, icars.actual_time)
        write_rides_per_car = ""
        rides_per_car = []

        # for irides in rides:
        while True:
            # check if car reach the end of allowed simulation time T
            if(icars.actual_time < T-1):
                # id_ride = sort_rides_and_take_first_v1(rides, icars)
                id_ride = sort_rides_and_take_first_v2(rides, icars, B)
                if(id_ride is None):
                    break
                if(icars.actual_time < rides[id_ride].f):
                    icars.give_me_a_ride_object(rides[id_ride], B)
                    rides_per_car.append(id_ride)
                    rides[id_ride].set_as_done()
                    n_rides_left -= 1
                    write_rides_per_car = "%s %d" %(write_rides_per_car, id_ride)
            else:
                break
            # print 'Updated actual_time: %d' %(icars.actual_time)

        write_rides_per_car = '%d %s' %(len(rides_per_car), write_rides_per_car)
        # print into file the rides of each car
        out.write(write_rides_per_car + '\n')
        print 'CAR ID %d ==> POINTS: %d\n' %(cntcar, icars.points)
        cntcar += 1
        if(n_rides_left == 0):
            print 'NO RIDES LEFT ... CLOSE'
            break

    out.close()
    print 'DONE'


    return

# ==============================================================================
# MAIN
# ==============================================================================
# input folder with input files
inFolder = os.path.abspath('../')
# names of the input files
inFiles = 'a_example.in b_should_be_easy.in c_no_hurry.in d_metropolis.in e_high_bonus.in'.split()
# autocreate names of output files
outFiles = [f.replace('.in', '.out') for f in inFiles]

# FILE 1
# book_rides_one_input(inFolder, inFiles[0], outFiles[0])

# TEST 2
# book_rides_one_input(inFolder, inFiles[1], outFiles[1])

# FILE 3
# book_rides_one_input(inFolder, inFiles[2], outFiles[2])

# FILE 4
# book_rides_one_input(inFolder, inFiles[3], outFiles[3])

# FILE 5
# book_rides_one_input(inFolder, inFiles[4], outFiles[4])

nfiles = len(inFiles)
for ifile in range(0, nfiles):
    book_rides_one_input(inFolder, inFiles[ifile], outFiles[ifile])
