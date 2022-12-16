import math


class Square:
    __count = 0

    @staticmethod
    def formula_herons(a, b, c):
        p = 0.5 * (a + b + c)
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        Square.__count += 1
        return s

    @staticmethod
    def sq_base_height(a, b):
        s = (a * b) / 2
        Square.__count += 1
        return s

    @staticmethod
    def sq_area(a):
        s = a * a
        Square.__count += 1
        return s

    @staticmethod
    def rectangle_area(a, b):
        s = a * b
        Square.__count += 1
        return s

    @staticmethod
    def amount():
        return Square.__count


print("Площадь треугольника по формуле Герона:", Square.formula_herons(3, 4, 5))
print("Площадь треугольника через основание и высоту:", Square.sq_base_height(6, 7))
print("Площадь квадрата:", Square.sq_area(7))
print("Площадь прямоугольника:", Square.rectangle_area(2, 6))
print("Количество подсчетов площади:", Square.amount())
