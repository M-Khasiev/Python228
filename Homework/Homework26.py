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

    def set_name(self):
        return self.name

    def get_name(self, n):
        if isinstance(n, str):
            self.name = n

    def set_year(self):
        return self.year

    def get_year(self, y):
        if isinstance(y, str):
            self.year = y

    def set_publisher(self):
        return self.publisher

    def get_publisher(self, p):
        if isinstance(p, str):
            self.publisher = p

    def set_genre(self):
        return self.genre

    def get_genre(self, g):
        if isinstance(g, str):
            self.genre = g

    def set_author(self):
        return self.author

    def get_author(self, a):
        if isinstance(a, str):
            self.author = a

    def set_price(self):
        return self.price

    def get_price(self, p):
        if isinstance(p, str):
            self.price = p


p1 = Book("Великий Гэтсби", "1925 г.", "Эксмо", "Роман", "Фрэнсис Скотт Фицджеральд", "2500р")
p1.print_info()
print(p1.set_name())
print(p1.set_year())
print(p1.set_publisher())
print(p1.set_genre())
print(p1.set_author())
print(p1.set_price())

p1.get_name("Портрет Дориана Грея")
p1.get_year("1890 г.")
p1.get_publisher("Эксмо")
p1.get_genre("Готическая литература, Философский роман")
p1.get_author("Оскар Уайльд")
p1.get_price("3000р")

p1.print_info()
print(p1.set_name())
print(p1.set_year())
print(p1.set_publisher())
print(p1.set_genre())
print(p1.set_author())
print(p1.set_price())
