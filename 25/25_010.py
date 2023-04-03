def div(x):
    divs=set()
    for d in range(1, int(x**0.5) +1):
        if x%d==0:
            divs.add(d)
            divs.add(x//d)
    return sorted(divs)
for x in range(1, int(input())+1):
    divs=div(x)
print(len(divs))
