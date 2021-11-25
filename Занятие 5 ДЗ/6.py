# -- coding: utf-8 --
def f6():
    k = 1
    s = 0
    n = int(input('n: '))
    while n != 0:
        s += n
        n = int(input('n: '))
        if n > 0:
            k += 1
        elif n < 0:
            return print('n < 0')
    print(s / k)
f6()