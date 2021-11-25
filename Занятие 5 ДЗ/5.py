# -- coding: utf-8 --
def f5():
    k = 0
    n = int(input('n: '))
    if n >= 0:
        while n != 0:
            n = int(input('n: '))
            if n >= 0:
                k += 1
            else:
                return print('n < 0')
        print(k)
    else:
        print('n < 0')
f5()
f5()