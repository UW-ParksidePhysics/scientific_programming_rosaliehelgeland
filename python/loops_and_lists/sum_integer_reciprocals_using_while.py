summation = 0
starting_index = 1  
maximum_index = 100
    
index = 1
while index < maximum_index:
    summation += 1/index
          
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')