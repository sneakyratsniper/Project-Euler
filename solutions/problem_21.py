import math
def d(n):
    return sum(i+n//i for i in range(2,int(math.sqrt(n))+1) if n%i == 0) + 1

total = 0 

for n in range(10000):
    s = d(n)
    if n == s or s >= 10000:
        continue
    elif d(s) == n:
        total += s + n 

print(total/2)

    

