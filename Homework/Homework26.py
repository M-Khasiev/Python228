class Book:

    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def print_info(self):
        print(f"Название книги: {self.name}\nГод выпуска: {self.year}\nИздатель: {self.publisher}\n"
              f"Жанр: {self.genre}\nАвтор: {self.author}\nСтоимость книги: {self.price}")

    def get_name(self):
        return self.name

    def set_name(self, n):
        if isinstance(n, str):
            self.name = n

    def get_year(self):
        return self.year

    def set_year(self, y):
        if isinstance(y, str):
            self.year = y

    def get_publisher(self):
        return self.publisher

    def set_publisher(self, p):
        if isinstance(p, str):
            self.publisher = p

    def get_genre(self):
        return self.genre

    def set_genre(self, g):
        if isinstance(g, str):
            self.genre = g

    def get_author(self):
        return self.author

    def set_author(self, a):
        if isinstance(a, str):
            self.author = a

    def get_price(self):
        return self.price

    def set_price(self, p):
        if isinstance(p, str):
            self.price = p


p1 = Book("Великий Гэтсби", "2020 г.", "Эксмо", "Роман", "Фрэнсис Скотт Фицджеральд", "2500р")
p1.print_info()
print(p1.get_name())
print(p1.get_year())
print(p1.get_publisher())
print(p1.get_genre())
print(p1.get_author())
print(p1.get_price())
print("\n\n")

p1.set_name("Портрет Дориана Грея")
p1.set_year("2016 г.")
p1.set_publisher("Эксмо")
p1.set_genre("Готическая литература, Философский роман")
p1.set_author("Оскар Уайльд")
p1.set_price("3000р")

p1.print_info()
print(p1.get_name())
print(p1.get_year())
print(p1.get_publisher())
print(p1.get_genre())
print(p1.get_author())
print(p1.get_price())
