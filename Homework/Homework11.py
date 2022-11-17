people = {
    'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
    'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
    'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
}
for i in people:
    print(i)
    for j in people[i]:
        print(j, ':', people[i][j])
try:
    n = input("Имя: ")
    r = input("Регион: ")
    print(people[n][r])
    new_z = int(input("Новое значение: "))
    people[n][r] = new_z
    print(people[n])
except KeyError:
    print("Такого ключа или его значения не существует!")