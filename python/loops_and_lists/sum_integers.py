maximum_integer = 10
n = maximum_integer
starting_integer = 1
integers = []

print (f'n = {maximum_integer}')

for integers in range(n+1):
    summation = (integers * (integers + 1))/2
    print (
    f'sum(1, {integers}) = {summation}'
    )

summation_formula = (n*(n+1))/2
print (f'n(n+1)/2 = {summation_formula}')

