# -- coding: utf-8 --
def f5(s):
    if s.count('f') == 1:
        print(s.find('f'))
    elif s.count('f') > 1:
        print(s.find('f'), s.rfind('f'))
    else:
        return ''
f5(input('Строка: '))