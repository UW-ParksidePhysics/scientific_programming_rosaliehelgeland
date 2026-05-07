

def parse_viscosity_data(filename):
    viscosity_data = {}

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith('#') or line == '':
                continue
            
            data = line.split()

            gas = ' '.join(data[:-3])
            values = [float(v) for v in data[-3:]]

            properties = ['viscosity', 'reference_temperature', 'reference_viscosity']

            viscosity_data[gas] = dict(zip(properties, values))

        return viscosity_data
        


def calculate_viscosity(temperature, gas, viscosity_data):
    info = viscosity_data[gas]

    C = info['viscosity']
    T0 = info['reference_temperature']
    mu0 = info['reference_viscosity']
    return (mu0* (T0 + C)/(temperature+C) * (temperature/T0)**1.5)


if __name__ == '__main__':
    import numpy as np 
    import matplotlib.pyplot as plt
    test_filename = "viscosity_of_gasses.dat"

    with open(test_filename, 'w') as f:
        f.write(""" #Viscosity data of some gases
        # Sutherland's formula for the viscosity:
        # mu = mu_0*(T_0 + C)/(T + C)(T/T_0)**1.5
        # Column 1: gas name
        # Column 2: C (in Kelvin) (Sutherland's constant)
        # Column 3: T_0 (in Kelvin)
        # Column 4: mu_0 (in 10**-6 Pa*s)

        # gas              C     T_0     mu_0
        air 120 291.15 18.27
        nitrogen 111 300.55 17.81
        oxygen 127 292.25 20.18
        carbon dioxide 240 293.15 14.8
        carbon monoxide 118 288.15 17.2
        hydrogen 72 293.85 8.76
        ammonia 370 293.15 9.82
        sulphur dioxide 416 293.65 12.54

        # Source: http://en.wikipedia.org/wiki/Viscosity
        
        """)
    viscosity_data = parse_viscosity_data(test_filename)
    
    temperatures = np.linspace(223, 373, 200)

    gas_names = ["air", "carbon dioxide", "hydrogen"]

    for gas in gas_names:
        viscosity = calculate_viscosity(temperatures, gas, viscosity_data)
        plt.plot(temperatures, viscosity, label=gas)

        plt.xlabel("Temperatures (K)")
        plt.ylabel("Viscosity (μ)")
        plt.legend()
        plt.show()