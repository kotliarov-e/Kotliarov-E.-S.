def f10():
    def fib(n): # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
        if n < 2:
            return n
        else:
            return (fib(n - 1) + fib(n - 2))
    k = int(input('Кол-во чисел: '))
    n = int(input('С какого эл-та начать: '))
    s = 0
    for i in range(k):
        n1 = fib(n)
        s += n1
        n += 1
    print('Сумма:', s)
f10()
