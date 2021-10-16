# -- coding: utf-8 --
def f3(s):
    s1 = (s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
    print(s1)
f3(input('Строка: '))