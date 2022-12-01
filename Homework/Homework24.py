f = open("text.txt", "w")
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
f.close()

f = open('text.txt', 'r')
read_line = f.readlines()
f.seek(0)
print(f.read())

n = int(input("pos1 = "))
m = int(input("pos2 = "))

if 0 <= n < len(read_line) and 0 <= m < len(read_line):
    read_line[n], read_line[m] = read_line[m], read_line[n]
else:
    print('\nТакой строки нет!')
f.close()


f = open('text.txt', 'w+')
f.writelines(read_line)
f.seek(0)
print("\n", f.read(), sep="")
f.close()