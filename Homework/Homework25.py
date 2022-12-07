import os


# Задача № 1

with open(r'C:\Python228\one.txt', 'r') as f1, open(r'C:\Python228\two.txt', 'r') as f2:
    str_0 = f1.readlines()
    str_2 = f2.readlines()
res = 1
str_1 = list()
for i in str_0:
    i = i.replace(f"Строка №{res}\n", f"Строка №{res}. ")
    str_1.append(i)
    res += 1
with open(r'C:\Python228\three.txt', 'w') as f3:
    for i in range(len(str_1)):
        f3.write(str_1[i])
        f3.write(str_2[i])
with open(r'C:\Python228\three.txt', 'r') as f3:
    print(f3.read())


# Задача № 2

def func_wlk(f, tpd):
    if tpd:
        print(f'Обход {f} сверху вниз')
    else:
        print(f'Обход {f} снизу вверх')
    for root, dirs, files in os.walk(f, topdown=tpd):
        print(root)
        print(dirs)
        print(files)
    print('-' * 35)


func_wlk('C:\Python228\Work', tpd=True)
func_wlk('C:\Python228\Work', tpd=False)
