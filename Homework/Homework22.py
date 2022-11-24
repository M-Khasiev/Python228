import re

# Задача № 1
s = " 1X, Text ABC 123 A1B2C3"
# reg = r'\d[^\d\s]|[^\d\s]\d'
reg = r'[\D]\d[\D]??'
print(re.findall(reg, s))


# Задача № 2
# s = "text from #START# till #END#"
# reg = r'#(\s[A-z]+\s)#'
# print(re.findall(reg, s))


# Задача № 3
# s = "12_34__56"
# reg = r'(\d+)_[^_]+'
# print(re.findall(reg, s))