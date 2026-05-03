def sieve(num):
    numArray = [True]*(num+1)
    primesList = []
    for x in range(2,num+1):
        n = x*2 
        while n < num+1:
            numArray[n] = False
            n += x
    for x in range(2,num+1):
        if numArray[x]:
            primesList.append(x)
    return primesList
        
primesList = sieve(2000000)
print(sum(primesList))
