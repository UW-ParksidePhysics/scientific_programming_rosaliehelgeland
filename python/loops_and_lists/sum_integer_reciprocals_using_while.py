#summation = 0
#starting_index = 1
#index = starting_index
#maximum_index = 100
      
#while index < maximum_index: 
   # summation += 1/index 
          
#print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}') 

# METHOD 1:
#cant use index < maximumum index because its always true, so it loops infinitely, only goes to 99
# in order for the index to work, it needs to equal +=1
# the maximum index in the while loop only goes to 99, if thats not fixed then putting the second value as 100 is misleading

#METHOD 2:
#my results: 1 + 0.5 + 0.333 = 1.0833

#GEMINI OUTPUT:
#The script you’ve shared is actually a classic "infinite loop" trap. If you ran this, your computer 
#would sit there spinning its wheels forever (or until you manually stopped it) because the value of index 
#never changes.

#Here is the breakdown of what is going wrong:
#1. The Missing Increment
#The biggest issue is that you never increase the value of index inside the loop. Since index 
#starts at 1 and 1 is always less than 100, the condition while index < maximum_index stays true forever.

#The Fix: You need to add index += 1 at the end of your loop.

#2. The Logic of the Limit
#In your print statement, you describe the sum as going from $k = 1$ to $100$. However, your 
#loop condition is index < maximum_index.

#Current behavior: The loop stops at 99.Intended behavior: To include 100, you should use index <= maximum_index.

summation = 0
starting_index = 1
index = starting_index
maximum_index = [3, 100]

while index <= maximum_index[0]:
    summation += 1/index
    index += 1

print(f' sum(k = {starting_index}, {maximum_index[0]}) 1/k = {summation}')

while index <= maximum_index[1]:
    summation += 1/index
    index += 1

print(f' sum(k = {starting_index}, {maximum_index[1]}) 1/k = {summation}')
 