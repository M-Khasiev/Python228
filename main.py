# name = "John"
# print("Hello,", name)
# age = 20
# print(age)
# print(type(name))
# print(type(age))
# a = 5
# b = 4
# a = b
# print(id(a))  # id
# print(id(b))
import re
# a = b = c = 1
# print(a, b, c)

# a,b,c = 5, "Hello", 9.2
# print(a, b, c)

# name_new = "Bob"
# print(name_new)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "Hello"
# print(type(a))
# a = 3
# print(type(a))

# name = "John"
# age = 20
# print("Меня зовут: " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут: ", name, ". Мне " , age, " лет")

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)

# res = a
# a = b
# b = res
# a, b = b, a

# print(" a:", a)
# print("b:", b)

# print("Строка \
# символов")
# print('Строка '
#       'символов')
# print("Документ \"script.py\" находится \rпо заданному пути \n\r\tC:\\\Python\\project")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 2)
# print("*" * 40)


# print(23124342949542569341923421454)
# print(2.23124342949542529341923421454)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(7 / 2)  # 3.5
# print(6 // 2)  # 3
# print(7 // 2)  # 3 целочисленное деление , отбрасывает то что после запятой (дробная часть)
# print(7 % 2)
# print(7 ** 2)


# classWork 2

# num = 10
# num += 5
# print(num)

# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# c = num % 10
# print(c)
# num = num // 10
# print(num)
# d = num % 10
# print(d)
# e = a * 1000 + b * 100 + c * 10 + d
# print(e)


# num1 = 4321
# print(num1)
# res = (num1 % 10) * 1000
# print(res)
# num1 = num1 // 10
# res += (num1 % 10) * 100
# print(res)
# num1 = num1 // 10
# res += (num1 % 10) * 10
# num1 = num1 // 10
# res += num1
# print(res)


# int() - преобразовывает к целочисленному типу данных
# float() - преобразовывает к вещественному типу данных
# str() - преобразовывает к строковому типу данных
# bool() - преобразовывает к булеву типу данных
# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
#
# print(int(3.8))
# print(round(3.8))
# print(round(3.895, 2)) # 5 и выше в большую сторону

# a = 5 / 3
# print(round(a, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(int(c))
# d = round(c)
# print(type(d))

# a = 1
# b = 2
# print("a:", a, "\nb:", b)
# print("a:", a)
# print("b:", b)

# name = "John"
# age = 23
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут" + name + ". Мне" + str(age) + "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end=" ")
# print("Я учу Python.", end="\n\n")
# print("qqq")
# print(5 + 2, 3 + 4, sep="|")


# print("*** Ваши данные ***")
# name = input("Ваше Имя: ") # Input - Функция для ввода данных. Значения по умолчанию дать нельзя.
# city = input("Ваш Город: ")
# print(name, city)


# num = int(input("Введите число: "))
# num2 = int(input("Введите степень: "))
# num3 = num ** num2
# print("Число " + str(num) + " в степени " + str(num2) + " равна: " + str(num3))
# print("Число ", num, " в степени ", num2, " равна: ", num3)

# num = int(input("Введите 1 число: "))
# num2 = int(input("Введите 2 число: "))
# num3 = int(input("Введите 3 число: "))
# num4 = int(input("Введите 4 число: "))
#
# res = num + num2
# res2 = num3 + num4
# cel = res / res2
# print("Результат: ", round(cel, 2))


# a = True
# b = False
# print(a + 5) # 1 + 5
# print(a * 5) # 0 * 5

# False = "", 0, False, None
# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(0))  # False
# print(bool(0.0))  # False
# print(bool(1))  # True
# print(bool(-1))  # True
# print(bool(0.5))  # True
# print(bool(False))  # False
# print(bool(None))  # False


# test = None
# print(test)  # None = присвоение первоначального значения
# test = 5
# print(test)  # 5

# print(7 == 7)  # True
# print(2 + 5 != 7)  # False
# print(8 > 7)  # True
# print(8 < 7)  # False
# print(8 <= 8)  # True
# print("привет" == "Привет")  # False = Символы разные

# print(2 < 4 < 9)  # True
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(3 * 3 <= 7 >= 2)  # False


# a = 18
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False


#  And - "И"
# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)


# Or - "Или"
# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)


# Not - "Не равен"
# print(not 9 - 7)
# print(not 7 - 7)


# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)


# age = int(input("Укажите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ на сайт запрещен")


# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# a = input("Введите первую сторону")
# b = input("Введите вторую сторону")
# c = input("Введите третью сторону")
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a == b or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# m = int(input("Введите номер месяца: "))
# # if (m >= 1) and (m <= 12):
# if 1 <= m <= 12:
#     if m == 1 or m == 2 or m == 12:
#         print("Зима")
#     if m == 3 or m == 4 or m == 5:
#         print("Весна")
#     if m == 6 or m == 7 or m == 8:
#         print("Лето")
#     if m == 9 or m == 10 or m == 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")


# Classwork 3

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5: # day >= 1 and day <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
#
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
#
# else:
#     print("Такого дня недели не существует!")


# v = int(input("Введите количество ворон: "))
# if 0 <= v <= 9:
#     print("На ветке ", end="")
#     if v == 1:
#         print(v, "ворона")
#     elif 2 <= v <= 4:
#         print(v, "вороны")
#     else:
#         print(v, "ворон")
# else:
#     print("Ошибка ввода данных")


# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= kop <= 10 or 15 <= kop <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Некорректный ввод данных!")


# Тернарное выражение (аналог Тернарного оператора в JS)

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 20, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")
#
# if a == b:
#     print("a == b")
# else:
#     if a > b:
#         print("a > b")
#     else:
#         print("b < a")

# Вариант №1 Мой
# a, b = 2, 0
# print("На ноль делить нельзя" if b == 0 else a / b)

# Вариант №2 Чужой
# print(a / b if b != 0 else "На ноль делить нельзя")


# Исключения
# print("Код выше")
# a = 5
# b = 0
# print(a / b)
# print("Код далее")

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя  делить на ноль")
# else:  # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# a = input("Введите первое число: ")  # "9"
# b = input("Введите второе число: ")  # "a"
# try:
#     a = int(a)  # 9
#     b = int(b)  # 'a' !!!
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)  # '9' + 'a'


# i = 10
# while i > 0:
#     print("i = ", i)
#     i -= 1  # i = i - 1

# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         print("i = ", i)
#     i += 1

# n = int(input("Укажите количество символов: ")) # 7
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1


# n = int(input("Укажите количество символов: ")) # 7
# while n > 0:
#     print("*", end="")
#     n -= 1


# Classwork 4

# n = input("Введите целое число: ")

# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:  # True - бесконечный цикл
#     if i == 3:
#         i += 1  # здесь обязательно должно быть прибавление счетчика
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")


# while True:
#     n = int(input("Введите положительное число"))
#     if n > 0:
#         break

# res = 1  # При умножении всегда ставим единицу (1)
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res = res * n
#
# print("Результат:", res)


# res = 0
# while res < 10:
#     if res == 5:
#         break
#     print(res)
#     res += 1
# else:
#     print("Цикл окончен, res = ", res)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 20:
#         if j % 2 != 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# Цикл For

# for element in collection:
#     print(element)

# for i in "Hello!":
#     print(i)

# i = 1
# for color in 'red', 'orange', 'yellow', 2, 0.3:
#     print(i,"color:", color, type(color))
#     i += 1

# for i in range(n):
#     Тело цикла

# range(start, stop, step)

# for i in range(100, -101, -10):
#     print(i, end=" ")

# for i in range(2, 9, 3)
# print()
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 3

# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if a % i:
#         print(i, end=" ")

# for i in range(10, 100):  # от 10 по 99
#     if i // 10 == i % 10: # if i % 11 = 0:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---")

# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
#
# for i in range(b):
#     for j in range(a):
#         if i == 0 or j == 0 or i == a - 1 or j == b - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# Classwork 5

# a = [i * 2 for i in "Hello"]
# print(a)
#
# for i in "Hello":
#     print(i * 2)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# print([i for i in range(30) if i % 2 == 0])


# Списки (list) (Массив JS)

# num = [8, 3, "one", 3.2, [1, 2, 3]]
# print(num)
# print(type(num))
# print(num[1])
# print(num[-1][1])
# print(num[-2])
# # print(num[5])
# # print(num[-6])
# num[2] = 256
# print(num)
# num[1] += 100
# num[-1] = 2
# # num[5] += 4
# print(num)

# Длина списка
# num = [8, 3, "one", 3.2, [1, 2, 3]]
# print("Длина списка:", len(num))


# s = []
# print(type(s))
# b = list("Hello")
# print(b)

# s = [5, 1] * 6
# print(s)

# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
#
# if n == n2:
#     print("Списки равны")
# else:
#     print("Списки разные")


# for в одну строку используется для генерации списка
# Синтаксис: [выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = a + b
# print(c)
# d = c * 2  # только на целочисленное значение
# print(d)


# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("Кол-во эл-тов")))]
# print(a)

# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):  # i - индексы
#     # print(i)
#     print(a[i], end=" ")
# print()
# for i in a:  # i - элементы
#     print(i, end=" ")


# lst = ['один', 'два', 'три']
# for i in lst:
#     print(i, end=" ")
# print()
# for i in range(len(lst)):
#     print(lst[i], end=" ")

# sum1 = 0
# n = [0] * int(input("Введите количество элементов: "))
# for i in range(len(n)):
#     n[i] = int(input("-> "))
#     if n[i] < 0:
#         sum1 += n[i]
# print(sum1)


# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных элементов:", k)
# print("Количество нечетных элементов:", s)

# sum1 = 0
# count = 0
# n = [0] * int(input("Введите количество элементов: "))
# for i in range(len(n)):
#     n[i] = int(input("-> "))
#     if n[i] != 0:
#         count += 1
#     sum1 += n[i]
# print("Среднее арифметическое:", sum1 / count)

# n = [0] * int(input("Введите количество элементов: "))
# for i in range(len(n)):
#     n[i] = int(input("-> "))
#
# for i in range(len(n)):
#     if i % 2 == 0:
#         print(n[i], end=" ")

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)


# Classwork 6

# Срезы

# список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[1::2])
# print(s[::-1])
# print(s[-2:2:-1])
# print(s[1:4:-1])
# print(s[10:20])


# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[-3:1:-1])
# print(s[2:5])


# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = 30
# print(s)

# Методы списков
# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([9, 8, 7])  # добавляет множество элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, 100)  # добавляет заданное значение (второй параметр) по указанному индексу (первый параметр)
# print(s)

# s1 = []
# s1.extend([1 * 1, 2 * 2, 3 * 3, 4 * 4, 5 * 5, 6 * 6, 7 * 7, 8 * 8, 9 * 9, 10 * 10])
# print(s1)
#
# s = []
# for i in range(1, 11):
#     s.extend([i ** 2])
# print(s)

# lst = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
# #     # lst.append(x)
# #     # lst.extend([x])
#     lst.insert(-1, x)
# print(lst)  # [2,3,1]


# n = int(input('Введите количество элементов списка: '))
# i = 0
# lst = []
# while i < n:
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
#     i += 1
# print(lst)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3, 5, 6, 7]
# b = [11, 22, 33,]
# c = []
# if len(b) > len(a):
#     for i in range(int(len(a))):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):     # range (3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [1, 20, 0, 30, 4, 5, 6, 7, 9, 3]
# s[4:] = []
# s[2:6] = []
# if 20 in s:  # Если 20 есть в списке s , то будет True и сработает if
#     s.remove(0)  # удаляет элемент по значению (не по индексу), первое совпадение,остальные не будет
# i = 0
# while i in s:
#     s.remove(i)
# print(s)

# last = s.pop()  # удаляет последний элемент из списка и возвращает удаляемый элемент
# print(last)
# print(s)
# second = s.pop(0)  # удаляет элемент по индексу
# print(s)
# print(second)

# s.clear()  # очищает список
# del s[:]
# del s[2]  # удаляет по индексу
# print(s)


# n = [(int(input("-> "))) for i in range(int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс: "))
# del s[k]
# n.pop(k)
# print(n)


# Classwork 7

# print(dir(list))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 9, 3]
# num = s.count(0)  # Считает количество заданных значений в списке
# print(num)
# ind = s.index(0, 3, -1)  # возвращает положение первого индекса с заданным значением (находит первый и останавливается
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # возвращает копию списка, расположенную по другому адресу
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print("a =", a)
# print("b =", b)
# print("s_copy =", s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 9, 3]
# s.reverse()  # (Возвращает None) Изменяет список в противоположную сторону (разворачивает наоборот)
# print(s)
#
# # s.sort()  # Сортирует список по возрастанию (со строками работает отдельно), изменяет исходный список
# s.sort(reverse=True)  # reverse=True - сортировка по убыванию
# print(s)
#
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)

# srt = sorted(s)  # Делает дубликат списка в отсортированном виде, но исходный не изменяет
# print(srt)
# print(s)
# print(id(srt))
# print(id(s))


# Генерация случайных данных

# import random as r
# from random import randint, randrange


# import random
# print(random.random())
# print(random.randint(0, 9))  # от 0 по 9 (включительно)
# print(random.randrange(0, 10, 2))


# from random import *

# print(randint(0, 9))  # от 0 по 9 (включительно)
# print(randrange(0, 10, 2))
# print(uniform(10.5, 25.5))  # генерирует случайное вещественное число
# print(round(uniform(10.5, 25.5), 2))  # Округление чисел
#
# s = [55, 66, 77, 88, 99, 20, 30, 80, 90]
# print(choice(s))  # Возвращает одно значение из списка, любого типа данных
# print(choices(s, k=5))  # Возвращает заданное количество любых чисел( количество случайных элементов)
# print(s)
# shuffle(s)  # Перемешивает элементы списка случайным образом
# print(s)
#
# mas = [randint(0, 100) for i in range(10)]
# print(mas)


# lst = [5, 3, 2, 4, 1]
# # lst = ['s', 'a', 'r']
# print(len(lst))
# print(sum(lst))  # только с числовыми значениями (суммирует элементы списка)
# print(max(lst))
# print(min(lst))


# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# print("Max: ", max(mas))
# mas.insert(0, max(mas))
# print(mas)
#
# lst = [randint(0,100) for i in range(10)]
# print(lst)
# l = lst.pop(lst.index(max(lst)))
# lst.insert(0, l)
# print(lst)

# mas = [randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)


# mas = [randint(1, 100) for i in range(10)]
# print(mas)
# a = min(mas)
# print("Min: ", a)
# l = mas.index(a)
# print("Index min: ", l)
# del mas[:l]
# print(mas)


# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)
#
# lst = []
# # if len(lst) == 0:
# print(bool(lst))
# if not lst:
#     print("Список пустой")


# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Первый список: ", b)
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
#
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# n = int(input("Размер списка: "))  # 6
# s = []
# while len(s) < n:
#     k = randint(1, n)  # от 1 по 6
#     if k not in s:
#         s.append(k)
# print(s)


#  Classwork 8

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]

# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()
# n = int(input("Ширина "))
# n2 = int(input("Высота "))
# q = [[0 for x in row]for row in m]
# q = [[0 for x in range(5)]for row in range(3)]
# for row in q:
#     # print(row)
#     for x in row:
#         print(x, end='\t\t')
#     print()

from random import *
# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matr = [[randint(0, 100) for i in range(m)] for j in range(n)]
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()
# a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
# for x, y, z in a:
#     print(x, "+", y, "+", z, "=", x + 4)

# w, h = 6, 6
# matrix = [[randint(0, 10) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for col in range(len(matrix[row])):
#             print(matrix[row + 1][col], end='\t')
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end='\t')
#         print()

# import math

# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)
# print(num2)
# num3 = math.floor(3.8)
# print(num3)
# print(round(math.pi, 2))
#
# radius = 9
# print("Площадь окружности с радиусом", radius, "=>", math.pi * (radius ** 2))
# print(round(2 * math.pi * radius, 2))

import time as t


# second = t.time()
# print("Секунды с начала цифровой эпохи:", second)
# localtime = t.ctime()
# print(localtime)
# res = t.localtime(second)
# print(res)
# print(res.tm_year)
# print(t.strftime("Today is %B %d, %Y"))
# print(t.strftime("%m/%d/%Y, %H:%M:%S", t.localtime(999956565)))
#
#
# pause = 5
# print("Program start...")
# t.sleep(pause)
# print(pause, "seconds.")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# t.sleep(local_time)
# print(text)

# start = t.monotonic()
# t.sleep(5)
# finish = t.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(t.strftime("Сегодня: %B %d, %Y"))


#  Функция

# def hello(name, word):
#     print("Hello", name, 'Say', word)
#
#
# hello("Irina", 'hi')
# hello("Ivan", 'hello')

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 7
# m = 9
# get_sum(n, m)
# get_sum('abc', 'def')
# get_sum(2.5, 4.5)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end=" ")
#         else:
#             print(b, end=" ")
#
#
# symbol(9, '+', '-')
# print()
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))

# a = int(input("1 число "))
# b = int(input("2 число "))
#
#
# def sum_1(c, d):
#     if c > d:
#         return c - d
#     else:
#         return c + d
#
#
# print(sum_1(a, b))


#  Classwork 9

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:  #
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надёжный пароль")
# else:
#     print("Ненадёжный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 5))
# q = 2
# print(get_sum(1, 5, d=q))e


# def sum_s(a, b=20):
#     return a * b
#
#
# print(sum_s('+'))

# def digit_sum(n, even=True):  # 123
#     s = 0
#     while n > 0:
#         cur_digit = n % 10  # 3 2 1
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10  # 12  1
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")
# display_info("Igor", age=23)


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = 'Hello'
# b = 'Hello'
# print(a == b)
# print(a is b)

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# lt1[1] = 'Hello'
# print(lt1)
# print(id(lt1[1]))
# print(id(lt1))

# s = 'Hello'
# print(id(s))
# # s += 'Word'
# s = s + 'World'
# print(s)
# print(id(s))

# a = 5
# print(a)
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# s = "Hello"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))

# lt1 = [1, 2, 3]
# print(lt1)
# print(id(lt1))
# # lt1 = lt1[1:-1]
# lt1 = lt1 + [4, 5]
# # lt1 += [4, 5]
# print(lt1)
# print(id(lt1))


#  Кортеж (tuple)


# lst = [10, 20, 30]  # Список
# tpl = (10, 20, 30)  # Кортеж
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(type(a))
# print(a)
# b = tuple((1, 2, 3, 4, 5))
# print(type(b))

# c = tuple("Hello")
# print(c)

# t = (1,)
# print(t)
# print(type(t))

# b = tuple((1, 2, 3, 4, 5))
# print(b)
#
# print(b[3])
# print(b[1:3])
# print(id(b))
# print(id(b[3]))
# b[1] = 3  Нельзя

# s = tuple(int(input("-> ")) for i in range(3))
# print(s)


# s = input("Строка:")
# a = tuple(s)
# print(a)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100)for i in range(10)))


# mas = tuple(2 ** i for i in range(1, 13))
# print(type(mas))
# print(mas)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(type(t3))
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l'))
# print(t3.index('l', 4))

# for i in t3:
#     print(i, end=" ")

# from random import *


#  Classwork 10
# def ran(t, p):
#     return tuple(randint(t, p) for i in range(10))
#
#
# a = ran(0, 6)
# b = ran(-5, 0)
# print(a)
# print(b)
# c = a + b
# print(c)
# print('0 =', c.count(0))


# a = 12345
# s = str(a)
# lst = list(s)
# print(lst)


# t = (10, 11, [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# t[-1][0] = 'new'
# print(id(t[4]))
# t[4].append('hi')
# print(id(t[4]))
# print(t, id(t))


# def create_tuple(lst):
#     s = []
#     # for i in lst[::-1]:
#     #     if i not in s:
#     #         s.append(i)
#     [s. append(i) for i in reversed(lst) if i not in s]
#     return tuple(s)
#
#
# print(create_tuple([1, 2, 3, 3, 2]))
# print(create_tuple([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))


# tu = (1, 2, 3)
# # x = tu[0]
# # y = tu[1]
# # z = tu[2]
# x, y, z = tu  # распаковка кортежа
# print(x, y, z)
#
#
# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# h, v, n = user
# print(h)

# a = (1, 2, 3)
# # del a
# print(a)
# print(a, id(a))
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# print(tpl, id(tpl))


# countries = (
#     ('Германия', 89.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
# print(countries, end='\n\n')
# for country in countries:
#     # print(country)
#     countryName, countryPopulation, cities = country
#     print('\nСтрана:', countryName, 'Население страны =', countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print('\tГород:', cityName, 'население = ', cityPopulation)

#  Множество (set)

# s = {'banana', 'apple', 'orange', 'apple', 'banana'}
# print(type(s))
# print(s)
# print(len(s))
# c = ['hello', 'world']
# a = set(c)
# print(a)

# s = {x * x for x in range(10)}
# print(s)

# num = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# print(num)
# # num = set(num)
# # print(num)
# # num = list(num)
# num = list(set(num))
# print(num)


# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
#
# print(to_set("Обычная строка"))

# t = {'red', 'green', 'blue'}
# # print('green' not in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
#
# for i in r:
#     if i[1] == 'c':
#         # print('A' + i[1:] if i[0] == 'a' else 'B' + i[1:])
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

#  Classwork 11

# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# # a.remove('Tom')
# # print(a)
# user = 'Tom'
# if user in a:
#     a.remove(user)
# print(a)
#
# # b = {1, 8, 5, 2}
# # print(b)
#
# a.discard('Bob')
# print(a)
# a.pop()
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# print(c)
# a.update(b)
# a |= b
# print(a)
# c = a & b
# print(c)
# a &= b
# print(a)
# c = a - b
# print(c)
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
#
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)

# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# only = drawing ^ music
# print('Одно хобби: ', only)
#
# both = drawing & music
# print('Два кружка: ', both)
#
# drawing = drawing - both
# print('Кружок рисования: ', drawing)

# s = frozenset([1, 2, 3, 4, 5, 4])
# print(s)
# c = [0, 1, 2]
# s1 = frozenset(c)
# s2 = s - s1
# print(s1)
# print(s2)
# a = frozenset({'Hello', 'world'})
# print(a)


# Словари (dict)

# s = ['one', 'two']
# # print(s[0])
# d = {'1': 'one', 2: 'two'}
# # print(d['1'])
# # print(d[2])
# print(d)

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# a = [
#     ('igor@gmail.com', 'igor'),
#     ('irina@gmail.com', 'irina'),
#     ('anna@gmail.com', 'anna')
# ]
# d = dict(a)
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)

# d = {0: 'text', "one": 45, (1, 2.3): 'tuple', 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[True])
# print(d[(1, 2.3)])
# print(d[42][1])
# print('one' in d)
# print('two' in d)

# print(d.keys())
# if 'one' in d:
#     print("TRUE")
# if 'one' in d.keys():
#     print("TRUE")

# key = 2
#
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + str(key) + " нет в словаре")
#
# print(d)

# for key in d:
#     print(key, "->", d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for i in d:
#     res = res * d[i]
# print(res)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# a = {i: input("-> ") for i in range(1, 5)}
# print(a)
# b = int(input("Введите элемент который нужно исключить: "))
# if b in a:
#     del a[b]
#     print(a)
# else:
#     print("Такого элемента нет")

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны", country, ':', capitals[country])
#     else:
#         print("В базе нет страны с таким названием", country)


# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 4600]
# }
#
# for i in goods:
#     print(i, ')', goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         cnt = int(input("Количество: "))
#         goods[n][1] = cnt
#     else:
#         break
#
# for i in goods:
#     print(i, ')', goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")


# Classwork 12

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('e', 'False')
# print(value)
# print(d)
# item = d.items()
# print(item)
# key = d.keys()
# print(key)
# value = d.values()
# print(value)
#
# for i, j in d.items():
#     print(i, '-> ', j)

# d.clear()
# item = d.pop('b', 5)
# print(item)
# it = d.popitem()
# print(it)
# item = d.setdefault('e', 5)
# print(item)
# d.update([('a', 7), ('q', 9)])
# d.update({'a': 7, 'q': 9})

# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d['e'] = 7
# d2['b'] = 5
# print("D =", d)
# print("D2 =", d2)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# # print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")


# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# # a = {value: key for key, value in d.items()}
# a = {key: value for key, value in d.items() if value <= 2}
# print(a)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)

# a = {i: i * 5 for i in 'Hello'}
# print(a)

# value = int(input("-> "))
# lt = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1, 9)}
# print(a)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# list()
# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# value = list(figures.values())
# # value = list(figures.keys())
# # value = list(figures.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i  # 'one'
#     else:
#         d[s].append(i)
# print(d)

#  zip()

# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# b = [5, 9, 7, 4]
# print(list(zip(a, b)))
#
# print(list(zip(range(5), range(100))))

# a = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# b = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}

# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '-> ', v1)
#     print(k2, '-> ', v2)

# for (k1, v1), v2 in zip(a.items(), b.values()):
#     print(k1, '-> ', v1, v2)

# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)
# print(x)
# print(y)

# lt1 = [2, 1, 4, 3]
# lt2 = ['c', 'a', 'b', 'd']
# # a1 = list(zip(lt2, lt1))
# # print(a1)
# # a1.sort()
# a = sorted(zip(lt1, lt2))
# print(a)

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, cost, m in zip(total_sales, prod_cost, month):
#     res = sales - cost
#     print("Чистая прибыль в", m, '=', res)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'peper': 0.2, 'onion': 0.55}
# print({**one, **two})  # {'apple': 0.4, 'orange': 0.35, 'peper': 0.2, 'onion': 0.55}
#
# for k, v in {**one, **two}.items():
#     print(k, '-> ', v)


#  Classwork 13

# en = ['red', 'green', 'blue']
# j = 1
# for i in en:
#     print(j, '-й цвет: ', i, sep='')
#     j += 1

# en = ['red', 'green', 'blue']
# for j, i in enumerate(en, 1):
#     print(j, '-й цвет: ', i, sep='')

# en = {0: 1, 1: 2, 2: 3}
#
# for j, i in enumerate(en, 1):
#     print(j, ": ", i, ' -> ', en[i], sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())


# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)


# def to_dict(*args):
#     a = {}
#     for i in args:
#         a[i] = i
#     return a
#
#
# print(to_dict(1, 2, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))


# def func(*num):
#     lst = []
#     a = sum(num) / len(num)
#     print(a)
#     for i in num:
#         if i < a:
#             lst.append(i)
#     return lst
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))


# def print_scores(stud, *scores):
#     print('*Student name:', stud)
#     for i in scores:
#         print(i, end=" ")
#     print()
#
#
# print_scores('John', 100, 95, 88, 92, 99)
# print_scores('Victor', 96, 20, 33, 92, 99)


# def func(*args):
#     res = []
#     for i in args:
#         res.append(int(str(i)[::-1]))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='Python'))

# def info(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print('*' * 20)
#
#
# info(firs_name='Irina', last_name='Petrova', age=22, phone=1234567890)
# info(firs_name='Igor', last_name='Ivanov', age=22, email='igor@gamil.com', country='Russia', phone=1234567890)

# def db(**kw):
#     my_dict.update(kw)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print('my_dict =', my_dict)


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)

# def func(a, *args, one=True, **kwargs):
#     return a, args, one, kwargs
#
#
# print(func(5, 9, 7, 8, 6, one=False, b=2, c=3, d=4))

# Область видимости (scope)

# for i in range(5):
#     a = 5
#     print(i)

# if True:
#     a = 5
# print('a =', a)

# name = 'Tom'
#
#
# def hi():
#     global name
#     name = 'Bob'
#     print('Hello', name)
#
#
# def bye():
#     print('Good bye', name)
#
#
#
# hi()
# bye()
# print(name)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))
# print(x)

# x = 3
#
# def func(a):
#     x = 2
#
#     def inner():
#         x = 5
#         print('x =', x)
#         return a + x
#
#     return inner()
# print(func(5))  # 7


# max = [1, 2, 3, 4, 5]
# print(sum(max))

# import builtins
#
# print(dir(builtins))


#  Classwork 14

# Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello", who)
#
#     inner_func()
#
#
# outer_func("world!")

# def func1():
#     a = 6  # 2
#
#     def func2(b):
#         a = 4  # 5
#         print("Сумма:", a + b)  # 6
#
#     print('a:', a)  # 3
#     func2(4)  # 4
#
#
# func1()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     print('global:', x)  # 25
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal:', a)  # 35
#
#     inner()
#     print(a)
#     t = a
#
# fn()
# z = x + t  # 25 + 30 = 55  ## 25 + 35 = 60
# print('results:', z)

# x = 5
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2,x =', x)
#
#     fn2()
#     print('fn1,x =', x)
#
#
# fn1()
# print('global x =', x)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
#
# res = increment(10)
# print(res)


# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# print(outer(5)(18))

# res = outer(5)
# print(res(10))
#
# print(res(2))
#
# res2 = outer(7)
# print(res2(5))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         nonlocal b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res = func('Moscow')
# print(res)
# res()
# res()
# res2 = func('Sochi')
# res2()
# res2()
# res()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())


#  Classwork 15

#  Анонимные функции, lambda-выражения

# (lambda x, y: print(x + y))(1, 2)
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))
#
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=3, c=3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))

# func = lambda *args: args
# print(func(1, 2, 3, 4))
# print(func('a', 'b'))

# func2 = lambda **kwargs: kwargs
# print(func2(a=5, b= 7, c= 10))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
#
# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))
#
# inc2 = (lambda n: (lambda x: x + n))
# print(type(inc2))
# # f2 = inc2(42)
# # print(f1(3))
# print(inc2(42)(3))
# print((lambda n: (lambda x: x + n))(42)(3))
#
# print((lambda n: (lambda x: (lambda y: n + x + y)))(2)(4)(6))

# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 10, 'c': 24}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1], reverse=True)
# lst.sort(key=func, reverse=True)
# print(lst)
# dict1 = dict(lst)
# print(dict1)

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# # players.sort(key=lambda item: item['last name'])
# # print(players)
#
# res = sorted(players, key=lambda item: item['raiting'])
# print(res)
#
# res = sorted(players, key=lambda item: item['last name'], reverse=True)
# print(res)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))
# print(abs(-3.2))


# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресенье')),
# }
#
# d[5]()

# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 13))

# minimum = (lambda a, b, c: a if a < b and a < c else b if b < c and b < c else c)
# print(minimum(9, 6, 32))


#  Функция map()

# def multiple(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(multiple, lst)))
# print(list(map(lambda t: t * 2, range(2, 10))))
# print(list(map(lambda t: t * 2, lst)))


# t = (2.88, -1.75, 100.55)
#
# # print(list(map(lambda x: str(x), t)))
# print(list(map(str, t)))
#
# a = ['2.88', '-1.75', '100.55']
# print(list(map(float, a)))

# areas = [3.578945, 5.789456, 7.456789, 56.4123456, 9.0123456, 32.7789456]
# print(list(map(round, areas, range(1, 7))))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = list(map(lambda x, y: [x, y], st, num))
# print(lst)
# tp = dict(lst)
# print(tp)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# lst = list(map(lambda x, y: x + y, l1, l2))
# print(lst)


#  Classwork 16

# Функция filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: 75 < s < 88, b))
# print(res)
# from random import *
#
# c = [randint(1, 40) for i in range(10)]
# print(c)
# res1 = list(filter(lambda s: 10 <= s <= 20, c))
# print(res1)

# a = [45, 55, 60, 37, 100, 105, 220]
# res1 = list(filter(lambda s: s % 15 == 0, a))
# print(res1)


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# #
# #
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()


# print()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("*" * 50)
#         fn(arg1, arg2)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name('Ирина', 'Лаврова')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 50)
#         fn(*args, **kwargs)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, end="\n\n")
# #
# #
# # @args_decorator
# # def hello():
# #     print("Hello")
# #
# #
# print_full_name('Ирина', 'Борис', 'Светлана', study="Javascript")
# print()
# print_full_name('Владимир', 'Екатерина', 'Виктор')
# print()
# hello()
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
# #
# #
# # @decor("Разность:", "-")
# # def sub(a, b):
# #     print(a - b)
# #
# #
# summa(5, 2)
# sub(5, 2)

# def decor(a):
#     def args_dec(fn):
#         def wrap(x):
#             return "Результат: " + str(a * fn(x))
#
#         return wrap
#
#     return args_dec
#
#
# @decor(3)
# def return_num(num):
#     return num * 2
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z='Hello! '):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2('Hello, ', 'World', '!'))
# print(typed_fn3('Hello, ', 'World', z=5))
# # print(typed_fn3('Hello, ', 'World', z='!!!'))


# Classwork 17

# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end="")
#             fn(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world2("Hi!")
# hello_world("world!")


# print(int('100', 2))
# print(int('7', 8))
# print(int('100', 16))
# print(int('100', 10))
# print(int('100'))

# print(bin(18))  # 0b10010  # 0B
# print(oct(18))  # 0o22    # 0O
# print(hex(18))  # 0x12    # 0X
#
# print(0b100 + 0o20)  # 4
# print(0o20)  # 16
# print(0x11 + 3)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)


# print(e * 3)
# print('y' in e)
# print(e[1])
# print(e[-1])
# print(e[:])
# print(e[2:-1])
# print(e[::-1])
# print(e[-1:0:-1])
# e = e[:3] + 't' + e[4:]
# print(e)

# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if i == c_old:
#             i = c_new
#         s2 += i
#     return s2
#
#
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования'
# st2 = change_char(st, 'N', 'P')
# print('st1 = ', st)
# print('st2 = ', st2)

# print(u'Привет')
# print(r'C:\file.txt')  # "сырые" строки # Не поддерживает символ слэш в конце
# print('C:\\file.txt')
# print(r'C:\\file.txt\\'[:-1])
# print(r'C:\\file.txt\\' + "\\")
# print('C:\\file.txt\\')

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="")
# print(f"Меня зовут {name}. Мне {age} лет")
#
# print(f"{2.356789}")
# print(f"{round(2.356789, 2)}")
# print(f"{2.356789:.2f}")

# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}"
#       f" - выражение")

# d = 74
# print(f"{{{{{d}}}}}")

# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + "\\" + file_name)


# s = """<div>
#     <a href="#">content</a>
# </div>
#
# """
# print(s)
#
# s1 = '''<div>
#     <a href="#">content</a>
# </div>
#
# '''
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(min.__doc__)


# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиус основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# Classwork 18

# print(ord('a'))
# print(ord('в'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in input("-> ")[:3]] if x not in arr]  # [:6:2] - пробелы
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# if a < b:
#     a, b = b, a
# while b <= a:
#     print(chr(b), "", end="")   # Мой вариант
#     b += 1

# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')


# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))  # 97
# print(ord('A'))  # 65


# from random import randint

# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# print(dir(str))

# s = " I am learning Python. hello, WORLD!"
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
#
# print(s.count("l", 3))  # подсчитывает кол-во вхождений подстроки в строку (подстрока - это то что мы ищем)
# print(s.find("Python1"))  # ищет в строке заданную подстроку, если она найдена , то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает "-1"

# a = "один два"
# b = a[:a.find(" ")]
# c = a[a.find(" ") + 1:]
# print(c)
# print(c + " " + b)

# a = 'ab12c59p7dq'
# b = []
# for i in a:
#     if i in '1234567890':
#         b.append(int(i))
#
# print(b)


# a = 'ab12c59p7dq'
# b = []
# for i in a:
#     if '1234567890'.find(i) != -1:
#         b.append(int(i))
#
# print(b)

# print(s)
# print(s.index("Python"))  # ищет в строке заданную подстроку, если она найдена , то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает исключение ValueError

# print(s.rfind('l'))  # Поиск спправа налево
# print(s.rindex('l'))

# a = s.find('h')
# print(a)
# b = s.rfind('h') + 1
# print(b)
# print(s[:a] + s[b:])

# print('abc123'.isalnum())  # определяет состоит ли строка из цифр или букв
# print('ABbc'.isalpha())  # определяет состоит ли строка из букв
# print('12345'.isdigit())  # определяет состоит ли строка из цифр
# print('abc2'.islower())  # определяет состоит ли строка из букв в нижнем регистре
# print('ABC3'.isupper())  # определяет состоит ли строка из букв в верхнем регистре


# print('py'.center(10, "-"))  # выравнивание строки по центру
# print(' py '.center(30, "*"))  # выравнивание строки по центру

# print("      py".lstrip())  # удаляют пробельные символы слева
# print("py      ".rstrip())  # удаляют пробельные символы справа
# print("   py   ".strip())   # удаляют пробельные символы и слева и справа
#
#
# print("https://www.python.org".lstrip('/:pths'))
# print("py.$$$;".rstrip(';$.'))
#
# print("https://www.python.org".lstrip('htps:/').rstrip("org."))
# print("https://www.python.org".strip('htps:/worg.'))
#
# print("https://www.python.org".strip(':/pthsworg').strip('.'))


# Classwork 19

# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace("Nython", "Python", 2))  # заменяет вхождение подстроки в строке


# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # a-b-c
#
# print("..".join(['1', '2']))  # обьединяет итерируемую последовательность (список, кортеж, другая строка) в одну строку
# # через заданный символ разделитель
#
#
# print(":".join('Hello'))


# print("Строка разделенная пробелами".split())  # делит строку на список из подстрок
# # print("Строка_разделенная_пробелами".split("_"))
# # print("Строка разделенная пробелами".split("а"))
#
# print("www.python.org.ru".split(".", 2))

# a = list(map(int, input("-> ").split()))
# print(a)
# print(a[0])

# a = input("Введите ФИО: ").split()
# print(a)
# print(a[0], " ", a[1][0], '.', a[2][0], '.', sep='')

# print("www.python.org.ru.".split(".", 2))
# print("www.python.org.ru.".rsplit(".", 2))
#
# print("www...python...org.".split("."))

# a = 'В строку заменить пробелы символов'.split(" ")
# print(a)
# print('*'.join(a))


# Регулярные выражения

# import re

#
# s = "Я ищу 9 совпадения в 2023 году. И я их найду в 2 счёта. 9578 1945"
# reg = r'\W'
# reg = r'[А-яё.]'   # [А-Яа-яЁё]
# reg = r'[12][09][0-9][0-9]'

# print(s.find(reg))
# print(re.findall(reg, s))  # ['я', 'я']  возвращает список, содержащий все совпадения
# print(re.findall('2', s))
#
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s))  # поиск по заданному шаблону в начале строки

# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону

# print(re.sub(reg, "!", s, 1, ))  #  поиск и замена

# print(re.findall(reg, s))

# s1 = "Ели{-ели}."
# pattern = r'[А-яё.\[\]{}-]'
# print(re.findall(pattern, s1))


# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты,  диапазоне от 00 до 59. 2021-06-15T01:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, s1))


# Classwork 20

# import re

# s = "Я ищу  совпадения в 2023 году. И я их найду в 2 счёта. 9578_194 5"
# reg = r'20*'

# print(re.findall(reg, s))

# Повторения
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - 0 или 1


# s1 = "Цифры: 7, +17, -42, 0013, 0.3"
# pattern = r'[+-]?\d+\.?\d*'
# # pattern = r'[+-]?\d+[.\d]*'
# print(re.findall(pattern, s1))


# s1 = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r'#.*', '', s1))
# print("Дата рождения:", re.sub(r'-', '.', re.sub(r'#.*', '', s1)))  # 05-03-1987

# Дата рождения: 05.03.1987


# s1 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# pattern = r'\w+\s*=[^;]+'
# pattern = r'\w+\s*=\s*\w+\s*[.\w]*'
# print(re.findall(pattern, s1))

# s1 = '12 сентября 2021 года'
# reg1 = r'\d{2,4}'
# print(re.findall(reg1, s1))

# s = "7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg2 = r'\+?7\d{10}'
# print(re.findall(reg2, s))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5"
# reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'

# print(re.findall(reg, s))

# def login(a):
#     return re.findall(r'^[\w!@#$-]{8,25}$', a)
#
#
# print(login('admin_admin'))
# print(login('admin_admin'))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# print(re.findall(r'[а-я]', 'Я я', re.IGNORECASE))


# text = """
# one Man
# two Women
# """
# print(re.findall(r'\w+$', text))
# print(re.findall(r'\w+$', text, re.MULTILINE))


# text = """
# one
# two
# """
#
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))


# Classwork 21
# import re

# print(re.findall("""
# [A-z.-]+  # part 1
# @         # поиск символа @
# [a-z_.-]+ # part 2
# """, 'test@mail.ru', re.VERBOSE))


# text = "hello world"
# print(re.findall(r'\w+', text, re.DEBUG))

# text = """Python,
# python
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))  # flags=re.IGNORECASE | re.MULTILINE

# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r'[\w.-]+@[\w.]+[\w]{2,3}'
# print(re.findall(reg, s))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.+?>", text))

# greedy - (жадный) (по умолчанию)
# lazy - (ленивый) (?)

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# t = "2324 786 22 4569"
# reg = r"\d{1,3}?"
# print(re.findall(reg, t))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg' title='подсказка'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'  # r'<img.*?>'  # r'<img[^>]*>'
# print(re.findall(reg, s))  # <img src='bg.jpg'>

# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r'\[\d+\]'
# print(re.findall(reg, s))

# s = 'Петр и Ольга отлично учатся!'
# reg = 'Петр|Виталий|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"int\s*=\s*\d+[.\w+]*|double\s*=\s*\d+[.\w+]*"
# reg = r"(int|double)\s*=\s*(\d+[.\w+]*)"
# print(re.findall(reg, s))


# () - группирующая скобка
# (?:) - группирующая скобка, не сохраняющая

# 192.168.255.255
# s = "127.0.0.1"
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS5, AI5"
# reg = r'(([A-z]+)(\d*))'
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# # reg = r'\s*[+*-]\s*'  # ['5', '7', '2', '4']
# reg = r'\s*([+*-])\s*'  # ['5', '+', '7', '*', '2', '-', '4']
# print(re.split(reg, s))


# s = "Я ищу  совпадения в 2023 году. И я их найду в 20000000000 счёта"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])
# print(re.search(reg, s).group(1))

# Classwork 22

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', replace_find, text))


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# print(re.findall(reg, s))

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))


# s = "Самолет прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.findall(reg, s))
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "google.com and google.ru and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


# Classwork 23

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))  # 5
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 15 (F)
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 9 6 7  ### 15 (F)
#
#
# print(to_str(253, 16))  # 769 // 10 = 76 // 10 = 7   ####  255 // 16 = 15


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']


# print(type(names[0]) == str)
# print(type(names[1]) == list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# def count(lst):
#     cnt = 0
#     for i in lst:
#         if isinstance(i, list):
#             cnt += count(i)
#         else:
#             cnt += 1
#     return cnt  # 1
#
#
# print(count(names))


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
#
#
# def union(s):
#     if not s:   # s == [] - список пустой
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print("Выпрямленный список:", union(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("   Hello\tWorld   "))


# def factorial_recursive(n):
#     if n == 1:
#         return
#     factorial_recursive(n - 1)
#     print(n)
#
# print(factorial_recursive(7))


# Classwork 24

# Файлы

# f = open('D:\\Python228\\text.txt', 'r')
# f = open('text.txt', 'r')
# print(f)
# print(*f)
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test.txt', 'r')
# print(f.readlines())
# f.close()


# f = open('test.txt', 'r')
# count = 0
# for line in f:
#     print(line, end='\r')
#     count += 1
# # print("count =", count)
# print(len(f.readlines()))
# # f.close()


# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld!')
# f.close()
#
# f = open('xyz.txt', 'a')
# # print(f.write('\nНовый текст'))
# lines = ['\nЛиния 1', '\nЛиния 2']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i - 1) + '\t' for i in range(1, 20)]
# print(lst)
# # f.writelines(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()

# f = open("text2.txt", "r")
# read_file = f.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'изменить строку в списке;\n':
#         read_file[i] = 'Hello world!\n'
# print(read_file)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_file)
# f.close()


# f = open('text3.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
#
# f = open('text3.txt', 'r')
# read_line = f.readlines()
# print(read_line)
# n = int(input("Введите индекс: "))
# if 0 <= n < len(read_line):
#     read_line.pop(n)
# else:
#     print('Такой строки нет')
# print(read_line)
# f.close()
#
#
# f = open('text3.txt', 'w')
# f.writelines(read_line)
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))  # 20
# print(f.seek(3))  # 3
# print(f.write("--new string--"))  # 14
# print(f.tell())  # 17
# f.close()

# f = open('text4.txt', 'wb')
# print(f.write(b"\nI am learning Python\n"))
# f.close()


# Classwork 25

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))

# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# lst = list(map(float, nums.split(' ')))
# print(lst)
# print(len(lst))
# print(sum(lst))


# file_name = 'res.txt'
#
#
# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words(file_name))


# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока'
#        '№10\n'
#
# with open("one.txt", "w") as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)


#  Модуль OS и OS.PATH

# import os

# print("Текущая директория: ", os.getcwd()) # C:\Python228
#
# print(os.listdir(".."))  # возвращает список директорий и файлов, находящихся в текущей директорий

# os.mkdir("folder")  # создает директорию по указанному пути

# os.makedirs("nested1/nested2/nested3")  # создает промежуточные директории и конечную, указанные в пути, если они не
# существует. Если конечная директория уже существует, то будет сгенерирована ошибка FileExistsError

# os.remove("text.txt")

# os.rename('nested1', 'test')  # переименовывает файл или директорию
# os.rename('res.txt', 'test/ress.txt')  # переименовывает файл или директорию, перемещает файлы в существующие
# директории (переместил файл)
# os.renames('text'.txt', 'test1/test1.txt') # переименовывает файл или директорию, создавая промежуточные директории (
# # переместил файл)

# os.rdmir("test1") # удаляет пустую директорию

# for root, dirs, files in os.walk('test'):  # Возвращает имена обьектов в виде дерева директорий. Для
#     # каждой директории возвращает кортеж (root - путь к директории, dirs - список директории, files - список файлов
#     print("Root:", root)
#     print("     Subdirs:", dirs)
#     print("         Files:", files)

# def remove_empty_dirs(root_true):
#     for root, dirs, files in os.walk(root_true):
#        if not os.listdir(root):
#            os.rmdir(root)
#            print(f"Директория {root} удалена.")
#
#
# remove_empty_dirs('test')


# OS PATH

# print(os.path.split(r'C:\Python228\test\nested1\nested2\nested3\giug.txt'))  # разбивает путь на кортеж (head, tail)
# # tail - последний компонент пути, head - все остальное
#
# print(os.path.dirname(r'C:\Python228\test\nested1\nested2\nested3\giug.txt'))  # возвращает имя директории ( + путь)
# print(os.path.basename(r'C:\Python228\test\nested1\nested2\nested3\giug.txt'))  # возвращает имя файла

# print(os.path.join('D:\pythonProject1', 'files', 'dir', 'three.txt'))


# dirs = ["Work/F1", "Work/F2/F21"]
#
# for d in dirs:
#     os.makedirs(d)
#
# files = {"Work": ['w.txt'],
#          "Work/F1": ['f11.txt', 'f12.txt', 'f13.txt'],
#          "Work/F2/F21": ['f211.txt', 'f212.txt']
#          }
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()


# file_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст для файла по пути {file}.")


# Classwork 26
# import os
# import time


# print(os.path.exists(r'C:\Python228\one.txt'))  # проверяет наличие файла или папки по указанному пути
# print(os.path.exists(r'C:\Python228\five.txt'))  # проверяет наличие файла или папки по указанному пути
# path = 'two.txt'
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу в секундах
# print(os.path.getctime(path))  # возвращает время создания файла
# print(os.path.getmtime(path))  # возвращает время последнего изменения файла
# print(os.path.getsize(path))  # размер файла в байтах

# size = round(os.path.getsize(path) / 1024, 2)
# print(size)
# a = os.path.getctime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))

# print(os.path.isfile(r'one.txt'))  # возвращает True, если путь является файлом
# print(os.path.isdir(r'Work'))  # возвращает True, если путь является директорий


# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1


# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))

# p1 = Point()
# p2 = Point()
# print("p1 =", p1.x)
# print("Point =", Point.x)
# # print(type(p1))
# p1.x = 100
# p2.x = 200
# print("p1 =", p1.x)
# print("p2 =", p2.x)
# print("Point =", Point.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y = 300
# print("p1 =", p1.y)
# print("p2 =", p2.y)
# print("Point =", Point.y)


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(Point.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print(self.__dict__)
#         # print("Метод set_coord")
#
#
# p1 = Point()
# print(p1.x)
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# p2 = Point()
# p2.x = 2
# p2.y = 7
# p2.set_coord()


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.country = country
#         self.phone = phone
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         if isinstance(name, str):
#             self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, bth):
#         self.birthday = bth
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1A')
# h1.print_info()
# h1.set_name("Алевтина")
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday("23.01.1987")
# print(h1.get_birthday())
# h1.print_info()


# Classwork 27

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника: ", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника: ", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dol")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print("Инициализатор")
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра", self.__class__.__name__)
#
#     def print_coord(self):
#         print(f"x: {self.x}, y: {self.y}")
#
#
# p1 = Point(5, 6)
# p1.print_coord()
# print(id(p1))
#
# p2 = Point(2, 7)
# p2.print_coord()
# print(id(p2))

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(7, 2)
# print(p2.count)
# p3 = Point(3, 4)
# print(p3.count)
# print(Point.count)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающий роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# print("Численность роботов:", Robot.k)


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами!")
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами!")
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами!")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 15
# print(p1.z)
# print(p1.__dict__)
# p1._Point__x = 111
# print(p1.get_coord())
# p1.set_coord(1, 2.3)
# print(p1.get_coord())
# print(p1.__dict__)
# p1.set_coord_x(8)
# print(p1.get_coord_x())
# p1.set_coord_y(9)
# print(p1.get_coord_y())
# p1.__x = 100
# p1.__y = 'abc'
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(p1.__dict__)


# Classwork 28

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):  # устанавливаем
#         print("Вызов __set_x")
#         self.__x = x
#
#     def __get_x(self):  # получаем
#         print("Вызов __get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):  # получаем __get_x
#         print("Вызов __get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):  # устанавливаем __set_x
#         print("Вызов __set_x")
#         self.__x = x
#
#     @x.deleter
#     def x(self):  # __del_x
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами!')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")


# class Person:
#     def __init__(self, name, skill):
#         self.__name = name
#         self.__skill = skill
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def skill(self):
#         return self.__skill
#
#     @skill.setter
#     def skill(self, s):
#         self.__skill = s
#
#     @skill.deleter
#     def skill(self):
#         del self.__skill
#
#
# p1 = Person("Viktor", 12)
# print(p1.name, p1.skill)
# p1.name = "Ann"
# p1.skill = 20
# print(p1.name, p1.skill)
# del p1.name
# del p1.skill
# print(p1.name, p1.skill)


# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(2, 7)
# print(Point.get_count())
# print(p1.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# c1 = Change()
# print(Change.inc(10), Change.dec(10))
# print(c1.inc(10), c1.dec(10))


# class Args:
#     @staticmethod
#     def max(*args):
#         res = 0
#         for i in args:
#             if i > res:
#                 res = i
#         return res
#
#     @staticmethod
#     def min(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def arf(a, b, c, d):
#         return (a + b + c + d) // 4
#
#     @staticmethod
#     def factorial(x):  # 5! = 1 * 2 * 3 * 4 * 5 = 120
#         first = 1
#         for i in range(1, x + 1):
#             first *= i
#         return first
#
#
# print(Args.max(3, 5, 7, 9))
# print(Args.min(3, 5, 7, 9))
# print(Args.arf(3, 5, 7, 9))
# print(Args.factorial(5))


# class Data:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# d = Data()
# string_date = d.from_string('23.10.2022')
# print(string_date.string_to_db())
# string_date1 = Data.from_string('21.12.2021')
# print(string_date1.string_to_db())


# Classwork 29

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счёт #{self.num} принадлежащий {self.surname} был закрыт.")
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счёта: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счёте")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И',
#         # 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or not 14 < old < 120:  # old < 14 or old > 120
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def olf(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Сидоров Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)

# Classwork 30

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# print(issubclass(Point, object))
# print(dir(Point))
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def __init__(self, *args, bg="yellow"):
#         super().__init__(*args)
#         self._background = bg
#
#     def draw_rect(self):
#         print(
#             f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self._background}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
#
#
# rect = Rect(Point(30, 40), Point(70, 80), "red", 10)
# rect.draw_rect()


#
# # DRY (Don't Repeat Yourself) - не повторяйся!!!

# Classwork 31

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f"{self.__color}"
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f"{self.__width}, {self.__height}, {self.color}"
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительное число")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительное число")
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect)
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = "red"
# rect.width = 5
# print(rect)
# print(rect.area())

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"=== Прямоугольник ===\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# class RectFonBorder(RectFon):
#     def __init__(self, width, height, background, border):
#         super().__init__(width, height, background)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape = Rect(100, 200)
# shape.show_rect()
# print()
#
# shape1 = RectFon(400, 300, "yellow")
# shape1.show_rect()
# print()
#
# shape2 = RectBorder(600, 500, '1px solid red')
# shape2.show_rect()
# print()
#
# shape3 = RectFonBorder(600, 500, 'yellow', '1px solid red')
# shape3.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


# Перегрузка методов

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(50, 60))
# line.draw_line()
#
#
# # Абстрактные методы
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_line(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()


# Classwork 32
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Родитель")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Переместил шахматную фигуру")
#
#
# q = Queen()
# q.draw()
# q.move()

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class EUR(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * EUR.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(EUR.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# e = [EUR(5), EUR(10), EUR(50), EUR(100)]
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Дочерний класс")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("Внучатый класс")
#
#
# g = GrandChild()
# g.display1()
# g.display2()

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_class_method():
#         print("Я - метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Связующий метод")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я - метод вложенного класса", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внутренний", out)
# print(inner.inner_name)
# inner.inner_method()

class Color:
    def __init__(self):
        self.name = "Green"
        self.lg = self.LightGreen()

    def show(self):
        print('Name:', self.name)

    class LightGreen:
        def __init__(self):
            self.name = "Light green"
            self.code = "024avc"

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)


outer = Color()
outer.show()

g = outer.lg
g.display()