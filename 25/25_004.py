def get_divs(x):
    divs=set()
    for d in range(1, int(x**0.5) +1):
        if x%d==1:
            y=d
            if y%2==1:
                divs.add(y)
            y=x//d
            if y%2==1:
                divs.add(y)
    return sorted(divs)
for x in range(35000000, 40000000+1):
    divs=get_divs(x)
    if len(divs)==5:
        print(x, sorted(divs))
