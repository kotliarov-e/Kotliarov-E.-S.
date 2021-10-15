# -- coding: utf-8 --
def n4(N):
    summa = 0
    k = 1
    for i in range(N):
        summa += int(input(f'Число {k}: '))
        k += 1
    print('Сумма: ', summa)
n4(int(input('Кол-во чисел: ')))

