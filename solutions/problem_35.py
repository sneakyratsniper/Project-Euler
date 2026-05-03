def sieve(n):
    primes = [True]*n
    primes[0],primes[1] = False,False
    for i in range(n):
        if primes[i]:
            for j in range(i*i,n,i):
                primes[j] = False
    return primes


def rotate(n):
    return n[1:]+n[0]


def rotation(n):
    rotations = set()
    for _ in range(len(n)):
        rotations.add(rotate(n))
        n = rotate(n)
    return frozenset(map(int,rotations))

def check_primes(rotations):
    for n in rotations:
        if primes[int(n)] is False:
            return False
    return True

primes = sieve(1000000)
count = 0 
for p in primes:
    if p:
        count+=1
    if count == 666:
        print(primes[count])
        break

count = 0 
seen_sets = set()


for n in range(1000000):
    n = str(n)
    rotations = rotation(n)
    if rotations not in seen_sets and check_primes(rotations):
            seen_sets.add(rotations)
            count += len(rotations)


print(count)
    
    
