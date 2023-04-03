def f(start, finish):
    if start==finish or start==3:
        return 1
    if start>finish:
        return 0
    else:
        return f(start+1,finish)+f(start+2, finish)+f(start*3, finish)
print(f(2,8)*f(8,10)*f(10,12))

