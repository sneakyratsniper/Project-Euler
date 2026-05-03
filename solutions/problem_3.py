def isprime(num):
    num = int(num)
    for x in range(2,8):
        if pow(3,num-1,num) == (1 % num):
            return True
        return False
max = 600851475143 
primefactors = []
for x in range(2,775146):
    if max%x == 0 and isprime(x):
        primefactors.append(x)
        print(x)

'''
primefactors = []
while isprime(max) != True or max == 3:
    for y in range(2,100):
        if (y == 2 or y == 3 or (y % 2 == 1 and isprime(y))) and (max % y == 0):
            primefactors.append(max/y)
            print(primefactors)
            max = max/y
            break
    for x in range(1,num):
       if 60081475143 % x == 0 and flt(x):
            if x > max:
                max = x
                print(max)
'''
print(primefactors)
print("done")
