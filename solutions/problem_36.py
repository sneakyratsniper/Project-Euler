def palindrome(num):
    num = str(num)
    for x in range(len(num) // 2):
        if num[x] != num[-x-1]:
            return False
    return True

for x in range(1000000):
    if palindrome(x) and palindrome(str(bin(x))[2:]) and str(bin(x))[2:][0] != '0':
        total += x

print(total)
