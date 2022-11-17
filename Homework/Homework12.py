#  Задача № 1
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {5: 50, 6: 60}
print(a, '\t', b, '\t', c, '\n', sep="")
general = {**a, **b, **c}
print(general)


#  Задача № 2
# d = {
#     'emp1': {
#         'name': 'John',
#         'salary': 7500
#     },
#     'emp2': {
#         'name': 'Emma',
#         'salary': 8000
#     },
#     'emp3': {
#         'name': 'Brad',
#         'salary': 6500
#     }
# }
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j, ':', d[i][j])
#
# print('\n')
# print("Если введете некорректно имя пользователя, изменений данных не произойдет!", '\n')
# p = input("Введите имя : ")
# z = int(input("Введите новую зарплату: "))
# print()
# if p == 'John':
#     d['emp1']['salary'] = z
# elif p == 'Emma':
#     d['emp2']['salary'] = z
# elif p == 'Brad':
#     d['emp3']['salary'] = z
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j, ':', d[i][j])
# while True:
#     j = int(input("Желаете ещё раз поменять зарплату пользователю? (Введите 0 - если нет, 1 - если да): "))
#     print()
#     if j == 1:
#         p = input("Введите имя : ")
#         z = int(input("Введите новую зарплату: "))
#         if p == 'John':
#             d['emp1']['salary'] = z
#         elif p == 'Emma':
#             d['emp2']['salary'] = z
#         elif p == 'Brad':
#             d['emp3']['salary'] = z
#         for i in d:
#             print(i)
#             for j in d[i]:
#                 print(j, ':', d[i][j])
#         print()
#     elif j == 0:
#         break

#  Задача № 3
# k = int(input("Количество студентов: "))
# st = {input(str(i) + "-й студент: "): int(input("Балл: ")) for i in range(1, k + 1)}
# num_1, num_2, res = 0, 0, 0
# for i in st.values():
#     num_1 = num_1 + i
#     num_2 = num_2 + 1
# res = round(num_1 / num_2)
# print("Средний балл: " + str(res) + '. Студенты с баллом выше среднего:')
# for i in st:
#     if st[i] > res:
#         print(i)
