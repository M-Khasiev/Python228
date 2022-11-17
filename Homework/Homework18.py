#  Задача № 1

# s = "Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
# Способ № 1
# a = s.index("(") + 1
# b = s.index(")")
# print(s[a:b])

# Способ № 2
# print(s.strip("Дастнющся ").strip("()"))

# Способ № 3
# print(s.lstrip("Данст ").rstrip("ающяс").strip("()"))

# Способ № 4
# for i in range(len(s)):
#     if s.index("(") < i < s.index(")"):
#         print(s[i], end="")

# Способ № 5
# for i in s[s.index("(") + 1:s.index(")")]:
#     print(i, end="")


# Задача № 2

# s = input("Строка: ")
# a = input("Её заменяемая подстрока: ")
# b = input("Новая подстрока: ")

# Способ № 1
# c = s.replace(a, b)
# print(c)

# Способ № 2
# c = s.split()
# for i in c:
#     if i == a:
#         i = b
#     print(i, "", end="")


# Задача № 3

# s = '''
# Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели.
# '''
# print(s)

# Способ № 1
# c = 0
# c += s.count(" е")
# c += s.count("Е")
# print("Количество слов:", c)

# Способ № 2
# c = s.split()
# res = 0
# for i in c:
#     if i[0] == "Е" or i[0] == "е":
#         res += 1
#
# print("Количество слов:", res)
