# -- coding: utf-8 --
def f9(s, symboldelete):
    s = s.replace(symboldelete, '')
    print(s)
f9(input('Строка: '), input('Удалить символ: '))