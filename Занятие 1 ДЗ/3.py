# -- coding: utf-8 --

# №4
seconds = int(input("Введите количество секунд: "))
sec = (str(seconds // 86400), str(round(seconds / 3600, 2)), str(round(seconds / 60, 2)), str(seconds))
print(f"{seconds} секунд это:", sec)