s=open('24_Cho_takoe.txt').readline()
#print(s)
k=0
len_k=3
for i in range(len(s)-2):
    if s[i] in "BCD":
        if (s[i+1] in "BDE") and (s[i+1]!=s[i]):
            if (s[i+2] in "BCE") and (s[i+1]!=s[i+2]):
                k+=1
print(k)



