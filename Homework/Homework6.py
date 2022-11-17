# Задание № 1
n = [(int(input("Введите элемент списка: "))) for i in range(int(input("Введите длину списка: ")))]
m = []
print("Список: ", n)
for i in range(len(n)):
    if n[i] > 0:
        m.append(n[i])
print("Новый список состоящий из положительных элементов: ", m)
res = 0
for i in m:
    if i > res:
        res = i
print("Наибольший элемент списка:", res)

# Задание № 2
# n = [(int(input("-> "))) for i in range(int(input("Введите элементы списка:\n n =  ")))]
# k = int(input("Введите индекс:\nk = "))
# c = int(input("Введите значение:\nc = "))
# n.insert(k, c)
# print(n)


# Задание № 3
# n = [(int(input("-> "))) for i in range(int(input("Введите элементы списка:\n n =  ")))]
# ch = int(input("Введите число: \nch = "))
# if ch in n:
#     print("Число присутствует в элементах списка")
# else:
#     print("Число отсутствует в элементах списка")
