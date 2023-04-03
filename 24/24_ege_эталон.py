A=open("24 (1).txt").readline()
k=1
k_max=1
for i in range(len(A)-1):
    if A[i]!=A[i-1]:
        k+=1
        if k>k_max:
            k_max=k
    else:
        k=1
print(k_max)

