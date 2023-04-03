A=open("k8.txt").readline()
print(A)
max_len=1
tek_len=1
a=[A[0]]
for i in range(1, len(A)):
    if A[i]==A[i-1]:
        tek_len+=1
        if tek_len==max_len:
            a.append(A[i])
        elif tek_len>max_len:
            max_len=tek_len
            a=[A[i]]
    else:
        tek_len=1
for a1 in a:
    print(a1, max_len)
