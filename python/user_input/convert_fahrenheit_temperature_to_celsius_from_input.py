
def convert_fahrenheit_to_celsius(fahrenheit_temperature):
    celsius_temperature = (5./9)*(fahrenheit_temperature-32)

    return celsius_temperature




#test cell

if __name__ == '__main__':
    
    fahrenheit_temperature = input('F=?')

    fahrenheit_temperature = float(fahrenheit_temperature)

    print (convert_fahrenheit_to_celsius(fahrenheit_temperature))