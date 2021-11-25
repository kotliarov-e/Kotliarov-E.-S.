# -- coding: utf-8 --
def f2():
    N = int(input('N = '))
    d = 2
    while N % d != 0:
        d += 1
    print(d)
f2()