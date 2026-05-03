def matchDigits(a,b):
    for x in a:
        try:
            b.remove(x)
        except ValueError:
            return False
    return True

num = 0 
running = True
while running:
    num+=1 
    running = False

    for k in range(2,7):
        if not matchDigits([x for x in str(num)], [x for x in str(num*k)]):
            running = True
 
print(num)


