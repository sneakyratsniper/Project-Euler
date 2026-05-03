a = 1
b = 2
c = 3

total = 0 
while True:
    if c > 4000000:
        break
    if c % 2 == 0:
        total += c
    c = a+b
    a, b = b, c

print(total+2)
