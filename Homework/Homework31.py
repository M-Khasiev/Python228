import math


class Table:
    def __init__(self, width=None, height=None, radius=None):
        if radius is None:
            self.width = width
            self.height = height
        if height is None and radius is None:
            self.width = width
            self.height = width
        if width is None and height is None:
            self.radius = radius

    def square(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод square()")

    @staticmethod
    def is_int(a):
        if not isinstance(a, (int, float)):
            return False
        return True


class Rectangular(Table):
    def square(self):
        if self.is_int(self.width) and self.is_int(self.height):
            return self.width * self.height
        else:
            return "Введенные данные должны быть целочисленными или вещественными!"


class Circle(Table):
    def square(self):
        if self.is_int(self.radius):
            return round(math.pi * (self.radius ** 2), 2)
        else:
            return "Введенные данные должны быть целочисленными или вещественными!"


t1 = Rectangular(20, 10)
print(t1.__dict__)
print(t1.square())
t2 = Rectangular(20)
print(t2.__dict__)
print(t2.square())
t3 = Circle(radius=20)
print(t3.__dict__)
print(t3.square())
