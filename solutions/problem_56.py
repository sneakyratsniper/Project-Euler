def dsum(n):
    return sum(int(d) for d in str(n))


highest = 0 
ma =  0
mb = 0 
for a in range(100):
    for b in range(100):
        s = dsum(a**b)
        if s > highest:
            highest = s 
            ma = a
            mb = b 

print(highest,ma,mb)




