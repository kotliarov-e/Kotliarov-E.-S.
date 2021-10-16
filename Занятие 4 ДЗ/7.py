# -- coding: utf-8 --
def f7(s):
    print(s.replace(s[s.find('h'):s.rfind('h') + 1], ''))
f7(input('Строка: '))