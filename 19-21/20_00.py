def f(x, p):
    print(x, p)
    if (x>=35 or p>4) and p!=2:
        return p==4
    if p%2==0:
        return f(x+1, p+1) and f(x+2, p+1) and f(x*2, p+1)
    else:
        return f(x+1, p+1) or f(x+2, p+1) or f(x*2, p+1)
for s in range(1, 35):
    if f(s, 1)==1:
        print(s)
        #1516
