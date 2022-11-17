def func(n):
    s = bin(n)
    s = int(s[2:])
    return s


while True:
    a = int(input("-> "))
    if a == 0:
        break
    else:
        print(func(a))
