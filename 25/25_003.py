for x in range(125256, 125330+1):
    divs=set()
    for d in range(1, int(x**0.5)+1):
        if d%2==0:
            d=x//d
            if d%2==0:
                divs.add(d)
                divs.add(x//d)
    if len(divs)==6:
        print(x, sorted(divs))
