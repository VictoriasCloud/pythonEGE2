A=open("ii5_0.txt").readline()
k=0
k_max=0
d=0
for i in A:
    if (i =="D" and d<1) or i!="D":
        if i!="D":
            k+=1
            if k>=k_max:
                k_max=k
        if i=="D" and d<1:
            d+=1
            k+=1
            if k>=k_max:
                k_max=k
    else:
        k=0
        d=0
print(k_max)



