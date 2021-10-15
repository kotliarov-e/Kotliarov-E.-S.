# -- coding: utf-8 --
def n3(a, b):
    if a > b:
        for i in range(a, b - 1, -1):
            if i % 2 != 0:
                print(i, end=' ')
n3(int(input('a: ')), int(input('b: ')))
