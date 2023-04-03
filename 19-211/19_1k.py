def f(x, p):
    if x>=35 and p==3:
        return 1
    else:
        if x<35 and p==3:
            return 0
        else:
            if x>=35:
                return 0
    return f(x+1, p+1) or f(x+2, p+1) or f(x*2, p+1)
for x in range(1, 35):
    if f(x, 1):
        print(x)
#19-------------9------------

