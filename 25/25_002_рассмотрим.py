for i in range(1000000, 2000001):
    divs=set()
    c=0
    for d in range(1, round(i**0.5)+1):
        if i % d == 0:
            if (abs(i/d-d))<=100:
                c+=1
    if c>2:
        print(i)

