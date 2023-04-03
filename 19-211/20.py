def k(x, p):
    if x>=35 and (p>3 and p%2==0):
        return 1
    else:
        if x>=35 or p<4:
            return 0
    return k(x+1, p+1) and k(x+2, p+1) and k(x*2, p+1)
for x in range(1, 35):
    if k(x, 1 ):
        print(x)
