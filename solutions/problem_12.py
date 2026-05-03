from collections import Counter

def triangle(n):
    return n*(n+1)//2

def sieve(num):
    numArray = [True]*(num+1)
    primesList = []
    for x in range(2,num+1):
        if numArray[x]:
            primesList.append(x)
            for n in range(x**2,num+1,x):
                numArray[n] = False
    return primesList
        
primes = sieve(100)

def primeFactors(n):
    factors = []
    for p in primes:
        if p**2 > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p 
    if n > 1:
        factors.append(n)
    return factors

def countDiv(n):
    exps = Counter(primeFactors(n))
    div = 1 
    for exponent in exps.values():
        div *= exponent+1
    return div

divisors = 1
n = 1 
while divisors < 500:
    n += 1
    divisors = countDiv(triangle(n)) 

print(triangle(n))

