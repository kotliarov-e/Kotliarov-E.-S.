# -- coding: utf-8 --
def f6(s):
    if s.count('f') > 1:
        print(s.find('f', s.find('f') + 1))
    elif s.count('f') == 1:
        print('-1')
    else:
        print('-2')
f6(input('Строка: '))