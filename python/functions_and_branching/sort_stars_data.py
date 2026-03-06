nearby_star_data = [
    ('Alpja Centauri A', 4.3, 0.26, 1.56),
    ('Alpha Centauri B', 4.3, 0.077, 0.45),
    ('Alpha Centauri C', 4.2, 0.00001, 0.00006),
    ("Barnard's Star", 6.0, 0.00004, 0.0005),
    ('Wolf 359', 7.7, 0.000001, 0.00002),
    ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
    ('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
    ('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
    ('Sirius A', 8.6, 1.00, 23.6),
    ('Sirius B', 8.6, 0.001, 0.003),
    ('Ross 154', 9.4, 0.00002, 0.005),
]



#creating a seperate distance value list
distance_values = [a[1] for a in nearby_star_data]
   
def sort_distances(distance_values):
    less = []
    equal = []
    greater = []
    if len(distance_values) > 1:
        pivot = distance_values[0]
        for a in distance_values:
            if a < pivot:
                less.append(a)
            elif a == pivot:
                equal.append(a)
            elif a > pivot:
                greater.append(a)
        return sort_distances(less)+equal+sort_distances(greater)

    else:
        return distance_values


#print(f'{sort_distances(distance_values)}')




brightness_values = [a[2] for a in nearby_star_data]

def sort_by_brightness(brightness_values):
    less = []
    equal = []
    greater = []
    if len(brightness_values) > 1:
        pivot = brightness_values[0]
        for a in brightness_values:
            if a < pivot:
                less.append(a)
            elif a == pivot:
                equal.append(a)
            elif a > pivot:
                greater.append(a)
        return sort_by_brightness(less)+equal+sort_by_brightness(greater)

    else:return brightness_values


#print(f'{sort_by_brightness(brightness_values)}')



luminosity_values = [a[3] for a in nearby_star_data]

def sort_by_luminosity(luminosity_values):
    less = []
    equal = []
    greater = []
    if len(luminosity_values) > 1:
        pivot = luminosity_values[0]
        for a in luminosity_values:
            if a < pivot:
                less.append(a)
            elif a == pivot:
                equal.append(a)
            elif a > pivot:
                greater.append(a)
        return sort_by_luminosity(less)+equal+sort_by_luminosity(greater)
    else: return luminosity_values

#print(f'{sort_by_luminosity(luminosity_values)}

#making distance table

print(f')