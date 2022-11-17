# Задача № 1
# def func(*args):
#     res = 1
#     for i in args:
#         res *= i
#     return res
#
#
# print(func(10, 9))
# print(func(2, 3, 4))
# print(func(3, 5, 10, 6))

# Задача № 2

# def func(*argh):
#     res = 0
#     lst = []
#     for i in argh:
#         res += i
#         lst.append(res)
#     for i in lst:
#         print(i, end=" ")
#     print()
#
#
# func(3, 9, 1)
# func(2, 5, 4, 2)
# func(3, 5, 10, 6, 3)

# Задача № 3
from math import *


def func(figure_type, **kwargs):
    if figure_type == 'rhombus':
        s = (kwargs['d1'] * kwargs['d2']) / 2
        return s
    elif figure_type == 'square':
        s = kwargs['a'] * kwargs['a']
        return s
    elif figure_type == 'trapezoid':
        s = 1 / 2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
        return s
    elif figure_type == 'circle':
        s = pi * (kwargs['r'] ** 2)
        return s
    else:
        return 'invalid data'


print(func(figure_type='rhombus', d1=10, d2=8))
print(func(figure_type='square', a=5))
print(func(figure_type='trapezoid', a=12, b=3, h=6))
print(func(figure_type='circle', r=18))
print(func(figure_type='unknown', a=1, b=2, c=3))
