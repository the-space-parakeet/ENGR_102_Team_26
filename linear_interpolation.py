# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ruby Johnson
#               Iris Hernandez
#               Oliver Brumley
#               John Leach
# Section:      559
# Assignment:   Lab 2.1 (Team)
# Date:         09/03/2026
#-----------------------------------------------------------#

# Import pi so we can calculate the ISS orbit's circumference.
from math import pi

#-----------------------------------------------------------#
# PART 1: Linear Interpolation
#   This program estimates the distance between the ISS and 
#   Houston, given measured distance at two points in time. 
#   It calculates the average speed of the ISS between the 
#   two points, and estimates its position at intermediate 
#   points by assuming a constant speed.
#-----------------------------------------------------------#

# Define given measurements.
time_0 = 10.0                                               # Initial time measurement (minutes)
time_1 = 55.0                                               # Final time measurement (minutes)

distance_0 = 2030.0                                         # Initial distance measurement (km)
distance_1 = 23030.0                                        # Final distance measurement (km)

time_test = 25.0                                            # Time for test case (minutes)

# Calculate station speed using s = (d1 - d0) / (t1 - t0).
speed = (distance_1 - distance_0) / (time_1 - time_0)       # Average station speed (km/min)

# Calculate linear estimate of ISS distance from Houston at 
# time t using d = d0 + st (Given: t0 < t < t1).
distance_from_houston = (                                   # Estimated distance from Houston (km)
    distance_0 + 
    (speed * (time_test - time_0))
)

# Print output, giving position of the ISS relative to 
# Houston at some time between 10 and 55 minutes.
print(f"Part 1:")
print(f"For t = {time_test} minutes, the position p = {distance_from_houston:.1f} kilometers")

#-----------------------------------------------------------#
# PART 2: Linear Extrapolation With Modulo
#   This program extends the linear estimate, assuming a 
#   constant velocity for the ISS, to times beyond the second 
#   measurement. For large time values, this estimate may be 
#   very inaccurate. The circular orbit of the ISS is 
#   accounted for by resetting the distance from Houston to 
#   zero after each full orbit is completed.
#-----------------------------------------------------------#

# Define given measurements.
orbit_radius = 6745.0                                       # Radius of the ISS orbit around Earth (km)

time_test = 300.0                                           # Time for test case (minutes)

# Calculate total distance for one ISS orbit using 
# circumference formula c = 2πr.
orbit_circumference = 2.0 * pi * orbit_radius               # Circumference of the ISS orbit (km)

# Calculate linear estimate of total distance traveled by 
# the ISS at time t using d = d0 + st (Given: 0 < t < inf).
total_distance_traveled = (                                 # Estimated distance the ISS traveled (km)
    distance_0 + 
    speed * (time_test - time_0)
)

# Distance from Houston resets every orbit. Calculate the
# distance from Houston using total distance (mod) the 
# distance in one full orbit.
distance_from_houston = (                                   # Estimated distance from Houston (km)
    total_distance_traveled % orbit_circumference
)

# Print output, roughly estimating the position of the ISS 
# relative to Houston at any time.
print(f"Part 2:")
print(f"For t = {time_test} minutes, the position p = {distance_from_houston} kilometers")
