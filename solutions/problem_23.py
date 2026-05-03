import math
def d(n):
    sq = math.sqrt(n)
    s = sum(x+(n//x) for x in range(1,int(sq)+1) if n%x==0) - n 
    if int(sq) == sq:
        return s - sq
    return s

def checkn(n):
    s = d(n)
    if s > n:
        return 'abundant'
    elif s < n:
        return 'deficient'

    return 'perfect'
    

UPPER_LIMIT = 28123
abundants = [n for n in range(12,UPPER_LIMIT) if checkn(n) == 'abundant']
abundant_sums = set()

for a1 in abundants:
    for a2 in abundants:
        s = a1+a2
        if s <= UPPER_LIMIT:
            abundant_sums.add(s)
        else:
            break

sN = 0.5*UPPER_LIMIT*(UPPER_LIMIT+1)
print(sN-sum(abundant_sums))




