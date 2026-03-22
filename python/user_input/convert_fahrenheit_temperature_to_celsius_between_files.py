from io import StringIO


def extract_and_convert_fahrenheit(infile):

    fahrenheit_temps = []
    
    celsius_temps = []


    for line in infile:

        if "Fahrenheit" in line:

            indexes = line.split(":")
            temp = indexes[1]
            temp = temp.split()

            F = float(temp[0])

            C = (5./9)*(F - 32)

            fahrenheit_temps.append(F)
            celsius_temps.append(C)

        
    return fahrenheit_temps, celsius_temps
    


temperature_data = StringIO(""" Temperature data
 ----------------
 Fahrenheit degrees: 67.2
 Fahrenheit degrees: 66.0
 Fahrenheit degrees: 78.9
 Fahrenheit degrees: 102.1
 Fahrenheit degrees: 32.0
 Fahrenheit degrees: 87.8""")


fahrenheit, celsius = extract_and_convert_fahrenheit(temperature_data)

print ('-'*21)

print (f'{"Fahrenheit"} {"Celsius":>9}')

print (f'{"----------"} {"-------":>9}')

for f, c in zip(fahrenheit, celsius):
    print(f'{f:>7.4} {c:>10.3}')

print ('-'*21)