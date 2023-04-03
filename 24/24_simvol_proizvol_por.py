s=open("24_Cho_takoe.txt").readline()
max_len=0
tek_len=0
for i in range(1, len(s)):
    if s[i] in "ABC":
        tek_len+=1
        if tek_len>max_len:
            max_len=tek_len
    else:
        tek_len=0
print(max_len)
#hz
