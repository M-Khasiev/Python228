# Задача № 1
a = 0


def func_rec(n):
    global a
    if len(n) == 0:
        return
    if n[0] < 0:
        a += 1
    func_rec(n[1:])


h = [-2, 3, 8, -11, -4, 6]
func_rec(h)
print(h)
print('n =', a)

# Задача № 2

names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
print(names)
res = 0
for i in names:
    if i == str(i):
        res += 1
    elif i == list(i):
        for j in i:
            if j == str(j):
                res += 1
            elif j == list(j):
                for k in j:
                    res += 1
print(res)
