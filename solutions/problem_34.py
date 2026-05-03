def factorial(n):
    if n == 1 or n == 0:
        return 1 
    else:
        return n * factorial(n-1)
    

def checkDigits(n):
    total = 0 
    for digit in str(n):
        total += factorial(int(digit))
    if total == n:
        return True
    return False

total = 0 
for x in range(3,100000):
    if checkDigits(x):
        total += x
print(total)
