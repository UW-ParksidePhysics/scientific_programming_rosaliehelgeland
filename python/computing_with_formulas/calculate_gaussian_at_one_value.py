from math import exp, sqrt, pi

m = 0. 
s = 2.
x = 1.

mean = m
standard_deviation = s
input_value = x



square_root_function = sqrt(2*pi)
numerator_right = 1.
denominator_right = square_root_function*s
fractional_square_rt = numerator_right/denominator_right

variable_numerator = x - m 
variable_function = variable_numerator/s
bracket_function = (-0.5)*((variable_function)**2)
left_side = exp(bracket_function)

gaussian_function = (fractional_square_rt)*(left_side)



print (f' The function inputs are listed below: ')

print (f' standard deviation is represented by variable s, and the value of s is {s} ')
print (f' mean is represented by variable m, and the value of m is {m} ')
print (f' the input value is represented by variable x, and the value of x is {x} ')


print (f'The output of the gaussian function is f(x) = {gaussian_function} ')
