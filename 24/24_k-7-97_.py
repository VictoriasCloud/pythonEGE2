s=open("k7-97.txt").readline()
tek_len=0
max_len=0
for i in s:
    if i=="C":
        tek_len+=1
        if tek_len>max_len:
            max_len=tek_len
    else:
        tek_len=0
print(max_len)
#URA!!!
