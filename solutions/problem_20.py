import math
number = math.factorial(100) 
total = 0 
for digit in range(len(str(number))):
    total += int(str(number)[digit])
    
print(total)
