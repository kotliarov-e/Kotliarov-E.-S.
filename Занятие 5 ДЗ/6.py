# -- coding: utf-8 --
def f6():
    k = 0
    s = 0
    n = int(input('n: '))
    while n > 0:
        s += n
        k += 1
        n = int(input('n: '))
    print(s / k)
f6()
