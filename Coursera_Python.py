import re

hand = open('regex_sum_1571845.txt')
res = list()
for i in hand:
    i = i.rstrip()
    stuff = re.findall("[0-9]+", i)
    res.append(stuff)

res_2 = list()
for i in res:
    for j in i:
        if j:
            res_2.append(int(j))

print(sum(res_2))
