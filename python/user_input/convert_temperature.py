"""
converting_temperatures(kelvin , fahrenheit , celsius):

convert_celsius_from_fahrenheit : C(F) = (5./9)*(fahrenheit - 32)

convert_celsius_from_kelvin : C(K) = kelvin - 274.15

convert_fahrenheit_from_celsius : F(C) = (9./5) * (celsius + 32)

convert_fahrenheit_from_kelvin : F(K) = (9./5) * ((kelvin - 274.15) + 32)

convert_kelvin_from_celsius : K(C) = celsius + 274.15

convert_kelvin_from_fahrenheit : K(F) = 274.15 + ((5./9) * (fahrenheit - 32))
"""



""" This is a test string """

import numpy as np 


def convert_celsius_from_fahrenheit(fahrenheit):
    CF = (5./9)*(fahrenheit-32)
    return CF 
if __name__ == '__main__':
    test_fahrenheit = 100
    
    print (convert_celsius_from_fahrenheit(test_fahrenheit))




def convert_celsius_from_kelvin(kelvin):
    CK = kelvin - 274.15
    return CK
if __name__ == '__main__':
    test_kelvin = 500

    print(convert_celsius_from_kelvin(test_kelvin))
 



def convert_fahrenheit_from_celsius(celsius):
    FC = (9./5) * celsius + 32

    return FC 
if __name__ == '__main__':
    test_celsius = 0
    
    print(convert_fahrenheit_from_celsius(test_celsius))


def convert_fahrenheit_from_kelvin(kelvin):
    FK = (9./5) * (kelvin-274.15) +32

    return FK
if __name__ == '__main__':
    test_kelvin = 600

    print(convert_fahrenheit_from_kelvin(test_kelvin))


def convert_kelvin_from_celsius(celsius):
    KC = celsius + 274.15

    return KC 
if __name__ == '__main__':
    test_celsius = 30

    print(convert_kelvin_from_celsius(test_celsius))


def convert_kelvin_from_fahrenheit(fahrenheit):
    KF = 274.15 + (5./9*fahrenheit)-32
    
    return KF 
if __name__ == '__main__':
    test_fahrenheit = 100

    print(convert_kelvin_from_fahrenheit(test_fahrenheit))

""" #inputs
    celsius_from_fahrenheit_input = 100
    celsius_from_kelvin_input = 500
    fahrenheit_from_celsius_input = 0
    fahrenheit_from_kelvin_input = 600
    kelvin_from_celsius_input = 30 
    kelvin_from_fahrenheit_input = 100

    #outputs
    celsius_from_fahrenheit_output = 37.7778
    celsius_from_kelvin_output = 225.85
    fahrenheit_from_celsius_output = 32
    fahrenheit_from_kelvin_output = 618.53
    kelvin_from_celsius_output = 304.15
    kelvin_from_fahrenheit_output = 297.7056
    """

celsius_from_fahrenheit_input = 100
celsius_from_kelvin_input = 500
fahrenheit_from_celsius_input = 0
fahrenheit_from_kelvin_input = 600
kelvin_from_celsius_input = 30 
kelvin_from_fahrenheit_input = 100

#outputs
celsius_from_fahrenheit_output = 37.7778
celsius_from_kelvin_output = 225.85
fahrenheit_from_celsius_output = 32
fahrenheit_from_kelvin_output = 618.53
kelvin_from_celsius_output = 304.15
kelvin_from_fahrenheit_output = 297.7056




def test_conversion():
    fahrenheit_temperature = 100
    celsius_temperature = 500
    

    test_fahrenheit_from_celsius = convert_fahrenheit_from_celsius(convert_celsius_from_fahrenheit(fahrenheit_temperature))
    return test_fahrenheit_from_celsius

    test_celsius_from_kelvin = convert_kelvin_from_celsius(convert_celsius_from_kelvin(celsius_temperature))
    return test_celsius_from_kelvin

    test_fahrenheit_from_kelvin = convert_fahrenheit_from_kelvin(convert_kelvin_from_fahrenheit(fahrenheit_temperature))
    return test_fahrenheit_from_kelvin

    def float_equal(test_FC, test_CK, test_FK, tolerance = 0.1)

   


