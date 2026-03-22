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

#FAHRENHEIT ---> CELSIUS
def convert_celsius_from_fahrenheit(fahrenheit):
    CF = (5./9)*(fahrenheit-32)
    return CF 
if __name__ == '__main__':
    test_fahrenheit = 100
    
    print (convert_celsius_from_fahrenheit(test_fahrenheit))



#KELVIN ---> CELSIUS
def convert_celsius_from_kelvin(kelvin):
    CK = kelvin - 274.15
    return CK
if __name__ == '__main__':
    test_kelvin = 500

    print(convert_celsius_from_kelvin(test_kelvin))
 


#CELSIUS ---> FAHRENHEIT
def convert_fahrenheit_from_celsius(celsius):
    FC = (9./5) * celsius + 32

    return FC 
if __name__ == '__main__':
    test_celsius = 0
    
    print(convert_fahrenheit_from_celsius(test_celsius))



#KELVIN ---> FAHRENHEIT
def convert_fahrenheit_from_kelvin(kelvin):
    FK = (kelvin - 273.15) * 9./5 + 32

    return FK
if __name__ == '__main__':
    test_kelvin = 600

    print(convert_fahrenheit_from_kelvin(test_kelvin))



#CELSIUS ---> KELVIN
def convert_kelvin_from_celsius(celsius):
    KC = celsius + 274.15

    return KC 
if __name__ == '__main__':
    test_celsius = 30

    print(convert_kelvin_from_celsius(test_celsius))



#FAHRENHEIT ---> KELVIN
def convert_kelvin_from_fahrenheit(fahrenheit):
    KF = (fahrenheit - 32) * 5./9 + 273.15
    
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


#test celsius_to_fahrenheit(fahrenheit_to_celsius(fahrenheit_temeprature)) is fahrenheit_temperature WITHIN TOLERANCE
#test kelvin_to_celsius(celsius_to_kelvin(celsius_temperature)) is celsius_temperature WITHIN TOLERANCE
#test kelvin_to_fahrenheit(fahrenheit_to_kelvin(fahrenheit_temperature)) is fahrenheit_temperature WITHIN TOLERANCE

def test_conversions():
    # fahrenheit, celsius input values
    fahrenheit_temperature = 100
    celsius_temperature = 0

    #testing celsius -> fahrenheit and fahrenheit -> celsius:
    celsius = convert_celsius_from_fahrenheit(fahrenheit_temperature)

    test_fahrenheit_output_from_celsius_conversion = convert_fahrenheit_from_celsius(celsius)


    #testing kelvin -> celsius and celsius -> kelvin
    kelvin = convert_kelvin_from_celsius(celsius_temperature)

    test_celsius_output_from_kelvin = convert_celsius_from_kelvin(kelvin)


    #testing kelvin -> fahrenheit and fahrenheit -> kelvin:
    test_kelvin = convert_kelvin_from_fahrenheit(fahrenheit_temperature)

    test_fahrenheit_output_from_kelvin = convert_fahrenheit_from_kelvin(test_kelvin)


    #defining "equal" as within tolerance:

    def temperatures_equal(value_a, value_b, tolerance=0.1):
        return abs(value_a - value_b ) <= tolerance
    
    #test function with temperatures

    success =(
        temperatures_equal(test_fahrenheit_output_from_celsius_conversion, fahrenheit_temperature)
        and temperatures_equal(test_celsius_output_from_kelvin, celsius_temperature)
        and temperatures_equal(test_fahrenheit_output_from_kelvin, fahrenheit_temperature)
    )

    message =(
        f" conversions failed:\n"
        f" test fahrenheit result was {test_fahrenheit_output_from_celsius_conversion:g} and actual is {fahrenheit_temperature:g}:\n"
        f" test celsius result was {test_celsius_output_from_kelvin:g} and actual is {celsius_temperature:g}:\n"
        f" test fahrenheit result was {test_fahrenheit_output_from_kelvin:g} and actual is {fahrenheit_temperature:g}:\n"
    )

    assert success, message

if __name__ == '__main__':
    test_conversions()

   


