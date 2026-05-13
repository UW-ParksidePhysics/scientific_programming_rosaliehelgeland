    #structure outline

    # nearby_star_data = {
    #    "star_name": {
    #        "distance": distance_value,
    #        "apparent_brightness": apparent_brightness_value,
    #        "luminosity": luminosity_values 
    #        }
    #    }

stars = {}



def convert_lists_of_tuples(list_name):

    for data in list_name: 
        key, *values = data
        
        properties = ['distance', 'apparent_brightness', 'luminosity']

        stars[key] = dict(zip(properties, values))




def print_star_information(star_data, star_name):
    info = stars.get(star_name)

    print(f'{"Star:"}{star_name}')

    print(f'{"Distance (ly):":>18} {info["distance"]:>14}')

    print(f'{"Apparent Brightness (m):":>28} {info["apparent_brightness"]:>6}')

    print(f'{"Luminosity (L_sun):":>23} {info["luminosity"]:>11}')
    print()




if __name__ == '__main__':

    nearby_star_data = [
    ('Alpha Centauri A',    4.3,  0.26,      1.56),
    ('Alpha Centauri B',    4.3,  0.077,     0.45),
    ('Alpha Centauri C',    4.2,  0.00001,   0.00006),
    ("Barnard's Star",      6.0,  0.00004,   0.0005),
    ('Wolf 359',            7.7,  0.000001,  0.00002),
    ('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
    ('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
    ('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
    ('Sirius A',            8.6,  1.00,      23.6),
    ('Sirius B',            8.6,  0.001,     0.003),
    ('Ross 154',            9.4,  0.00002,   0.0005), 
    ]

    convert_lists_of_tuples(nearby_star_data)

    print_star_information(stars, 'Wolf 359')

    print_star_information(stars, 'Sirius A')