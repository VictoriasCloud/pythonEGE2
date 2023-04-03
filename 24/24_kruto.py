A=open("24 (1).txt").readline()
#print(A)
max_len=1
tek_len=1
a=A[0]
for i in range(len(A)-1):
    if A[i]==A[i-1]:
        tek_len+=1
        if tek_len>max_len:
            max_len=tek_len
            a=A[i]
    else:
        tek_len=1
print(a, max_len)
