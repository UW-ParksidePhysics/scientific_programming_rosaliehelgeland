from math import pi

g = 9.81          # m/s^2
p = 1.2           # kg/m^3
a = 0.11          # m
Cd = 0.2
m = 0.43          #kg

Fg = m*g          # N
A = pi*a**2       #m^2


drag_coefficient = Cd 
air_density = p

cross_area_ball = A
ball_mass = m

gravitational_acceleration = g
gravitational_force = Fg

ball_radius = a



soft_kick_velocity = 25./9.  #m/s
hard_kick_velocity = 100./3. #m/s


Fd_soft_kick = (1./2.)*(Cd*p*A*(soft_kick_velocity**2))
Fd_hard_kick = (1./2.)*(Cd*p*A*(hard_kick_velocity**2))



print (f' When the balls velocity is {soft_kick_velocity:.2f} m/s, the drag force of the ball is {Fd_soft_kick:.2f} N. ')
print (f' When the balls velocity is {hard_kick_velocity:.2f} m/s, the drag force of the ball is {Fd_hard_kick:.2f} N. ')
