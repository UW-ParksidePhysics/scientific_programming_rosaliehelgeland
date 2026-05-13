def parse_constants_file(filename):
    infile = open(filename, 'r')
    
    constants = {}
    
    
    for line in infile:
        
        words = line.split()
        
        if len(words) < 2:
            continue
        
        try:
            constant = float(words[-2])
            
        except ValueError:
            continue
        
        if len(words[:-2]) == 3:
            name = words[0] + ' ' + words[1] + ' ' + words[2]
            
        elif len(words[:-2]) == 2:
            name = words[0] + ' ' + words[1]
        
        else:
            name = words[0]
        
        constants[name] = constant
    infile.close()
    return constants 

if __name__ == '__main__':
    
    test_filename = "constants_test.txt"
    
    with open(test_filename, 'w') as f:
        f.write("""  name of constant           value              dimension
                ------------------------------------------------------------
                speed of light     299792458.0  m/s
                gravitational constant 6.67259e-11 m**3/kg/s**2
                Planck constant 6,6260755e-34 J*s
                elementary charge 1.60217733e-19 C
                Avogadro number 6.0221367e23 1/mol
                Boltzmann constant 1.380658e-23 J/K
                electron mass 9.1093897e-31 kg
                proton mass 1.6726231e-27 kg""")
        
    constants = parse_constants_file(test_filename)
    
    print(constants)