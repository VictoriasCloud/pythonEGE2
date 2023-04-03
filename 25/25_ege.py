a=120115
b=120200
max_count=0
max_x=0
for x in range(a, b+1):
    count=0
    for i in range(1, x+1):
        if x%i==0:
            count+=1
    if count>=max_count:
        max_count=count
        max_x=x
print(max_count, max_x)

