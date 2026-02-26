times = [0.00, 0.11, 0.23, 0.34, 0.45, 0.57, 0.68, 0.79, 0.91, 1.02]
positions = [0.00, 0.09, -9.62, -29.15, -58.48, -97.62, -146.58, -205.34, -273.92, -352.31]

times_positions = [times, positions]

for t, p in zip(times_positions[0], times_positions[1]):
    print (t, p)




