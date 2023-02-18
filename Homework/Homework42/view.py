def decorator_mk(ar):
    def wrapper(fn):
        def arguments_method(*args, **kwargs):
            print(ar.center(49, "="))
            f = fn(*args, **kwargs)
            print("=" * 50)
            return f

        return arguments_method

    return wrapper


class Interface:
    @decorator_mk(" Редактирование данных каталога фильма ")
    def giving_choice(self):
        print("Действия с фильмами:\n1 - добавление фильма\n2 - каталог фильма\n3 - просмотр определенного фильма\n"
              "4 - удаление фильма\nq - выход из программы")
        choice = input("Выберите вариант действия: ")
        return choice

    @decorator_mk(" Добавление фильма ")
    def view_data_recording(self):
        d = {
            "Название фильма": None,
            "Жанр": None,
            "Режиссер": None,
            "Год выпуска": None,
            "Длительность": None,
            "Студия": None,
            "Актёры": None
        }
        for i in d:
            d[i] = input(f"Введите {i}: ").strip()
        return d

    @decorator_mk(" Каталог фильмов ")
    def view_movie_available(self, data):
        if data:
            for index, i in enumerate(data.values(), 1):
                print(f"{index}. {i['Название фильма']} ({i['Год выпуска']})")
        else:
            print("Ваш каталог пуст")

    @decorator_mk(" Информация о фильме ")
    def view_watching_specific_movie(self):
        cinema = input("Введите название фильма, который вы хотите просмотреть: ")
        return cinema.strip()

    @decorator_mk(" Информация о фильме ")
    def movie_information(self, cinema):
        for i in cinema:
            print(f"{i}: {cinema[i]}")

    @decorator_mk(" Удаление фильма ")
    def view_delete_specific_movie(self):
        cinema = input("Введите название фильма, который вы хотите удалить: ")
        return cinema.strip()

    @decorator_mk(" Удалённый фильм ")
    def view_delete_information_movie(self, cinema):
        print(f"Фильм {cinema['Название фильма']}({cinema['Год выпуска']}) удалён из каталога")

    @decorator_mk(" Предупреждение: ")
    def absense(self):
        print("Данный фильм отсутствует в вашем каталоге")

    @decorator_mk(" Предупреждение: ")
    def input_error(self, option):
        print(f"Варианта {option} не существует")

    def end_programm(self):
        print("Программа завершена.")
