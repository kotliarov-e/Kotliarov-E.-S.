# -- coding: utf-8 --
def f7():
    k = 0
    n = int(input('n: '))
    while n != 0:
        x = int(input('n: '))
        if n < x:
            k += 1
        n = x
    print(k)
f7()
