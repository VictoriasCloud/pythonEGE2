for x in range(174457, 174505+1):
    divs=set()
    for d in range(2, int(x**0.5)+1):
        if x%d==0:
            divs.add(d)
            divs.add(x//d)
            #print(x)
            if len(divs)>2:
                break
    if len(divs)==2:
        print(x, sorted(divs))
