# -- coding: utf-8 --
def n5(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i**3
    print(summa)
n5(int(input('n: ')))
