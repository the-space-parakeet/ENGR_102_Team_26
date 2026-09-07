# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ruby Johnson
#               Iris Hernandez
#               Oliver Brumley
#               John Leach
# Section:      559
# Assignment:   Lab 3 (Team)
# Date:         09/07/2026
#-----------------------------------------------------------#

#-----------------------------------------------------------#
# Description of the Calculations:
#-----------------------------------------------------------#
# Input Variables:
#     - time_1 will be the first time input by user;
#       we will convert it from string to a float.
#     - x_pos_1, y_pos_1, and z_pos_1 will be the x, y, and z
#       positions of the object at the initial time (time 1), 
#       also string to float.
#     - time_2 will be the second time input by user, also 
#       converted string to float.
#     - x_pos_2, y_pos_2, and z_pos_2 will be the x, y, and z 
#       positions of the object at the final time (time 2), 
#       also string to float.
# Calculations Used:
#     - Average velocity formula for linear interpolation is:
#       v_avg = dx/dt.
#     - Linear interpolation formula is:
#       dx = x + v_avg * dt.
#     - Evenly-spaced time step (dt) for interpolation is:
#       time_step = (time_2 - time_1) / 4.
#     - For every step of interpolation, the time will be 
#       incremented by the time step (dt).
#     - For every step of intepolation, the position will be 
#       incremented by the average velocity times the time 
#       step (v_avg * dt).
# Output Variables:
#     - time will represent the current time.
#     - x_pos, y_pos, and z_pos will represent the 
#       current interpolated position coordinates in R3.
#-----------------------------------------------------------#

#-----------------------------------------------------------#
# Sample Calculation: 
#-----------------------------------------------------------#
# time_1 = 1
# x_pos_1 = 1
# y_pos_1 = 1
# z_pos_1 = 1

# time_2 = 2
# x_pos_1 = 2
# y_pos_1 = 2
# z_pos_1 = 2

# avg_velocity_x
#     = (x_pos_2 - x_pos_1) / (time_2 - time_1)
#     = (2 - 1) / (2 - 1)
#     = 1
# avg_velocity_y
#     = (y_pos_2 - y_pos_1) / (time_2 - time_1)
#     = (2 - 1) / (2 - 1)
#     = 1
# avg_velocity_z
#     = (z_pos_2 - z_pos_1) / (time_2 - time_1)
#     = (2 - 1) / (2 - 1)
#     = 1

# time_step 
#     = (time_2 - time_1) / 4
#     = (2 - 1) / 4
#     = 0.25

# zeroth iteration position/time:
#     time = time_1 = 1
#     x_pos = x_pos_1 = 1
#     y_pos = y_pos_1 = 1
#     z_pos = z_pos_1 = 1

# first iteration position/time:
#     time += time_step 
#     time = 1 + 0.25
#     time = 1.25
#     x_pos += avg_velocity_x * time_step
#     x_pos = 1 + (1) * 0.25
#     x_pos = 1.25
#     y_pos += avg_velocity_y * time_step
#     y_pos = 1 + (1) * 0.25
#     y_pos = 1.25
#     z_pos += avg_velocity_z * time_step
#     z_pos = 1 + (1) * 0.25
#     z_pos = 1.25
#
# ... repeat 3 more times!
#-----------------------------------------------------------#

#-----------------------------------------------------------#
# Input position and time data.
#-----------------------------------------------------------#

# Input the time t for the initial datapoint.
time_1 = float(input("Enter time 1: "))

# Input the position <x, y, z> for the initial datapoint.
x_pos_1 = float(input("Enter the x position of the object at time 1: "))
y_pos_1 = float(input("Enter the y position of the object at time 1: "))
z_pos_1 = float(input("Enter the z position of the object at time 1: "))

# Input the time t for the final datapoint.
time_2 = float(input("Enter time 2: "))

# Input the position <x, y, z> for the final datapoint.
x_pos_2 = float(input("Enter the x position of the object at time 2: "))
y_pos_2 = float(input("Enter the y position of the object at time 2: "))
z_pos_2 = float(input("Enter the z position of the object at time 2: "))

print()

#-----------------------------------------------------------#
# Calculate the average velocity over the interval.
#-----------------------------------------------------------#

# Calculate the average velocity for each component 
# <v_x, v_y, v_z> over the time interval [time_1, time_2].
# Use the formula for average velocity:
#       v_avg = delta_pos / delta_time
#       v_avg = (pos_2 - pos_1) / (time_2 - time_1)
# Assume time interval is not zero.
v_x_avg = (x_pos_2 - x_pos_1) / (time_2 - time_1)
v_y_avg = (y_pos_2 - y_pos_1) / (time_2 - time_1)
v_z_avg = (z_pos_2 - z_pos_1) / (time_2 - time_1)

#-----------------------------------------------------------#
# Calculate the time step for interpolation.
#-----------------------------------------------------------#

# Number of points to interpolate over the interval 
# (excluding the given initial and final points).
NUM_INTERPOLATED_POINTS = 3

# Calculate the evenly-spaced time step for interpolation.
time_step = (time_2 - time_1) / (NUM_INTERPOLATED_POINTS + 1)

#-----------------------------------------------------------#
# Interpolate and print the position at each time step.
#-----------------------------------------------------------#

# Variables to store the current time and <z,y,z> position.
# Initialize them to the initial position and time.
time = time_1
x_pos = x_pos_1
y_pos = y_pos_1
z_pos = z_pos_1

# This should be the following loop, but we will manually 
# unroll the loop until we are allowed to use loops:
#-----------------------------------------------------------#
# for i in range(NUM_INTERPOLATED_POINTS + 2):
#     # Print the current time and position values.
#     print(
#         f"At time {time:.2f} seconds the object is at "
#         f"({x_pos:.3f}, {y_pos:.3f}, {z_pos:.3f})"
#     )
#     # Increment the time and position values.
#     time += time_step
#     x_pos += v_x_avg * time_step
#     y_pos += v_y_avg * time_step
#     z_pos += v_z_avg * time_step
#-----------------------------------------------------------#

# Iteration 1: Initial Position
# Print the current time and position values.
print(
    f"At time {time:.2f} seconds the object is at "
    f"({x_pos:.3f}, {y_pos:.3f}, {z_pos:.3f})"
)
# Increment the time and position values.
time += time_step
x_pos += v_x_avg * time_step
y_pos += v_y_avg * time_step
z_pos += v_z_avg * time_step

#-----------------------------------------------------------#

# Iteration 2: Interpolated Position 1
# Print the current time and position values.
print(
    f"At time {time:.2f} seconds the object is at "
    f"({x_pos:.3f}, {y_pos:.3f}, {z_pos:.3f})"
)
# Increment the time and position values.
time += time_step
x_pos += v_x_avg * time_step
y_pos += v_y_avg * time_step
z_pos += v_z_avg * time_step

#-----------------------------------------------------------#

# Iteration 3: Interpolated Position 2
# Print the current time and position values.
print(
    f"At time {time:.2f} seconds the object is at "
    f"({x_pos:.3f}, {y_pos:.3f}, {z_pos:.3f})"
)
# Increment the time and position values.
time += time_step
x_pos += v_x_avg * time_step
y_pos += v_y_avg * time_step
z_pos += v_z_avg * time_step

#-----------------------------------------------------------#

# Iteration 4: Interpolated Position 3
# Print the current time and position values.
print(
    f"At time {time:.2f} seconds the object is at "
    f"({x_pos:.3f}, {y_pos:.3f}, {z_pos:.3f})"
)
# Increment the time and position values.
time += time_step
x_pos += v_x_avg * time_step
y_pos += v_y_avg * time_step
z_pos += v_z_avg * time_step

#-----------------------------------------------------------#

# Iteration 5: Final Position
# Print the current time and position values.
print(
    f"At time {time:.2f} seconds the object is at "
    f"({x_pos:.3f}, {y_pos:.3f}, {z_pos:.3f})"
)
# Increment the time and position values.
time += time_step
x_pos += v_x_avg * time_step
y_pos += v_y_avg * time_step
z_pos += v_z_avg * time_step

#-----------------------------------------------------------#