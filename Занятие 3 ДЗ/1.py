# -- coding: utf-8 --
def n1(a, b):
    if a <= b:
        for i in range(a, b + 1):
            print(i, end=' ')
n1(int(input('a: ')), int(input('b: ')))

