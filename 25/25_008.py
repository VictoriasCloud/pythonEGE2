#15*12?
for x in range(1001, 550000):
    if x%26==0 and str(x)[:2]=="15" and str(x)[-3:-1]=="12":
        print(x, x//26)
