# -- coding: utf-8 --
def n10(n, k):
    F1, F2 = 1, 1
    m = [F1, F2]
    for i in range(2, n):
        F1, F2 = F2, F1 + F2
        m.append(F2)
    print(sum(m[k-1:]))     #я не придумал другого способа
n10(int(input('Кол-во чисел из ряда: ')), int(input('Номер с которого начать: ')))
