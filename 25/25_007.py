from itertools import*
s="0123456789"
count=0
d=[]
for i in range(4):
    for j in product(s, repeat=i):
        word=int('123'+''.join(j)+"67")
        if word%123==0:
            print(word, word//123)
