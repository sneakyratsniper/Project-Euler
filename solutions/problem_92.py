def next_chain(num):
    return sum(int(n)**2 for n in str(num))

def chain(n):
    while n != 1 and n != 89:
        n = next_chain(n)
    if n == 1:
        return False
    return True

count = 0 
for n in range(1,10000000):
    if chain(n):
        count += 1 

print(count)

        
    

