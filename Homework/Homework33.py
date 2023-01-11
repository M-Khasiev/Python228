# Вариант 1 (Только Пол)
import random


class Cat:
    def __init__(self, name: str, age: int, sex: str):
        if 'M' in sex:
            print(name, "is good boy!!!")
        elif 'F' in sex:
            print(name, "is good girl!!!")
        else:
            raise ValueError("Укажите мужской ('M') или женский ('F') пол")
        self.name = name
        self.age = age
        self.sex = sex

    def __add__(self, other):
        if self.sex == other.sex:
            raise ValueError("Пол животных должен быть разным")
        p = ["M", "F"]
        n = [f"Cat(name='No name', age=0, sex= {random.choice(p)})" for i in range(random.randint(1, 10))]
        return n


c1 = Cat("Tom", 7, 'M')
c2 = Cat("Elsa", 5, 'F')
print(c1 + c2)


# Вариант 2 (Имя и Пол)
class Cat:
    def __init__(self, name: str, age: int, sex: str):
        if 'M' in sex:
            print(name, "is good boy!!!")
        elif 'F' in sex:
            print(name, "is good girl!!!")
        else:
            raise ValueError("Укажите мужской ('M') или женский ('F') пол")
        self.name = name
        self.age = age
        self.sex = sex

    def __add__(self, other):
        if self.sex == other.sex:
            raise ValueError("Пол животных должен быть разным")
        p = ["M", "F"]
        name_cats1 = ["Alex", "Sean", "Barney", "Henry", "Jerry", "Leo", "Martin", "Oscar", "Jasper", "Austin", "Sam",
                      "Bruce", "Richard", 'Simon', 'Felix']
        name_cats2 = ["Lucy", "Molly", "Daisy", "Betsy", "Michelle", "Grace", "Monica", "Samantha", "Hannah",
                      "Charlotte", "Alice", "Jessica", "Mia", "Simone", "Fiona", "Elsa"]
        n = list()
        for i in range(random.randint(1, 10)):
            pol = random.choice(p)
            if pol == "M":
                male_name = random.choice(name_cats1)
                n.append(f"Cat(name = {male_name}, age=0, sex= {pol}")
            elif pol == "F":
                male_name = random.choice(name_cats2)
                n.append(f"Cat(name = {male_name}, age=0, sex= {pol}")
        return n


c1 = Cat("Tom", 7, 'M')
c2 = Cat("Elsa", 5, 'F')
print(c1 + c2)
