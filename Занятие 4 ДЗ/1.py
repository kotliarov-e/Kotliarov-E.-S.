# -- coding: utf-8 --
def f(s):
    print(s[2])
    print(s[-2])
    print(s[:5:])
    print(s[:-2:])
    print(s[::2])
    print(s[1::2])
    print(s[::-1])
    print(s[::-2])
    print(len(s))
f(input('Строка: '))