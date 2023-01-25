import json


# Вариант 1 (Статические свойства)

def annual_income(summa: int):
    return summa


class PersonData:
    name = 'John'
    surname = 'Wick'
    age = 42
    resides = 'New York'
    cars = ['Mercedes-Benz', 'Audi', 'Mustang']
    children = ('Mark', 'Bella', 'Joseph')
    foot_size = 43.5
    married = True
    education = {
        'Stanford University': "Bachelor's degree",
        'Harvard University': "Master's degree",
        'Time spent on education': {
            'Stanford': 3,
            'Harvard': 1
        }
    }
    income = annual_income(100000)


dt = dict(PersonData.__dict__)
lst = list()
for i, j in dt.items():
    if i.startswith("__"):
        lst.append(i)
for i in lst:
    del dt[i]
json_string = json.dumps(dt)
data = json.loads(json_string)
print(data)
print()


# Вариант 2 (Динамические свойства)

class PersonData2:
    def __init__(self, name, surname, age, resides, cars, children, foot_size, married, education, money):
        self.name = name
        self.surname = surname
        self.age = age
        self.resides = resides
        self.cars = cars
        self.children = children
        self.foot_size = foot_size
        self.married = married
        self.education = education
        self.income = self.annual_income2(money)

    @staticmethod
    def annual_income2(summa: int):
        return summa


p1 = PersonData2('John', 'Wick', 42, 'New York', ['Mercedes-Benz', 'Audi', 'Mustang'], ('Mark', 'Bella', 'Joseph'),
                 43.5, True, {'Stanford University': "Bachelor's degree", 'Harvard University': "Master's degree",
                              'Time spent on education': {'Stanford': 3, 'Harvard': 1}}, 100000)
json_string2 = json.dumps(p1.__dict__)
data2 = json.loads(json_string2)
print(data2)
