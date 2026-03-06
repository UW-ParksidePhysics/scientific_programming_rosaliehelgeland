def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperaute):
    return (5./9)*(fahrenheit_temperaute - 32)

print(60*'-')

print(f'converting from fahrenheit to celsius: ')

print(60*'-')

print(f'convert_fahrenheit_temperature_to_celsius(32) = {convert_fahrenheit_temperature_to_celsius(32):.1f}°C')
print(f'convert_fahrenheit_temperature_to_celsius(69.8) = {convert_fahrenheit_temperature_to_celsius(69.9):.1f}°C')
print(f'convert_fahrenheit_temperature_to_celsius(262) = {convert_fahrenheit_temperature_to_celsius(212):.1f}°C')

print(60*'-')

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
    return (9./5)*celsius_temperature + 32

print(f'to test my values:')

print(60*'-')

print (f'convert_celsius_temperature_to_fahrenheit(0) = {convert_celsius_temperature_to_fahrenheit(0):.1f}°F')
print (f'convert_celsius_temperature_to_fahrenheit(21) = {convert_celsius_temperature_to_fahrenheit(21):.1f}°F')
print (f'convert_celsius_temperature_to_fahrenheit(100) = {convert_celsius_temperature_to_fahrenheit(100):.1f}°F')

print(60*'-')

