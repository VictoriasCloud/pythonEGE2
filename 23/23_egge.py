def f(start, finish):
    if start==finish:
        return 1
    if start>finish:
        return 0
    else:
        return f(start+2, finish)+f(start*2,finish)+f(start+3, finish)
print(f(2, 11)*f(11, 22))
