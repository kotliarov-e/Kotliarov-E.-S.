# -- coding: utf-8 --
def f8(s):
    print((s[s.find('h') + 1:s.rfind('h'):])[::-1])
f8(input('Строка: '))