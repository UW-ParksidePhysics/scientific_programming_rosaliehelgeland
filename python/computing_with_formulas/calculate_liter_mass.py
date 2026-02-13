gasoline_density = 0.755          #g/cm^3
iron_density = 787.               #g/cm^3
air_density = .12                 #g/cm^3
ice_density = 91.67               #g/cm^3
silver_density = 1050.            #g/cm^3
platinum_density = 2145.          #g/cm^3
human_body_density = 1.096        #g/cm^3

liter_conversion = 1/1000                    #liter/mililiter

gasoline_weight = (gasoline_density)*(liter_conversion)
iron_weight = (iron_density)*(liter_conversion)
air_weight = (air_density)*(liter_conversion)
ice_weight = (ice_density)*(liter_conversion)
silver_weight = (silver_density)*(liter_conversion)
platinum_weight = (platinum_density)*(liter_conversion)
human_body_weight = (human_body_density)*(liter_conversion)



print (f' the weight of one liter of gasoline is {gasoline_weight} grams ')
print (f' the weight of one liter of iron is {iron_weight} g. ')
print (f' the weight of one liter of air is {air_weight} g. ')
print (f' the weight of one liter of ice is {ice_weight} g. ')
print (f' the weight of one liter of silver is {silver_weight} g. ')
print (f' the weight of one liter of platinum is {platinum_weight} g. ')
print (f' the weight of one liter of the human body is {human_body_weight} g. ')
