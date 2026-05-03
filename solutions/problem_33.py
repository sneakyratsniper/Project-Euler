def tryPair(a,b):
    if a != 0 and b != 0 and b>a:
        return a/b
    return 0

ans = []
for a in range(1,100):
    for b in range(1,100):
        try:
            a1,a2 = int(str(a)[0]),int(str(a)[1])
        except:
            a1,a2 = int(str(a)[0]),0 
        try:
            b1,b2 = int(str(b)[0]),int(str(b)[1])
        except:
            b1,b2 = int(str(b)[0]),0
        if a1 == a2 or b1 == b2 or (a1*a2*b1*b2)==0:
            continue
        fract = a/b
        if fract == tryPair(a1,b1) or fract == tryPair(a1,b2) or fract == tryPair(a2,b1) or fract == tryPair(a2,b2):
            ans.append((a,b))
            

def checkValues(f,i,j):
    for a in str(f[0]):
        for b in str(f[1]):
            if a!=i and b!=j:
                if int(f[0])/int(f[1]) == int(a)/int(b):
                    print(f)
                    return True
    return False
 
def checkFrac(f):
    for a in str(f[0]):
        for b in str(f[1]):
            if a == b:
                checkValues(f,a,b)
                
    return False

for f in ans:
    if checkFrac(f):
        print(f)
        


