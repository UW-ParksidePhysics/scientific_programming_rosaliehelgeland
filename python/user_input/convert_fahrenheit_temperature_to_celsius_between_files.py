def extract_and_convert_fahrenheit(filename):
    infile = open(filename, 'r')

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
    
    infile.close()

fahrenheit, celsius = extract_and_convert_fahrenheit("/work/scientific_programming_rosaliehelgeland/python/user_input/Temperature data.2.txt")

print (f"Fahrenheit" "Celsius")

for f, c in zip(fahrenheit, celsius):
    print(f, c)