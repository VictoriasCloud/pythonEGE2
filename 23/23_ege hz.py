q = 0
for n in range(1, 10000):
    for i in range(1, n):
        if n % i == 0:
            q = i
            if q==17:
                print(n)

