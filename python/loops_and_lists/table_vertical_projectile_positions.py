#table of t and y(t)
#
# y(t) = v0*t - (1/2)*g*t^2
#
#n + 1 uniformly spaced t values 
#interval [0, 2*v0/g]


#pick two solid objects
solid_objects = ['Earth', 'Moon']
gravitational_accelerations = [9.81, 1.63] #m/s/s

#pick positive initial velocity
initial_velocity = 5. #m/s

#number of intervals
number_of_times = 9

#print the table
print (f'For initial velocity of {initial_velocity:.2f} m/s')
print(58*'-')

print (f' {solid_objects[0]} g = {gravitational_accelerations[0]:.2f} m/s/s)   '
    f' {solid_objects[1]} g = {gravitational_accelerations[1]:.2f} m/s/s)')

print(58*'-')

#print small headers (units)
print(f'{"t(s)":>10} {"y(m)":>10}    {"t(s)":>10} {"y(m)":>10}') 
print(f'{"----":>10} {"----":>10}    {"----":>10} {"----":>10}')

print(f'using for loop:')

#specifying end times
end_time_earth = 2 * initial_velocity / gravitational_accelerations[0]
end_time_moon = 2 * initial_velocity / gravitational_accelerations[1]


for i in range(number_of_times + 1):
    #Earth
    t1 = i * end_time_earth / number_of_times
    y1 = initial_velocity * i - (0.5) * gravitational_accelerations[0] * i**2

    #Moon
    t2 = i * end_time_moon / number_of_times
    y2 = initial_velocity * i - (0.5) * gravitational_accelerations[1] * i**2

    print(f' {t1:10.2f} {y1:10.2f}   {t2:10.2f} {y2:10.2f}')

# while loop 
print(f'using a while loop:')

i = 0 
while i <= number_of_times:
    #Earth
    t1 = i * end_time_earth / number_of_times
    y1 = initial_velocity * i - (0.5) * gravitational_accelerations[0] * i**2

    print(f' {t1:10.2f} {y1:10.2f}')
    i += 1

print ()

i = 0

while i <= number_of_times:
    #Moon
    t2 = i *end_time_moon / number_of_times
    y2 = initial_velocity * i - (0.5) * gravitational_accelerations[1] * i**2

    print(f'{t2:35.2f}     {y2:<55.2f}')

    i += 1

print (58*'-')    
