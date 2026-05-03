def divisible(num):
    isdiv = True
    for x in range(2,20):
        if num % x != 0:
            isdiv = False
    return isdiv
num =  20
running = True 
while running:
    if divisible(num):
        print(num)
        break
    else:
        num+= 20


