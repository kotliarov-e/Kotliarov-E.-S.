# -- coding: utf-8 --
def n6(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f'Факториал {n} =', f)
n6(int(input('n: ')))
