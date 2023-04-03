s=open("24_Cho_takoe.txt").readline()
tl=0
ml=0
for i in range(1, len(s)):
    if s[i]=="C":
        tl+=1
        if tl > ml:
            ml=tl
    else:
        tl=0
print(ml)

