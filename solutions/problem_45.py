import time
def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)
    

t = {triangle(n) for n in range(100000)}
p = {pentagonal(n) for n in range(100000)}
h = {hexagonal(n) for n in range(100000)}
print(t.intersection(p,h))


