print (f' °F      °C      °Ca')  #labels
print (f'________________________')     #table heading

fahrenheit_temperature = 0.    #starting temperature
fahrenheit_step = 10. 

while fahrenheit_temperature <= 100:
    celsius_temperature = (fahrenheit_temperature - 32.) * (5./9.)
    approx_temperature = (fahrenheit_temperature - 30.) / 2. #approximate temperature
    print (f'{fahrenheit_temperature},   {celsius_temperature:.1f},   {approx_temperature} ')
    fahrenheit_temperature += fahrenheit_step

print (f'________________________')   #end of table 
