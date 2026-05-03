def collatz(n):
    count = 0 
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        count += 1
    return count

collatz(10)

maxChain = 0 
highestNum = 0

#for n in range(1,1000000):
#    chain = collatz(n)
#    if chain > maxChain:
#        maxChain = chain
#        highestNum = n
#print(highestNum)
