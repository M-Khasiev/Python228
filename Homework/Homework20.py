# import re
print("Создайте пароль. От 6 до 18 символов.")
print("Валидные символы: цифры, английские буквы, дефис, собачка и подчеркивание.")
s = input("Введите пароль: ")


def func_password(a):
    lst = re.findall(r'^[A-z\d@_-]{6,18}$', a)
    if lst:
        print("Создание пароля прошло успешно!", "\nВаш пароль:", lst[0])
    else:
        print("Вы создали невалидный пароль!")


func_password(s)
