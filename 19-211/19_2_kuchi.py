def f(x, y, p):
    if x+y>=77 and p==3:
        return True
    else:
        if x+y<77 and p==3:
            return False
        else:
            if x+y>=77:
                return False
    return f(x+1, y, p+1) or f(x*2, y, p+1) or f(x, y+1, p+1) or f(x, y*2, p+1)
for s in range(1, 69+1):
    if f(7, s, 1):
        print(s)
        break
