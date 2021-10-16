# -- coding: utf-8 --
def f4(s):
    print(s[s.find(' ') + 1:], s[:s.find(' ')])
f4(input('Строка: '))