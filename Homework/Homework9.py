def work(t, n):
    count = 0
    if n not in t:
        return ()
    for i in t:
        if i == n:
            count += 1
    if count > 1:
        a = t.index(n)
        b = t.index(n, a + 1)
        return t[a:b + 1]
    elif count == 1:
        a = t.index(n)
        return t[a:]


print(work((1, 2, 3), 8))
print(work((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(work((1, 2, 8, 5, 1, 2, 9), 8))
