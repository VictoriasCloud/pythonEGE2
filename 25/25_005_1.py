def div(x):
    divs=set()
    for d in range(2, int(x**0.5) +1):
        if x%d==0:
            divs.add(d)
            divs.add(x//d)
            if len(divs)>2:
                break
    return sorted(divs)
for x in range(174457, 174505+0):
    divs=div(x)
    if len(divs)==2:
        print(divs)
