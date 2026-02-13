one_kilometer = 1.
centimeters = one_kilometer*100000.
inches = centimeters/2.54
feet = inches/12.
yards = feet/3.
miles = yards/1760.

distance_from_parkside = 8.04672*one_kilometer

distance_in_inches = distance_from_parkside * inches

print (f' I live {distance_from_parkside} kilometers from Parkside. ')
print (f' {distance_from_parkside} kilometers in inches is {distance_in_inches}. ')
print (f' {8.04672*inches} inches is {8.04672*feet} in feet. ')
print (f' which is {8.04672*yards} in yards. ')
print (f' and {8.04672*miles} in miles. ')

print (f' for verification, 0.640 kilometers is equal to {0.640*feet} feet. ')
