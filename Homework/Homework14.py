# Задача № 1
# def func_compute(n):
#     def inner(x):
#         return x * n
#
#     return inner
#
#
# res1 = func_compute(2)
# print(res1(15))
# print(res1(20))
# res2 = func_compute(3)
# print(res2(15))
# print(res2(20))

# Задача № 2

# Вариант 1
s = 0


def func(a, b, c):
    def inner(x, y):
        global s
        s = x * y
        return s

    return 2 * (inner(a, c) + inner(c, b) + inner(a, b))


print(func(2, 4, 6))
print('s=', s)
print(func(5, 8, 2))
print(func(1, 6, 8))


# Вариант 2

def func(a, b, c):
    s = 0

    def inner(x, y):
        nonlocal s
        s = x * y
        return s

    return 2 * (inner(a, c) + inner(c, b) + inner(a, b))


print(func(2, 4, 6))
print(func(5, 8, 2))
print(func(1, 6, 8))


# Вариант 3

def func(a, b, c):
    def inner(x, y):
        s = x * y
        return s

    return 2 * (inner(a, c) + inner(c, b) + inner(a, b))


print(func(2, 4, 6))
print(func(5, 8, 2))
print(func(1, 6, 8))
