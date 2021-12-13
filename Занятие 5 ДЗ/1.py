# -- coding: utf-8 --
def f1():
    N = int(input('N = '))
    k = 1
    while k**2 <= N:
        print(k**2, end=' ')
        k += 1
f1()
