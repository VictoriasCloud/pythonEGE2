def f(x, p):
    if x>=101 and p==3:
        return 1
    else:
        if x<101 and p==3:
            return 0
        else:
            if x>=101:
                return 0
    return f(x+1, p+1) or f(x*5, p+1)
for s in range(1, 100+1):
    if f(s, 1):
        print(s)
