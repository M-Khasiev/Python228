class Student:
    def __init__(self, name):
        self.name = name
        self.obj = self.Computer()

    def print_info(self):
        print(f"{self.name} => {self.obj.technical()}")

    class Computer:
        def __init__(self):
            self.title_nt = "HP"
            self.cpu = "i7"
            self.memory = "16"

        def technical(self):
            return f"{self.title_nt}, {self.cpu}, {self.memory}"


s1 = Student("Roman")
s1.print_info()
s2 = Student("Vladimir")
s2.print_info()
