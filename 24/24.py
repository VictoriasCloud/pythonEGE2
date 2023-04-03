A=open('24_Cho_takoe.txt').readline()
k=1
k_max=1
for i in range(1, len(A)):
    if A[i]==A[i-1]=="X":
        k=k+1
        k_max=max(k, k_max)
    else:
        k=1
print(k_max)
