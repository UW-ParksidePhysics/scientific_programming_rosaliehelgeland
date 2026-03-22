import sys

sys.argv = ['convert_fahrenheit_to_celsius_from_command_line', 100]


def convert_fahrenheit_to_celsius(fahrenheit_temperature):

    celsius_temperature = (5./9)*(fahrenheit_temperature-32)

    return celsius_temperature


if __name__ == '__main__':
    print (f'run as program:')
    fahrenheit = float(sys.argv[1])
    print (f'{sys.argv[1]} degrees fahrenheit converts to {convert_fahrenheit_to_celsius(fahrenheit)} degrees celsius')