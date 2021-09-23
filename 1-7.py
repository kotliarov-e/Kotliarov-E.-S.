# -- coding: utf-8 --

# №1
print("Курс программирования начался")

# №2
print(16823 * 12302 % 3092)

# №3
def f(name, age):
    if ((age > 0) and (age < 75)):    # a)
        if (name != 'Иван'):          # b)
            if (age >= 16):
                return "Поздравляем вы поступили в ВГУИТ"
            elif (age < 16):
                ost = 16 - age
                return f"Сначало нужно окончить школу!" \
                       f" \nВам осталось учиться ещё {ost} года(лет) в школе"    # c)
        else:
            return 'Вас зовут Иван'
    else:
        return 'Слишком большой возраст'
print(f(str(input("Имя: ")), int(input("Возраст: "))))

# №4
seconds = int(input("Введите количество секунд: "))
print(f"{seconds} секунд это:", seconds // 86400, ':', round(seconds / 3600, 2), ':', round(seconds / 60, 2))

# №5
n = int(input("Введите число n: "))
print(n + n**2 + n**3 + n**4 + n**5)

# №6
x, y = input("x: "), input("y: ")
a = x, y = y, x
print(' '.join(a))

# №7
number = int(input('Введите число: '))
if number % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')
