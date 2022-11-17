#  Задача № 1
from random import *

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for i in a:
    for j in i:
        print(j, end="\t")
    print()
print()
for i in range(len(a)):
    for j in range(1):
        print(a[i][0], end="\t")
print()
for i in range(len(a)):
    for j in range(1):
        print(a[i][1], end="\t")
print()
for i in range(len(a)):
    for j in range(1):
        print(a[i][2], end="\t")
print()
for i in range(len(a)):
    for j in range(1):
        print(a[i][3], end="\t")


#  Задача № 2
# x, y = 6, 6
# a = [[randint(0, 10) for j in range(y)] for i in range(x)]
# for i in a:
#     for j in i:
#         print(j, end="\t\t")
#     print()
# print()
#
# b = [randint(0, 10) for i in range(x)]
# print(b)
#
# print()
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i % 2 == 0:
#             print(b[j], end="\t\t")
#         else:
#             print(a[i][j], end="\t\t")
#     print()
