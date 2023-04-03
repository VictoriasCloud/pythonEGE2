count=0
for n in range(3532000, 3532160+1):
    n_del=0
    for d in range(1, n+1):
        print(n,d)
        if n%d==0:
            n_del+=1
        if n_del>2:
            break
    if n_del==2:
        count+=1
        #print(count, n)

