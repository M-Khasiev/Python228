import math


class Rectangle:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Rectangle.__check_value(x) and Rectangle.__check_value(y):
            self.__x = x
            self.__y = y

    def __check_value(num):
        if isinstance(num, int):
            return True
        return False

    def set_data_x(self, x):
        if Rectangle.__check_value(x):
            self.__x = x
        else:
            print("Вводимые данные должны быть числами!")

    def set_data_y(self, y):
        if Rectangle.__check_value(y):
            self.__y = y
        else:
            print("Вводимые данные должны быть числами!")

    def get_data(self):
        print(f"Длина прямоугольника: {self.__x}\nШирина прямоугольника: {self.__y}")

    def get_data_x(self):
        return self.__x

    def get_data_y(self):
        return self.__y

    def area(self):
        print(f"Площадь прямоугольника: {self.__x * self.__y}")

    def perimeter(self):
        print(f"Периметр прямоугольника: {(self.__x * 2) + (self.__y * 2)}")

    def hypotenuse(self):
        print(f"Гипотенуза прямоугольника: {round(math.sqrt((self.__x ** 2) + (self.__y ** 2)), 2)}")

    def print_rectangle(self):
        for i in range(self.__x):
            print("*", end="")
            for j in range(self.__y):
                print("*", end="")
            print()


p1 = Rectangle(3, 9)
p1.get_data()
p1.area()
p1.perimeter()
p1.hypotenuse()
p1.print_rectangle()
print("\n\n")

p1.set_data_x(7)
p1.set_data_y(15)
p1.get_data()
p1.area()
p1.perimeter()
p1.hypotenuse()
p1.print_rectangle()
