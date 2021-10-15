# -- coding: utf-8 --
def n9(n):
    summa = 0
    F1, F2 = 1, 1
    for i in range(2, n):
        F1, F2 = F2, F1 + F2
    print(f'Сумма {n} элементов:', F2)
n9(int(input('Кол-во чисел из ряда: ')))