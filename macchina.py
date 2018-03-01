class Macchina:
	self.actual_x = 0
	self.actual_y = 0
	self.actual_time = 0
    self.points = 0
    self.rides = []

    def give_me_a_ride_object(self, ride):
        a = ride.a
        b = ride.b
        x = ride.x
        y = ride.y
        s = ride.s
        f = ride.f
        i = ride.id
        self.give_me_a_ride_values(a, b, x, y, s, f, i)

    def give_me_a_ride_values(self, ride_a, ride_b, ride_x, ride_y, ride_s, ride_f, ride_i):
        # time taken by the car to go to the starting point of the ride
        d_from_actual_to_start = np.abs(ride_a-self.actual_x) + np.abs(ride_b-self.actual_y)

        # the internal time of the car is updated to take into account the travel time
        self.actual_time += d_from_actual_to_start

        #time/distance of the ride
        d_from_start_to_end = np.abs(ride_a-ride_x) + np.abs(ride_b-ride_y)

        if self.actual_time  == ride_s
            self.points += d_from_start_to_end
        # the car has arrived to the starting point, but it is still to early to start the ride
        if ride_s > self.actual_time:
            # move the time of the car to the starting time of the ride
            self.actual_time = ride_s


        # update the position and time of the car to
        self.actual_x = ride_x
        self.actual_y = ride_y




        self.actual_time += d_from_start_to_end

        if self.actual_time < self.f:
            self.points += (self.f  - self.actual_time)


        self.rides.append(i)
    	return
