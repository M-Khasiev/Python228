a = [int(input("-> ")) for i in range(int(input("Введите элементы списка:\nn = ")))]

for i in range(len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end=" ")
