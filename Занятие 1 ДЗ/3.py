# -- coding: utf-8 --

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