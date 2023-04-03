def f(x, p):
    if x>=77 and p==3:
        return True
    else:
        if x<77 and p==3:
            return False
        else:
            if x>=77:
                return False
    return f(x+1, p+1) or f(x*2, p+1) or f(x,  p+1) or f(x, p+1)
for s in range(1, 69+1):
    if f(s, 1):
        print(s)
        break
