def fin_c(x):
    divs=set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            y = d
            if y%2==0:
                divs.add(y)
            y=x//d
            if y%2==0:
                divs.add(y)
    return sorted(divs)
for x in range(125256, 125330+1):
    divs=fin_c(x)
    if len(fin_c(x))==6:
        print(x, sorted(divs))


