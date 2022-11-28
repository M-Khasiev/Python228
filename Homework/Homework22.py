import re

# Задача № 1
s = "1X, Text ABC 123 A1B2C3"
reg = r'(\d)[^\d\s]|[^\d\s](\d)'
res = re.findall(reg, s)
lst = list()
for i in res:
    for j in i:
        if '1234567890'.find(j) != -1 and j != '':
            lst.append(j)
print(lst)


# Задача № 2
s = "text from #START# till #END#"
reg = r'#(\s[A-z]+\s)#'
print(re.findall(reg, s))


# Задача № 3
s = "12_34__56"
reg = r'(\d+)_[^_]+'
print(re.findall(reg, s))