import re


class Automobile:
    def __init__(self, model, year, manufacturer, engine, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, m):
        self.verify_model(m)
        self.__model = m

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.verify_year(y)
        self.__year = y

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, m):
        self.verify_manufacturer(m)
        self.__manufacturer = m

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, e):
        self.verify_engine(e)
        self.__engine = e

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.verify_color(c)
        self.__color = c

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        self.verify_price(p)
        self.__price = p

    @staticmethod
    def verify_model(model):
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")

    @staticmethod
    def verify_year(year):
        if not isinstance(year, str) or len(year) != 4:
            raise TypeError("Год выпуска должен быть строкой и четырехзначным числом")
        for i in year:
            if not i.isdigit():
                raise TypeError("Использовать в строке только числа!")
        r = re.findall(r'^(19[\d][\d]|20[0-2][\d])$', year)
        if not r:
            raise TypeError("Некорректно указан год")

    @staticmethod
    def verify_manufacturer(manufacturer):
        if not isinstance(manufacturer, str):
            raise TypeError("Название производителя может быть только строкой")

    @staticmethod
    def verify_engine(engine):
        if not isinstance(engine, str):
            raise TypeError("Мощность двигателя должна быть строкой")

    @staticmethod
    def verify_color(color):
        if not isinstance(color, str):
            raise TypeError("Цвет машины должен быть строкой")
        for i in color:
            if not i.isalpha():
                raise TypeError("Название цвета должен быть из букв!")

    @staticmethod
    def verify_price(price):
        if not isinstance(price, int):
            raise TypeError("Цена должна быть числом")

    def print_info(self):
        print(str.center(' Данные автомобиля ', 40, "*"))
        print(f"Название модели: {self.__model}")
        print(f"Год выпуска: {self.__year}")
        print(f"Производитель: {self.__manufacturer}")
        print(f"Мощность двигателя: {self.__engine}")
        print(f"Цвет машины: {self.__color}")
        print(f"Цена: {self.__price}")
        print("=" * 40)


auto = Automobile("X7 M50i", "2021", "BMW", "530 л.c.", "White", 10790000)
auto.print_info()
auto.model = "S63 E Perfomance"
auto.year = "2023"
auto.manufacturer = "Mercedes-Benz"
auto.engine = "802 л.с."
auto.color = "Black"
auto.price = 31120000
auto.print_info()


