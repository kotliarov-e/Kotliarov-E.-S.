# -- coding: utf-8 --
def f8():
    p = -1
    k = 0
    m = 0
    n = int(input('n: '))
    while n != 0:
        if p == n:
            k += 1
        else:
            p = n
            m = max(m, k)
            k = 1
        n = int(input('n: '))
    m = max(m, k)
    print(m)
f8()