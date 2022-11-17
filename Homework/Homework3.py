try:
    a = int(input("Введите начало диапазона: "))
    b = int(input("Введите конец диапазона: "))
    res = 0

    if a < b:
        while a <= b:
            if a % 2:
                res = a + res
            a += 1
        print("Сумма целых нечетных чисел:", res)
    elif a > b:
        while b <= a:
            if b % 2:
                res = b + res
            b += 1
        print("Сумма целых нечетных чисел:", res)
    else:
        print("Ошибка ввода данных")
except ValueError:
    print("Введите корректно диапазон")
