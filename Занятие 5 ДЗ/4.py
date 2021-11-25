# -- coding: utf-8 --
def f4():
    x = int(input('Первый день: '))
    y = int(input('Цель: '))
    k = 0
    while x <= y:
        x *= 1.10
        k += 1
    print('Дней для достижения цели:', k + 1)
f4()