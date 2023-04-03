A=open("24_rrr.txt").readline()
k=0
k_max=0
for i in range(0, len(A)-1):
    if ((A[i] and A[i+1]) in "AB") and A[i]!=A[i+1] :
        k+=1
        if k>k_max:
            k_max=k
    else:
        if A[i]=="B":
            k=1
        else:
            k=0
print(k, k_max)
