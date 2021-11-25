# -- coding: utf-8 --
def f7():
    k = 0
    n = int(input('n: '))
    if n >= 0:
        while n != 0:
            x = int(input('n: '))
            if x > 0:
                if n < x:
                    k += 1
            elif x < 0:
                return print('n < 0')
            n = x
        print(k)
    else:
        print('n < 0')
f7()
