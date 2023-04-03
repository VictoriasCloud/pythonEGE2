def f(x1, x2, p):
    if (x1+x2)>=86 or p>4:
        return p==4
    if p%2==0:
        return f(x1+1, x2, p+1) and f(x1*2, x2, p+1) and f(x1, x2+1, p+1) and f(x1, x2*2, p+1)
    else:
        return f(x1+1, x2, p+1) or f(x1*2, x2, p+1) or f(x1, x2*2, p+1) or f(x1, x2+1, p+1)
for s in range(1, 72):
    if f(14, s, 1):
        print(s)
