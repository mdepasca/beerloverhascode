import numpy as np

# function to sort rides by:
# 1) starting distance from actual position of the car
# 2) earliest start time - actual car time >= distance
def sort_rides_and_take_first(rides_in, car):

  # rides == list of rides
  # car == macchina con posizione tempo etc
  rides = [r for r in rides_in if r.done == False]

  # 1)
  dist = [np.abs(car.actual_x - r.startX) - np.abs(car.actual_y - r.startY) for r in rides]
  
  # 2)
  delta_time = [r.earliest_start - car.actual_time for r in rides]
  
  # combine 1) and 2)
  cond = [delta_time[i] - dist[i] for i in range(len(rides)) ]
  idx_cond = np.argsort(cond)
  
  id_ride = idx_cond[0]

  return id_ride

