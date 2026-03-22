#infile = open('/work/scientific_programming_rosaliehelgeland/python/user_input/Temperature data.txt', 'r')
#filestring = infile.read()
#filestring
from io import StringIO


def extract_and_convert_fahrenheit(infile):

    for line in infile:

        if "Fahrenheit" in line:

            indexes = line.split(":")
            temp = indexes[1]
            temp = temp.split()

            fahrenheit = float(temp[0])

            celsius = (5./9)*(fahrenheit-32)

            return celsius
    

if __name__ == '__main__':

    temperature_data = StringIO(""" Temperature Data
    ----------------
    Fahrenheit degree: 67.2
    """)

    celsius_conversion = extract_and_convert_fahrenheit(temperature_data)

    print(celsius_conversion, 'Degrees Celsius')