# -- coding: utf-8 --
def n2(a, b):
    if a < b:
        for i in range(a, b + 1):
            print(i, end=' ')
    else:
        for i in range(a, b - 1, -1):
            print(i, end=' ')
n2(int(input('a: ')), int(input('b: ')))