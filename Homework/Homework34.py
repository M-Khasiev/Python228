from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def print_figure(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side: int, color):
        self.side = side
        super().__init__(color)

    def square(self):
        return f"Площадь: {self.side * self.side}"

    def perimetr(self):
        return f"Периметр: {self.side * 4}"

    def info(self):
        return f"===Квадрат===\nСторона:{self.side}\nЦвет: {self.color}\n{self.square()}\n{self.perimetr()}"

    def print_figure(self):
        for i in range(self.side):
            print("*", end="")
            for j in range(self.side - 1):
                print("*", end="")
            print()


class Rectangle(Shape):
    def __init__(self, height: int, width: int, color):
        self.height = height
        self.width = width
        super().__init__(color)

    def square(self):
        return f"Площадь: {self.height * self.width}"

    def perimetr(self):
        return f"Периметр: {2 * (self.height + self.width)}"

    def info(self):
        return f"===Прямоугольник===\nДлина: {self.height}\nШирина: {self.width}\nЦвет: {self.color}\n{self.square()}" \
               f"\n{self.perimetr()}"

    def print_figure(self):
        for i in range(self.height):
            print("*", end="")
            for j in range(self.width):
                print("*", end="")
            print()


class Triangle(Shape):
    def __init__(self, side1: int, side2: int, side3: int, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__(color)

    def square(self):
        sm_per = (self.side1 + self.side2 + self.side3) / 2
        return f"Площадь: " \
               f"{round(math.sqrt(sm_per * (sm_per - self.side1) * (sm_per - self.side2) * (sm_per - self.side3)), 2)}"

    def perimetr(self):
        return f"Периметр: {self.side1 + self.side2 + self.side3}"

    def info(self):
        return f"===Треугольник===\nСторона 1: {self.side1}\nСторона 2: {self.side2}\n" \
               f"Сторона 3: {self.side3}\n{self.square()}\n{self.perimetr()}"

    def print_figure(self):
        lst = [self.side1, self.side2, self.side3]
        n = min(lst)
        for i in range(n):
            print(" " * (n - i - 1) + "*" * (2 * i + 1))


lst = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]
for i in lst:
    print(i.info())
    i.print_figure()
    print()
