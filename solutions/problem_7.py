import random
def isprime(num):
    num = int(num)
    isprime = True
    for x in range(2,8):
        if pow(x,num-1,num) == (1 % num):
            isprime = False
    return isprime


def is_prime(n,a):
    #Check small primes
    if n % 2 == 0 : return False
    for x in range(3,min(10001,n),2):
        if n % x == 0 : return False

    if n < 3 : raise ValueError("arg must be greater than or equal to 3")
   
    #Miller Rabin
    #Step 1 : Solve n - 1 = d*2**s
    d = n-1
    s = 0 
    while d % 2 == 0:
        d = d // 2
        s += 1 

    #Step 2 : x = a**d mod n
    x = pow(a,d,n)
    if x == 1 or x == n-1:
        return True
    else:
        #Step 3 : a**d*2**r mod n
        for i in range(0,s):
            x1 = pow(x,2,n)
            if x1 == n-1:
                return True
            x = x1
    return False

num = 5
primeNum= 2
while primeNum != 10001:
    numIsPrime = True
    for y in range(10):
        a = random.randrange(2,num-1)
        if is_prime(num,a) is False:
            numIsPrime = False
    if numIsPrime == True:
        primeNum += 1
    num+=2

print(num)
