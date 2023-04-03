a=[int(i) for i in open("18_.txt")]
c=1
maxim=-10000
for i in range(len(a)-1):
    if abs(int(a[i])-int(a[i+1]))<=10:
        c+=1
        maxim=max(maxim, a[i]+a[i+1])
print(maxim)
