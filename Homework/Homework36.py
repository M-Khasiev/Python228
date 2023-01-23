import random


class ValidateString:
    @staticmethod
    def data_input(arg):
        if not isinstance(arg, int) or arg < 0:
            raise ValueError(f"Данные должны быть целыми положительным числами")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.data_input(value)
        instance.__dict__[self.name] = value


class Triangle:
    st1 = ValidateString()
    st2 = ValidateString()
    st3 = ValidateString()

    def __init__(self, st1: int, st2: int, st3: int):
        self.st1 = st1
        self.st2 = st2
        self.st3 = st3

    def existing_triangle(self):
        if self.st1 + self.st2 > self.st3 and self.st2 + self.st3 > self.st1 and self.st1 + self.st3 > self.st2:
            return f"Треугольник со сторонами ({self.st1}, {self.st2}, {self.st3}) существует."
        else:
            return f"Треугольник со сторонами ({self.st1}, {self.st2}, {self.st3}) не существует."


t1 = [Triangle(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for i in range(10)]
for i in t1:
    print(i.existing_triangle())
