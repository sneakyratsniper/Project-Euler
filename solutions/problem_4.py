import math
def is_palindrome(num):
    palindrome = True
    num = str(num)
    for x in range(len(num)//2):
        if num[x] != num[-x-1]:
            palindrome = False  
    return palindrome

 
for max in range(900000,1000000):
    if is_palindrome(max):
        factors = []
        for x in range(2,max):
            if max%x == 0:
                factors.append(x)

        for x in factors:
            for y in factors:
                if x * y == max and len(str(x)) == 3 and len(str(y)) == 3:
                    print("X",x,"Y",y)

