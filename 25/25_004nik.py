def divs(x):
    d=set()
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    d=[i for i in d if i%2==1]
    #print(x)
    return sorted(d)
for x in range(30000, 400000+1):
    if len(divs(x))==5:
        print(x, divs(x))
