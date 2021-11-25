# -- coding: utf-8 --
def f3():
    N = int(input('N = '))
    i = 1
    k = 0
    while i <= (N // 2):
        i *= 2
        k += 1
    print(k, i)
f3()