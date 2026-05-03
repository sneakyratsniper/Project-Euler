def checkSum(num):
    total = 0 
    for digit in str(num):
        total += int(digit) ** 5
    if total == num:
        return True
    return False


total = 0 
for x in range(2,10000000):
    if checkSum(x):
        total += x

print(total)

    
