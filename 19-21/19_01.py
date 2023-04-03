def f(x, p):
    if x>=63 or p>3:
        return p==3
    if p%2==0:
        return f(x+1, p+1) or f(x+4, p+1) or f(x*5, p+1)
    else:
        return f(x+1, p+1) or f(x+4, p+1) or f(x*5, p+1)
for x in range(1, 63):
    if f(x, 1):
        print(x)
#3

