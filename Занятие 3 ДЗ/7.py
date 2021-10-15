# -- coding: utf-8 --
def n7(n):
    f = 1
    s = 0
    for i in range(1, n + 1):
        f *= i
        s += f
    print('Сумма =', s)
n7(int(input('n: ')))
