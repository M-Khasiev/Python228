# Задача №1
# a = int(input("Начало диапазона: "))
# b = int(input("Конец диапазона: "))
# if a > b:
#     while a >= b:
#         if a % 2:
#             print(str(a) + " ", end="")
#         a -= 1
# elif a < b:
#     while a <= b:
#         if a % 2:
#             print(str(a) + " ", end="")
#         a += 1

# Задача №2
# print("\"Угадай число\"\nПопробуйте угадать число от 1 до 100.\nДля выхода из игры введите 0.", end="\n\n")
# res = 0
# try:
#     while True:
#         a = int(input("Введите число от 1 до 100: "))
#         if a == 0:
#             print("Вы вышли из игры...\nЕсли хотите попробовать снова, запустите программу заново.")
#             break
#         elif 1 <= a <= 100:
#             if a < 41:
#                 print("Загаданное число больше")
#             elif a > 41:
#                 print("Загаданное число меньше")
#             res += 1
#             if a == 41:
#                 print("\nПоздравляю!\nВы угадали число с " + str(res) + " раза")
#                 break
#         else:
#             print("Вводите числа указанные в условии!")
# except ValueError:
#     print("Ошибка ввода данных")
