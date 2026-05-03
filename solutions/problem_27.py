def sieve(num):
    numArray = [True]*(num+1)
    primesList = []
    for x in range(2,num+1):
        if numArray[x]:
            primesList.append(x)
            for n in range(x**2,num+1,x):
                numArray[n] = False
    return primesList

primesList = sieve(1000)
primesSet = set(sieve(100000))

def count_primes(a,b):
    n = 0 
    while int(n**2 + a*n + b) in primesSet:
        n+=1
    return n 
            
highest = 0
co = (0,0)
for b in primesList:
    for a in range(-999,1000):
        primecount = count_primes(a,b)
        if primecount > highest:
            highest = primecount 
            co = (a,b)

print(co[0]*co[1])
            
        




     
