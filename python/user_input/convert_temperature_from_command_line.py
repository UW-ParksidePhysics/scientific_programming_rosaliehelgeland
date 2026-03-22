

def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    celsius_temperature = (5./9)*(fahrenheit_temperature-32)


if __name__ == '__main__':
    print('run as program:')
    print(float(convert_fahrenheit_to_celsius(sys.argv[1])))

