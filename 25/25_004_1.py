for x in range(35000000, 40000000+1):
    divs=set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            divs.add(d)
            divs.add(x//d)
            if len(divs)>5:
                break
if len(divs)==5:
    print(sorted(divs))
