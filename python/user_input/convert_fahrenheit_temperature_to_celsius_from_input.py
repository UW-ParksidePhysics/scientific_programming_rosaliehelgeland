"""
fahrenheit_temperature = input('F=?')

fahrenheit_temperature = float(fahrenheit_temperature)

fahrenheit_to_celsius = F(C) = (5./9) * (fahrenheit_temperature - 32)

print(fahrenheit_to_celsius)
"""

import numpy as np 

fahrenheit_temperature = input('F=? ')

fahrenheit_temperature = float(fahrenheit_temperature)


def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    F = (5./9)*(fahrenheit_temperature-32)
    return F 


if __name__ == '__main__':
    test_fahrenheit_temperature = 0
    fahrenheit_temperature = test_fahrenheit_temperature

    print (convert_fahrenheit_to_celsius(fahrenheit_tem))