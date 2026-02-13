from math import pi, log

m_large = 67.    #g
m_small = 47.    #g
p = 1.038        #g/cm^3
c = 3.7          #J/gK
k = 5.4*10**-3   #W/

Tw = 100.        #C
Ty = 70.         #C
T_room = 20.     #C
T_fridge = 4.    #C



left_numerator_sml = (m_small**(2/3))*((c*p)**(1/3))
left_numerator_lg = (m_large **(2/3))*((c*p)**(1/3))

left_denominator = (k*(pi**2))*(((4*pi)/3)**(2/3))


left_side_sml = left_numerator_sml/left_denominator
left_side_lg = left_numerator_lg/left_denominator



right_numerator_fridge = T_fridge - Tw
right_denominator = Ty - Tw
right_bracket_fridge = 0.76*(right_numerator_fridge/right_denominator)

right_side_fridge = log(right_bracket_fridge)


right_numerator_room = T_room - Tw
right_bracket_room = 0.76*(right_numerator_room/right_denominator)

right_side_room = log(right_bracket_room)



s_fridge_sml = (left_side_sml)*(right_side_fridge)  #sec
s_fridge_lg = (left_side_lg)*(right_side_fridge)    #sec

s_room_sml = (left_side_sml)*(right_side_room)      #sec
s_room_lg = (left_side_lg)*(right_side_room)        #sec



t_fridge_sml = s_fridge_sml/60   #mins
t_fridge_lg = s_fridge_lg/60     #mins

t_room_sml = s_room_sml/60       #mins
t_room_lg = s_room_lg/60            #mins



print (f' Small egg from fridge temperature cook time = {s_fridge_sml:.2f} s = {t_fridge_sml:.2f} min. ')
print (f' Large egg from fridge temperature cook time = {s_fridge_lg:.2f} s = {t_fridge_lg:.2f} min. ')
print (f' Small egg from room temperature cook time = {s_room_sml:.2f} s = {t_room_sml:.2f} min. ')
print (f' Large egg from room temperature cook time = {s_room_lg:.2f} s = {t_room_lg:.2f} min. ')



