#  Задача № 1
def krt(ch):
    lst = []
    for i in ch:
        if i > 0:
            if i % 13 == 0:
                lst.append(i)
    if len(lst):
        return max(lst)
    else:
        return "no such numbers"


a = [int(input('-> ')) for i in range(int(input("Введите желаемое кол-во чисел в списке: ")))]
print(krt(a))
# print(krt([2, 7, 0, 1, 5]))
# print(krt([2, 7, 0, 1, 5, -13, 13]))
# print(krt([26]))
# print(krt([99, 99, 100, 34, -39]))
# print(krt([99, 39, 99, 100, 34]))


#  Задача № 2

# s = ('ab', 'abcd', 'cde', 'abc', 'def')
# print("Исходный кортеж:", s)
# a = input("s = ")
# if a in s:
#     print("Yes")
# else:
#     print("No")


#  Задача № 3
# print("Введите статистику частотности символов в кортеже", end="\n\n")
# a = input("Введите по порядку, без пробелов, элементы кортежа: ")
# a = tuple(a)
# print(a)
# lst = []
# for i in a:
#     if i not in lst:
#         lst.append(i)
# for j in lst:
#     print("Количество", j, "=", a.count(j))
