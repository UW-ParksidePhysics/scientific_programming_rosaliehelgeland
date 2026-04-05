# visualize trajectory of a ball as an animation 
# time starts at zero, end at the ground 
#    * x(t) = v_0 * t*cos(theta)
#    * y(t) = v_0 * t*sin(theta) - 0.5 * g * t**2
# simulate values of y_0, v_0, and theta simultaneously 
# input y_0, v_0, and theta in an array titled initial_conditions
# color each curve differently, label them each in legend
# assume y = 0 is the ground, do not plot any trajectories below 0.
# use time of flight t_f to limit each trajectory in time 
#    * t_f = (2 * v_0 * sin(theta)/g)
# mark the maximum height of each directory with a dashed horizontal line the same color of the curves 
#    * use PyPlot axhline() function
#    * h = (v_0**2 * sin(theta)**2)/(2 * g)

import numpy as np
import matplotlib.pyplot as plt


trajectories = []

g = 9.81 #m/s

initial_conditions = [
    [0, 50, 30],
    [0, 60, 40],
    [0, 30, 50]
    ]


def time_of_flight(v_0, theta, g):
    return (2 * v_0 * np.sin(theta))/g

def x_values(v_0, t, theta):
    return v_0 * t*np.cos(theta)

def y_values(v_0, t, theta, g):
    return v_0 * t * np.sin(theta) - 0.5 * g * t**2



#computing trajectories

for y_0, v_0, deg_theta in initial_conditions:
    
    theta = np.deg2rad(deg_theta) 
    
    t_f = time_of_flight(v_0, theta, g)
    
    t = np.linspace(0, t_f, 100)
    
    x = x_values(v_0, t, theta)
    
    y = y_values(v_0, t, theta, g)
    
    
    trajectories.append((x, y, v_0, theta, deg_theta))
    
def max_height(v_0, theta, g):
    return (v_0**2 * np.sin(theta)**2)/(2 * g)



plt.ion()
figure, axis = plt.subplots()

colors = ['g', 'r', 'b']


#maximums 

x_max = max([max(x) for x,_,_,_,_ in trajectories])
y_max = max([max(y) for _,y,_,_,_ in trajectories])


for frame in range(1, 100):
    
    axis.clear()
    
    
    for i, (x, y, v_0, theta, deg_theta) in enumerate(trajectories):
        
        axis.plot(x[:frame], y[:frame],colors[i], 
             label = f"v = {v_0}, theta = {deg_theta}")
        
        h = max_height(v_0, theta, g)
        axis.axhline(h, linestyle='--', color = colors[i])
        
    
    axis.set_xlim(0, x_max)
    axis.set_ylim(0, y_max)
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.legend()
    
    plt.pause(0.05)
    
plt.ioff()
plt.show()