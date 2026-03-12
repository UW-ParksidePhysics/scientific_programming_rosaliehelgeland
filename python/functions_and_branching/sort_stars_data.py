from functools import cmp_to_key


nearby_star_data = [
    ('  Alpja Centauri A ', 4.3, 0.26, 1.56),
    ('  Alpha Centauri B ', 4.3, 0.077, 0.45),
    ('  Alpha Centauri C ', 4.2, 0.00001, 0.00006),
    ("   Barnard's Star  ", 6.0, 0.00004, 0.0005),
    ('      Wolf 359     ', 7.7, 0.000001, 0.00002),
    ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
    ('   Luyten 726-8 A  ', 8.4, 0.000003, 0.00006),
    ('   Luyten 726-8 B  ', 8.4, 0.000002, 0.00004),
    ('      Sirius A     ', 8.6, 1.00, 23.6),
    ('      Sirius B     ', 8.6, 0.001, 0.003),
    ('      Ross 154     ', 9.4, 0.00002, 0.005),
]



#creating a seperate distance value list
distance_values = [a[1] for a in nearby_star_data]
   
def sort_by_distance(a, b):
    if a[1]<b[1]:
        return -1
    elif a[1]>b[1]:
        return 1
    else:
        return 0. 

def sort_by_brightness(a, b):
    if a[2]<b[2]:
        return -1
    if a[2]>b[2]:
        return 1
    else:
        return 0

def sort_by_luminosity(a, b):
    if a[3]<b[3]:
        return -1
    if a[3]>b[3]:
        return 1
    else:
        return 0

print(33*'-')

print(f'{"Star":>12}{"Distance":>20}')
print(f'{"--------------------":>4} {"---------":>12}')
for star in sorted(nearby_star_data, key=cmp_to_key(sort_by_distance)):
    print(f'{star[0]:>6} {star[1]:>10}')

print(33*'-')

print(35*'-')

print(f'{"Star":>12}{"Brightness":>22}')
print(f'{"--------------------":>4}{"-----------":>15}')

for star in sorted(nearby_star_data, key=cmp_to_key(sort_by_brightness)):
    print(f'{star[0]}{star[2]:>13.4}')

print(35*'-')

print(36*'-')

print(f'{"Star":>12}{"Luminosity":>23}')
print(f'{"--------------------":>4}{"-----------":>16}')

for star in sorted(nearby_star_data, key=cmp_to_key(sort_by_luminosity)):
    print(f'{star[0]:>6}{star[3]:>14.4}')

print(36*'-')