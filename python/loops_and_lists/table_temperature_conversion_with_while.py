print (f' °F      °C')  #labels
print (f'______________')     #table heading

fahrenheit_temperature = 0.    #starting temperature
fahrenheit_step = 10. 

while fahrenheit_temperature <= 100:
    celsius_temperature = (fahrenheit_temperature - 32.) * (5./9.)
    print (f'{fahrenheit_temperature},   {celsius_temperature:.1f}')
    fahrenheit_temperature += fahrenheit_step

print (f'_________________')   #end of table 
