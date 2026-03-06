def calculate_velocity_and_acceleration(positions, index, time_step=1e-6):
    velocity = (positions[index+1]-(positions[index-1]))/(2*time_step)
    acceleration = (positions[index+1]-2*positions[index]+positions[index-1])/time_step**2
    return velocity, acceleration

times = [0, 0.5, 1.5, 2.2]
def test_kinematics(positions, velocity):
    positions = [velocity*t for t in times]


print(f'for non-constant velocity:')

positions = list(range(0, 5, 1))

for i in range(1, len(positions)-1):
    print(calculate_velocity_and_acceleration(positions, i, 1e-6))

