# formula for trajectory of ball: f(x) = x * tan(theta) - (1/(2 * v_0**2))*((g * x**2)/(2 * cos**2(theta)) + y_0)
# x: coordinate along the ground
# g: acceleration due to gravity near the large body [eg. Earth]
# v_0 is the value of the initial velocity 
#  initial velocity makes an angle (theta) with the x axis
# initial position of the ball: (0, y_0)
# first read input data y_0, theta, and v_0 from the command line
# plot the trajectory y = f(x) for y >= 0.

import numpy as np
from matplotlib.pylab import tan, cos
import matplotlib.pyplot as plt
import sys

sys.argv = ['plot_trajectory', 15, 5, 10]

# create function

def ball_trajectory(v_0, y_0, theta, g, x):
    return y_0 + x * tan(theta) - ((g * x**2)/(2 * v_0**2 * cos(theta)**2))


# pull variables from command line 

try: 
    
    initial_velocity = float(sys.argv[1])

    initial_y_value = float(sys.argv[2])

    theta = float(sys.argv[3])
    
except IndexError:
    print(f'initial velocity, initial position and theta value needed on command line!')
    sys.exit(1)



# define constants

gravitational_acceleration_Earth = 9.81 #m/s

if __name__ == '__main__':
    
    v_0 = initial_velocity
    
    y_0 = initial_y_value
    
    test_theta = np.deg2rad(theta)
    
    coordinates_along_ground = np.linspace(0, 100, 50)
    trajectories = ball_trajectory(v_0, y_0, test_theta, gravitational_acceleration_Earth, coordinates_along_ground)

    plt.plot(coordinates_along_ground, trajectories)
    plt.xlabel('position coordinates')
    plt.ylabel('trajectory')
    plt.show()